from sqlite3 import connect

from create_db import NAME_DB

from create_db import SQL_FOLDER


def input_in_range(text: str, begin: int, end: int) -> int:
    while True:
        number = input(f"{text}({begin}...{end}): ")
        if number.isdigit():
            result = int(number)
            if begin - 1 < result < end + 1:
                break
    return result


def choice_of(name_sql: str) -> tuple[int, str]:
    with open(f"{SQL_FOLDER}{name_sql}", "r") as f:
        sql = f.read()

    with connect(NAME_DB) as con:
        cur = con.cursor()
        cur.execute(sql)
        list_of_choice = cur.fetchall()

    [print(f"{choice[0]} - {choice[1]}") for choice in list_of_choice]
    choice_number = input_in_range("Enter the subject number", 1, len(list_of_choice))

    return list_of_choice[choice_number - 1]


def choice_of_subject() -> tuple[int, str]:
    return choice_of("query_subject.sql")


def choice_of_lector() -> tuple[int, str]:
    return choice_of("query_lector.sql")


def choice_of_group() -> tuple[int, str]:
    return choice_of("query_group.sql")


def choice_of_student() -> tuple[int, str]:
    return choice_of("query_student.sql")
