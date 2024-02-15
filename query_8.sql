
    SELECT AVG(value) as AaverageMarks, subjects.name as Subject, lectors.name as Lector
    FROM marks
    JOIN subjects ON marks.subject_id_fn = subjects.id 
    JOIN lectors ON subjects.lector_id_fn = lectors.id
    WHERE lectors.name = 'John Lopez'
    GROUP BY subjects.id
    ORDER BY subjects.name
    