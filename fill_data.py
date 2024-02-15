from sqlite3 import connect

from sqlite3 import Error

from sqlite3 import Connection

from create_db import NAME_DB

from faker import Faker

from random import randint

from datetime import date

from datetime import timedelta


NUMBER_STUDENTS = 50
NUMBER_GROUPS = 3
NUMBER_SUBJECTS = 8
NUMBER_LECTORS = 5
NUMBER_MARKS = (12, 20)

MARKS_RANGE = (1, 12)

START_DATE = date(2024, 1, 8)


GROUPS = ["IT-25", "PM-45", "MC-12"]

SUBJECTS = [
    "Math",
    "History",
    "Ukrainian",
    "English",
    "Astronomy",
    "Physics",
    "Chemistry",
    "Literature",
]

NAME = "name"


def convert_list_fields(list_field: list[str]) -> tuple[str, str]:
    # table_field - name, begin_date, end_date
    # question_marks - ?,?,?
    list_field_str = ""
    question_marks = ""
    for field in list_field:
        list_field_str = f"{list_field_str}{field},"
        question_marks = f"{question_marks}?,"
    return (
        list_field_str[: len(list_field_str) - 1],
        question_marks[: len(question_marks) - 1],
    )


def convert_to_tuple(list_data: list) -> list[tuple[str,]]:
    return [(field,) for field in list_data]


def fake_names(number: int) -> list[str]:
    return [Faker().name() for _ in range(number)]


def fake_names_ids(number: int, range_of_ids: int) -> list[tuple[str, int]]:
    fake_list = []
    for _ in range(number):
        fake_list.append((Faker().name(), randint(1, range_of_ids)))
    return fake_list


def subjects_ids(number: int, range_of_ids: int) -> list[tuple[str, int]]:
    while True:
        ids = set()
        fake_list = []
        for i in range(number):
            id_of_lector = randint(1, range_of_ids)
            ids.add(id_of_lector)
            fake_list.append((SUBJECTS[i], id_of_lector))
        if len(ids) == range_of_ids:
            break
    return fake_list


def numer_of_marks_and_group_in_students(
    my_students: list[tuple[str, int]]
) -> tuple[dict[int:int], dict[int:int]]:
    number_marks_by_student, group_by_student = dict(), dict()
    id_student = 0
    for student_info in my_students:
        id_student += 1
        number_marks_by_student[id_student] = randint(*NUMBER_MARKS)
        group_by_student[id_student] = student_info[1]
    return number_marks_by_student, group_by_student


def generate_marks(
    numer_of_marks: dict[int:int], group_of_student: dict[int:int]
) -> list[tuple[int, date, int, int]]:
    list_of_marks = []
    received_marks = {}
    for id_student in range(1, NUMBER_STUDENTS + 1):
        received_marks[id_student] = 0
    number_of_students_in_group = {}
    for id_student in range(1, NUMBER_STUDENTS + 1):
        number_of_students_in_group[group_of_student[id_student]] = 0
    students_of_group = [[], [], [], []]
    for id_student in range(1, NUMBER_STUDENTS + 1):
        id_group = group_of_student[id_student]
        number_of_students_in_group[id_group] += 1
        students_of_group[id_group].append(id_student)
    for number_of_week in range(7):
        if numer_of_marks == received_marks:
            break
        for number_of_day in range(5):
            date_of_mark = START_DATE + timedelta(number_of_week * 7 + number_of_day)
            for number_of_group in range(1, NUMBER_GROUPS + 1):
                if number_of_students_in_group[number_of_group] == 0:
                    continue
                for number_of_class in range(4):
                    id_subject = randint(1, NUMBER_SUBJECTS)
                    number_of_marks_in_class = randint(
                        0, number_of_students_in_group[number_of_group]
                    )
                    id_students_by_marks_of_class = []
                    for mark in range(number_of_marks_in_class):
                        while True:
                            id_student_by_mark = students_of_group[number_of_group][
                                randint(
                                    0, number_of_students_in_group[number_of_group] - 1
                                )
                            ]
                            if id_student_by_mark not in id_students_by_marks_of_class:
                                id_students_by_marks_of_class.append(id_student_by_mark)
                                break
                        list_of_marks.append(
                            (
                                randint(*MARKS_RANGE),
                                date_of_mark,
                                id_subject,
                                id_student_by_mark,
                            )
                        )
                        received_marks[id_student_by_mark] += 1
                        if (
                            received_marks[id_student_by_mark]
                            == numer_of_marks[id_student_by_mark]
                        ):
                            number_of_students_in_group[number_of_group] -= 1
                            students_of_group[number_of_group].remove(
                                id_student_by_mark
                            )
    return list_of_marks


def fill_table(
    my_connection: Connection,
    table_name: str,
    list_field: list[str],
    table_data: list[tuple],
) -> int:

    list_field_str, question_marks = convert_list_fields(list_field)

    sql = f"INSERT INTO {table_name}({list_field_str}) VALUES({question_marks});"

    print(f"Table {table_name} is created.")
    my_cursor = my_connection.cursor()
    try:
        my_cursor.executemany(sql, table_data)
        my_connection.commit()
    except Error as e:
        print(e)
    finally:
        my_cursor.close()

    return my_cursor.lastrowid


if __name__ == "__main__":
    with connect(NAME_DB) as my_connection:
        fill_table(my_connection, "groups", [NAME], convert_to_tuple(GROUPS))
        fill_table(
            my_connection,
            "lectors",
            [NAME],
            convert_to_tuple(fake_names(NUMBER_LECTORS)),
        )
        my_students = fake_names_ids(NUMBER_STUDENTS, NUMBER_GROUPS)
        fill_table(my_connection, "students", [NAME, "group_id_fn"], my_students)
        my_subjects = subjects_ids(NUMBER_SUBJECTS, NUMBER_LECTORS)
        fill_table(my_connection, "subjects", [NAME, "lector_id_fn"], my_subjects)
        my_marks = generate_marks(*(numer_of_marks_and_group_in_students(my_students)))
        fill_table(
            my_connection,
            "marks",
            ["value", "date_of", "subject_id_fn", "student_id_fn"],
            my_marks,
        )
