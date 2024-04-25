import sqlite3
from sqlite3 import Error as SQLiteError
from src.utils.console import console, error_console
conn = None


def create_connection(db_file):
    global conn
    if conn is not None:
        return
    try:
        conn = sqlite3.connect(db_file)
        console.log(f'Connection to {db_file} successful')
    except SQLiteError as e:
        error_console.log(f"Error while connecting to {db_file}: {e}")


def get_connection():
    global conn
    create_connection("todos.db")
    return conn


def create_all(db_file):
    if conn is None:
        create_connection(db_file)
    try:
        c = conn.cursor()

        # create the status table
        c.execute('''
            CREATE TABLE IF NOT EXISTS Status (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL UNIQUE
            );
        ''')

        # insert the statuses this cannot be altered later
        c.execute("INSERT OR IGNORE INTO Status (id, name) VALUES (0, 'Active'), (1, 'Complete'), (2, 'Archived');")

        # create the categories table
        c.execute('''
            CREATE TABLE IF NOT EXISTS Category (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL UNIQUE
            );
        ''')
        c.execute("INSERT OR IGNORE INTO Category (id, name) VALUES (0, 'Uncategorized');")
        # category deletion trigger
        conn.execute('''
        CREATE TRIGGER SetDefaultCategoryId
        AFTER DELETE ON Category
        FOR EACH ROW
        BEGIN
            UPDATE Todo SET category_id = 0 WHERE category_id = OLD.id;
        END;
        ''')

        # create the todos table
        c.execute('''
            CREATE TABLE IF NOT EXISTS Todo (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                description TEXT,
                priority INTEGER CHECK(priority BETWEEN 0 AND 9),
                status_id INTEGER,
                category_id INTEGER DEFAULT 0,
                FOREIGN KEY (status_id) REFERENCES Status(id),
                FOREIGN KEY (category_id) REFERENCES Category(id) ON DELETE SET DEFAULT
            );
        ''')

        # committing the changes
        conn.commit()
        console.log("the required tables were created successfully.")
    except SQLiteError as e:
        error_console.log(e)
    finally:
        if conn:
            conn.close()
            console.log("connection closed successfully.")
