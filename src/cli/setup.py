import typer
from src.utils import db
from src.utils.console import console

app = typer.Typer()


@app.command()
def init():
    console.log("initializing the database")
    db.create_all("todos.db")