from sqlite3 import connect

from pathlib import Path


NAME_DB = "./db/study.db"

SQL_FOLDER = "./sql/"

READY_REQUESTS = [1, 4]


def delete_old_sql_files() -> None:
    for number_request in range(1, 13):
        if number_request not in READY_REQUESTS:
            sql_file = Path(f"query_{number_request}.sql")
            if sql_file.is_file():
                sql_file.unlink()


def create_db() -> None:
    with open(f"{SQL_FOLDER}study_create.sql", "r") as f:
        sql = f.read()

    with connect(NAME_DB) as con:
        cur = con.cursor()
        cur.executescript(sql)


if __name__ == "__main__":
    create_db()
    delete_old_sql_files()
