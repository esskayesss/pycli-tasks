from src.utils.db import get_connection
from src.utils.console import console, error_console
from sqlite3 import Error as SQLiteError
from src.models.category import Category
conn = get_connection()


def add_category(
    name: str,
):
    try:
        c = conn.cursor()
        c.execute('''
            INSERT INTO Category (name)
            VALUES (?);
        ''', (name,))
        conn.commit()
        console.log(f"Category added successfully. [{name}]")
    except SQLiteError as e:
        error_console.log(e)


def list_categories():
    try:
        c = conn.cursor()
        c.execute('''
            SELECT * FROM Category;
        ''')
        results = c.fetchall()
        categories = []
        for result in results:
            category = Category(
                ID=result[0],
                name=result[1]
            )
            categories.append(category)
        return categories
    except SQLiteError as e:
        error_console.log(e)


def get_category(id: int) -> Category:
    try:
        c = conn.cursor()
        c.execute('''
            SELECT * FROM Category WHERE id = ?;
        ''', (id,))
        result = c.fetchone()
        category = Category(
            ID=result[0],
            name=result[1]
        )
        return category
    except SQLiteError as e:
        error_console.log(e)


def delete_category(category: Category):
    try:
        c = conn.cursor()
        c.execute('''
            DELETE FROM Category WHERE id = ?;
        ''', (category.ID,))
        conn.commit()
        console.log("Category deleted successfully.")
    except SQLiteError as e:
        error_console.log(e)
