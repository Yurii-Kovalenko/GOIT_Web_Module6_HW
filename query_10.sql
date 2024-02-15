
    SELECT DISTINCT students.name as Student, subjects.name as Subject, lectors.name as Lector
    FROM subjects
    JOIN marks ON marks.subject_id_fn = subjects.id
    JOIN lectors ON subjects.lector_id_fn = lectors.id
    JOIN students ON marks.student_id_fn = students.id
    WHERE students.name = 'Randall Pearson' and lectors.name = 'John Lopez'
    ORDER BY subjects.name
    