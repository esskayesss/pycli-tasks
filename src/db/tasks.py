from sqlite3 import Error as SQLiteError
from src.utils.db import get_connection
from src.utils.console import console, error_console
from src.models.tasks import Task
conn = get_connection()


def add_task(task: Task):
    try:
        c = conn.cursor()
        c.execute('''
            INSERT INTO Todo (name, description, priority, status_id, category_id)
            VALUES (?, ?, ?, ?, ?);
        ''', (task.name, task.description, task.priority, task.status.value, task.category_id))
        conn.commit()
        console.log("Task added successfully.")
    except SQLiteError as e:
        error_console.log(e)


def list_tasks():
    try:
        c = conn.cursor()
        c.execute('''
            SELECT * FROM Todo;
        ''')
        results = c.fetchall()
        tasks=[]
        for result in results:
            task = Task(
                ID=result[0],
                name=result[1],
                description=result[2],
                priority=result[3],
                status_id=result[4],
                category_id=result[5]
            )
            tasks.append(task)
        return tasks
    except SQLiteError as e:
        error_console.log(e)


def update_task_status(task: Task, status_id: int):
    try:
        c = conn.cursor()
        c.execute('''
            UPDATE Todo SET status_id = ? WHERE id = ?;
        ''', (status_id, task.ID))
        conn.commit()
        console.log("Task status updated successfully.")
    except SQLiteError as e:
        error_console.log(e)


def delete_task(task: Task):
    try:
        c = conn.cursor()
        c.execute('''
            DELETE FROM Todo WHERE id = ?;
        ''', (task.ID,))
        conn.commit()
        console.log("Task deleted successfully.")
    except SQLiteError as e:
        error_console.log(e)