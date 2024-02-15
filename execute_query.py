from sqlite3 import connect

from create_db import NAME_DB

from create_db import READY_REQUESTS

from auxiliary_functions import input_in_range

from auxiliary_functions import choice_of_subject

from auxiliary_functions import choice_of_lector

from auxiliary_functions import choice_of_group

from auxiliary_functions import choice_of_student


def sql_query_2() -> None:
    subject_name = choice_of_subject()[1]
    result = f"""
    SELECT AVG(value) as AaverageMarks, students.name as Student, subjects.name as Subject
    FROM marks
    JOIN students ON marks.student_id_fn = students.id
    JOIN subjects ON marks.subject_id_fn = subjects.id
    WHERE subjects.name = '{subject_name}'
    GROUP BY student_id_fn
    ORDER BY AaverageMarks DESC
    LIMIT 1
    """
    with open(f"query_2.sql", "w") as fw:
        fw.write(result)


def sql_query_3() -> None:
    subject_name = choice_of_subject()[1]
    result = f"""
    SELECT AVG(value) as AaverageMarks, groups.name as Group_Name, subjects.name as Subject
    FROM marks
    JOIN students ON marks.student_id_fn = students.id
    JOIN subjects ON marks.subject_id_fn = subjects.id
    JOIN groups ON students.group_id_fn = groups.id
    WHERE subjects.name = '{subject_name}'
    GROUP BY groups.id
    ORDER BY groups.name
    """
    with open(f"query_3.sql", "w") as fw:
        fw.write(result)


def sql_query_5() -> None:
    lector_name = choice_of_lector()[1]
    result = f"""
    SELECT subjects.name as Subject, lectors.name as Lector
    FROM subjects
    JOIN lectors ON subjects.lector_id_fn = lectors.id
    WHERE lectors.name = '{lector_name}'
    ORDER BY subjects.name
    """
    with open(f"query_5.sql", "w") as fw:
        fw.write(result)


def sql_query_6() -> None:
    group_name = choice_of_group()[1]
    result = f"""
    SELECT students.name as Student, groups.name as Group_Name
    FROM students
    JOIN groups ON students.group_id_fn = groups.id
    WHERE groups.name = '{group_name}'
    ORDER BY students.name
    """
    with open(f"query_6.sql", "w") as fw:
        fw.write(result)


def sql_query_7() -> None:
    group_name = choice_of_group()[1]
    subject_name = choice_of_subject()[1]
    result = f"""
    SELECT students.name as Student, marks.value as Mark, marks.date_of as Date, subjects.name as Subject, groups.name as Group_Name 
    FROM marks
    JOIN students ON marks.student_id_fn = students.id
    JOIN subjects ON marks.subject_id_fn = subjects.id
    JOIN groups ON students.group_id_fn = groups.id
    WHERE groups.name = '{group_name}' AND subjects.name = '{subject_name}'
    ORDER BY students.name
    """
    with open(f"query_7.sql", "w") as fw:
        fw.write(result)


def sql_query_8() -> None:
    lector_name = choice_of_lector()[1]
    result = f"""
    SELECT AVG(value) as AaverageMarks, subjects.name as Subject, lectors.name as Lector
    FROM marks
    JOIN subjects ON marks.subject_id_fn = subjects.id 
    JOIN lectors ON subjects.lector_id_fn = lectors.id
    WHERE lectors.name = '{lector_name}'
    GROUP BY subjects.id
    ORDER BY subjects.name
    """
    with open(f"query_8.sql", "w") as fw:
        fw.write(result)


def sql_query_9() -> None:
    student_name = choice_of_student()[1]
    result = f"""
    SELECT DISTINCT students.name as Student, subjects.name as Subject 
    FROM subjects
    JOIN marks ON marks.subject_id_fn = subjects.id
    JOIN students ON marks.student_id_fn = students.id
    WHERE students.name = '{student_name}'
    ORDER BY subjects.name
    """
    with open(f"query_9.sql", "w") as fw:
        fw.write(result)


def sql_query_10() -> None:
    student_name = choice_of_student()[1]
    lector_name = choice_of_lector()[1]
    result = f"""
    SELECT DISTINCT students.name as Student, subjects.name as Subject, lectors.name as Lector
    FROM subjects
    JOIN marks ON marks.subject_id_fn = subjects.id
    JOIN lectors ON subjects.lector_id_fn = lectors.id
    JOIN students ON marks.student_id_fn = students.id
    WHERE students.name = '{student_name}' and lectors.name = '{lector_name}'
    ORDER BY subjects.name
    """
    with open(f"query_10.sql", "w") as fw:
        fw.write(result)


def sql_query_11() -> None:
    student_name = choice_of_student()[1]
    lector_name = choice_of_lector()[1]
    result = f"""
    SELECT AVG(value) as AaverageMarks, students.name as Student, lectors.name as Lector
    FROM marks
    JOIN subjects ON marks.subject_id_fn = subjects.id
    JOIN lectors ON subjects.lector_id_fn = lectors.id
    JOIN students ON marks.student_id_fn = students.id
    WHERE students.name = '{student_name}' and lectors.name = '{lector_name}'
    """
    with open(f"query_11.sql", "w") as fw:
        fw.write(result)


def sql_query_12() -> None:
    group_name = choice_of_group()[1]
    subject_name = choice_of_subject()[1]
    result = f"""
    SELECT students.name as Student, marks.value as Mark, marks.date_of as Date, subjects.name as Subject, groups.name as Group_Name 
    FROM marks
    JOIN students ON marks.student_id_fn = students.id
    JOIN subjects ON marks.subject_id_fn = subjects.id
    JOIN groups ON students.group_id_fn = groups.id
    WHERE groups.name = '{group_name}' AND subjects.name = '{subject_name}' AND marks.date_of = (SELECT MAX(marks.date_of) 
    FROM marks
    JOIN students ON marks.student_id_fn = students.id
    JOIN subjects ON marks.subject_id_fn = subjects.id
    JOIN groups ON students.group_id_fn = groups.id
    WHERE groups.name = '{group_name}' AND subjects.name = '{subject_name}')
    ORDER BY students.name
    """
    with open(f"query_12.sql", "w") as fw:
        fw.write(result)


def execute_query(id_query: int) -> list[tuple]:
    if id_query not in READY_REQUESTS:
        exec(f"sql_query_{id_query}()")
    with open(f"query_{id_query}.sql", "r") as fr:
        sql = fr.read()

    with connect(NAME_DB) as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()


if __name__ == "__main__":
    request_number = input_in_range("Enter the request number", 1, 12)
    print(execute_query(request_number))
