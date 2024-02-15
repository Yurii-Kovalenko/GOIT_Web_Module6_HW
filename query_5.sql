
    SELECT subjects.name as Subject, lectors.name as Lector
    FROM subjects
    JOIN lectors ON subjects.lector_id_fn = lectors.id
    WHERE lectors.name = 'Chelsea Bishop'
    ORDER BY subjects.name
    