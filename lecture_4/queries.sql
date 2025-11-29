-- 1. Create tables
-- Table 1: students
CREATE TABLE IF NOT EXISTS students
(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    full_name TEXT NOT NULL,
    birth_year INTEGER NOT NULL
);

-- Table 2: grades
CREATE TABLE IF NOT EXISTS grades
(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id INTEGER NOT NULL,
    subject TEXT NOT NULL,
    grade INTEGER NOT NULL,
    FOREIGN KEY (student_id) REFERENCES students(id)
);

-- 2. Insert data
-- Insert students
INSERT INTO students (full_name, birth_year) VALUES
('Alice Johnson', 2005),
('Brian Smith', 2004),
('Carla Reyes', 2006),
('Dantal Kim', 2005),
('Eva Thompson', 2003),
('Felix Nuyvert', 2007),
('Grace Patel', 2005),
('Henry Lopez', 2004),
('Isabella Martinez', 2006);

-- Insert grades using actual student IDs
INSERT INTO grades (student_id, subject, grade) VALUES
((SELECT id FROM students WHERE full_name = 'Alice Johnson'), 'Math', 88),
((SELECT id FROM students WHERE full_name = 'Alice Johnson'), 'English', 92),
((SELECT id FROM students WHERE full_name = 'Alice Johnson'), 'Science', 85),
((SELECT id FROM students WHERE full_name = 'Brian Smith'), 'Math', 75),
((SELECT id FROM students WHERE full_name = 'Brian Smith'), 'History', 83),
((SELECT id FROM students WHERE full_name = 'Brian Smith'), 'English', 79),
((SELECT id FROM students WHERE full_name = 'Carla Reyes'), 'Science', 95),
((SELECT id FROM students WHERE full_name = 'Carla Reyes'), 'Math', 91),
((SELECT id FROM students WHERE full_name = 'Carla Reyes'), 'Art', 89),
((SELECT id FROM students WHERE full_name = 'Dantal Kim'), 'Math', 84),
((SELECT id FROM students WHERE full_name = 'Dantal Kim'), 'Science', 88),
((SELECT id FROM students WHERE full_name = 'Dantal Kim'), 'Physical Education', 93),
((SELECT id FROM students WHERE full_name = 'Eva Thompson'), 'English', 90),
((SELECT id FROM students WHERE full_name = 'Eva Thompson'), 'History', 85),
((SELECT id FROM students WHERE full_name = 'Eva Thompson'), 'Math', 88),
((SELECT id FROM students WHERE full_name = 'Felix Nuyvert'), 'Science', 72),
((SELECT id FROM students WHERE full_name = 'Felix Nuyvert'), 'Math', 78),
((SELECT id FROM students WHERE full_name = 'Felix Nuyvert'), 'English', 81),
((SELECT id FROM students WHERE full_name = 'Grace Patel'), 'Art', 94),
((SELECT id FROM students WHERE full_name = 'Grace Patel'), 'Science', 87),
((SELECT id FROM students WHERE full_name = 'Grace Patel'), 'Math', 90),
((SELECT id FROM students WHERE full_name = 'Henry Lopez'), 'History', 77),
((SELECT id FROM students WHERE full_name = 'Henry Lopez'), 'Math', 83),
((SELECT id FROM students WHERE full_name = 'Henry Lopez'), 'Science', 80),
((SELECT id FROM students WHERE full_name = 'Isabella Martinez'), 'English', 99),
((SELECT id FROM students WHERE full_name = 'Isabella Martinez'), 'Math', 89),
((SELECT id FROM students WHERE full_name = 'Isabella Martinez'), 'Art', 92);

-- 3. Find all grades for a specific student (Alice Johnson)
SELECT s.full_name, g.subject, g.grade
FROM students s
JOIN grades g ON s.id = g.student_id
WHERE s.full_name = 'Alice Johnson';

-- 4. Calculate the average grade per student
SELECT s.full_name, AVG(g.grade) as average_grade
FROM students s
JOIN grades g ON s.id = g.student_id
GROUP BY s.id, s.full_name;

-- 5. List all students born after 2004
SELECT id, full_name, birth_year
FROM students
WHERE birth_year > 2004;

-- 6. Create a query that lists all subjects and their average grades
SELECT subject, AVG(grade) as average_grade
FROM grades
GROUP BY subject;

-- 7. Find the top 3 students with the highest average grades
SELECT s.full_name, AVG(g.grade) as average_grade
FROM students s
JOIN grades g ON s.id = g.student_id
GROUP BY s.id, s.full_name
ORDER BY average_grade DESC
LIMIT 3;

-- 8. Show all students who have scored below 80 in any subject
SELECT DISTINCT s.full_name, g.subject, g.grade
FROM students s
JOIN grades g ON s.id = g.student_id
WHERE g.grade < 80;

-- Indexes for optimization
CREATE INDEX idx_students_birth_year ON students(birth_year);
CREATE INDEX idx_grades_student_id ON grades(student_id);
CREATE INDEX idx_grades_subject ON grades(subject);
CREATE INDEX idx_grades_grade ON grades(grade);