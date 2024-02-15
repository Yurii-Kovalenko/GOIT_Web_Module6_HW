
    SELECT AVG(value) as AaverageMarks, students.name as Student, subjects.name as Subject
    FROM marks
    JOIN students ON marks.student_id_fn = students.id
    JOIN subjects ON marks.subject_id_fn = subjects.id
    WHERE subjects.name = 'English'
    GROUP BY student_id_fn
    ORDER BY AaverageMarks DESC
    LIMIT 1
    