import typer
from typing import Optional
from typing_extensions import Annotated, List
from rich.prompt import Prompt
from rich.table import Table
from src.db import categories as categories_conn
from src.models.category import Category
from src.utils.console import console, error_console

app = typer.Typer()


@app.command(name="add")
def add_category(names: List[str]):
    for name in names:
        categories_conn.add_category(name)


@app.command(name="list")
def list_categories():
    categories_list = categories_conn.list_categories()
    print(categories_list)


@app.command(name="delete")
def delete_category():
    categories = categories_conn.list_categories()
    table_categories(categories)
    category_id = int(Prompt.ask("Enter the category id to delete"))
    categories_conn.delete_category(categories[category_id])


def table_categories(categories: [Category]):
    table = Table(title="Categories")
    table.add_column("idx", style="cyan")
    table.add_column("Name")
    for (idx, category) in enumerate(categories):
        table.add_row(str(idx), category.name)
    console.print(table)