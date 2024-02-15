
    SELECT students.name as Student, marks.value as Mark, marks.date_of as Date, subjects.name as Subject, groups.name as Group_Name 
    FROM marks
    JOIN students ON marks.student_id_fn = students.id
    JOIN subjects ON marks.subject_id_fn = subjects.id
    JOIN groups ON students.group_id_fn = groups.id
    WHERE groups.name = 'IT-25' AND subjects.name = 'Math' AND marks.date_of = (SELECT MAX(marks.date_of) 
    FROM marks
    JOIN students ON marks.student_id_fn = students.id
    JOIN subjects ON marks.subject_id_fn = subjects.id
    JOIN groups ON students.group_id_fn = groups.id
    WHERE groups.name = 'IT-25' AND subjects.name = 'Math')
    ORDER BY students.name
    