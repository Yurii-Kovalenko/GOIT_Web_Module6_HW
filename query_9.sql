
    SELECT DISTINCT students.name as Student, subjects.name as Subject 
    FROM subjects
    JOIN marks ON marks.subject_id_fn = subjects.id
    JOIN students ON marks.student_id_fn = students.id
    WHERE students.name = 'Randall Pearson'
    ORDER BY subjects.name
    