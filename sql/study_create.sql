-- Table: groups
DROP TABLE IF EXISTS groups;
CREATE TABLE groups (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(100) UNIQUE NOT NULL
);

-- Table: students
DROP TABLE IF EXISTS students;
CREATE TABLE students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(100) UNIQUE NOT NULL,
    group_id_fn INTEGER,
    FOREIGN KEY (group_id_fn) REFERENCES groups (id)
      ON DELETE CASCADE
      ON UPDATE CASCADE
);

-- Table: lectors
DROP TABLE IF EXISTS lectors;
CREATE TABLE lectors (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(100) UNIQUE NOT NULL
);

-- Table: subjects
DROP TABLE IF EXISTS subjects;
CREATE TABLE subjects (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(100) UNIQUE NOT NULL,
    lector_id_fn INTEGER,
    FOREIGN KEY (lector_id_fn) REFERENCES lectors (id)
      ON DELETE CASCADE
      ON UPDATE CASCADE
);

-- Table: marks
DROP TABLE IF EXISTS marks;
CREATE TABLE marks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    value INTEGER NOT NULL,
    date_of DATE NOT NULL,
    subject_id_fn INTEGER,
    student_id_fn INTEGER,
    FOREIGN KEY (subject_id_fn) REFERENCES subjects (id)
      ON DELETE CASCADE
      ON UPDATE CASCADE,
    FOREIGN KEY (student_id_fn) REFERENCES students (id)
      ON DELETE CASCADE
      ON UPDATE CASCADE
);
