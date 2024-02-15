SELECT AVG(value) as AaverageMarks, students.name as Name, students.id
FROM marks
JOIN students ON marks.student_id_fn = students.id
GROUP BY student_id_fn
ORDER BY AaverageMarks DESC
LIMIT 5

