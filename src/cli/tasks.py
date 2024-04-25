import typer
from rich.prompt import Prompt
from rich.table import Table
from src.db import tasks as tasks_conn
from src.db import categories as categories_conn
from src.models.tasks import Task
from src.utils.console import console
from src.cli.categories import table_categories

app = typer.Typer()


@app.command(name="add")
def add_todo():
    title = Prompt.ask("Title the task to add")
    description = Prompt.ask("Describe the task")
    priority = Prompt.ask("Priority of the task")
    categories = categories_conn.list_categories()
    table_categories(categories)
    category = int(Prompt.ask("Category of the task"))
    category = categories[category]
    new_task = Task(title, description, priority, category_id=category.ID)
    tasks_conn.add_task(new_task)


@app.command(name="list")
def list_todos(a: bool = False):
    tasks = tasks_conn.list_tasks()
    active_tasks = [task for task in tasks if task.status.value == 0]
    completed_tasks = [task for task in tasks if task.status.value == 1]
    active_tasks.sort(key=lambda x: x.priority, reverse=True)
    tasks = active_tasks
    if a:
        completed_tasks.sort(key=lambda x: x.priority, reverse=True)
        active_tasks.extend(completed_tasks)

    tasks_table(tasks)


@app.command(name="complete")
def complete_todo():
    tasks = tasks_conn.list_tasks()
    tasks.sort(key=lambda x: x.priority, reverse=True)
    tasks = [task for task in tasks if task.status.value == 0]
    tasks_table(tasks)
    task_id = int(Prompt.ask("Enter the task id to complete"))
    task = tasks[task_id]
    tasks_conn.update_task_status(task, 1)


@app.command(name="delete")
def delete_todo():
    tasks = tasks_conn.list_tasks()
    tasks.sort(key=lambda x: x.priority, reverse=True)
    tasks_table(tasks)
    task_id = int(Prompt.ask("Enter the task id to delete"))
    tasks_conn.delete_task(tasks[task_id])


def tasks_table(tasks: [Task]):
    table = Table(title="Tasks")
    table.add_column("idx", style="cyan")
    table.add_column("Title")
    table.add_column("Description")
    table.add_column("Priority")
    table.add_column("Status")
    table.add_column("Category")
    for (idx, task) in enumerate(tasks):
        table.add_row(
            str(idx),
            task.name,
            task.description,
            str(task.priority),
            str(task.status.name),
            categories_conn.get_category(task.category_id).name,
        )
    console.print(table)