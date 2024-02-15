
    SELECT students.name as Student, groups.name as Group_Name
    FROM students
    JOIN groups ON students.group_id_fn = groups.id
    WHERE groups.name = 'IT-25'
    ORDER BY students.name
    