
    SELECT AVG(value) as AaverageMarks, students.name as Student, lectors.name as Lector
    FROM marks
    JOIN subjects ON marks.subject_id_fn = subjects.id
    JOIN lectors ON subjects.lector_id_fn = lectors.id
    JOIN students ON marks.student_id_fn = students.id
    WHERE students.name = 'Randall Pearson' and lectors.name = 'John Lopez'
    