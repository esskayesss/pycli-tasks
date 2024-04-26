import typer
from src.cli import categories, tasks, setup
from src.utils import db

app = typer.Typer(
    name="Todos CLI",
    help="A simple CLI for managing your todos.",
    rich_markup_mode="rich",
    no_args_is_help=True
)

app.add_typer(categories.app, name="categories")
app.add_typer(tasks.app, name="tasks")
app.add_typer(setup.app, name="setup")

if __name__ == "__main__":
    db.create_all("todos.db")
    app()
