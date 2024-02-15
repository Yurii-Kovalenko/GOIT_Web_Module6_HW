
    SELECT AVG(value) as AaverageMarks, groups.name as Group_Name, subjects.name as Subject
    FROM marks
    JOIN students ON marks.student_id_fn = students.id
    JOIN subjects ON marks.subject_id_fn = subjects.id
    JOIN groups ON students.group_id_fn = groups.id
    WHERE subjects.name = 'Ukrainian'
    GROUP BY groups.id
    ORDER BY groups.name
    