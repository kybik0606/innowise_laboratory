import sqlite3
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(current_dir, 'school.db')

conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Вставляем студентов и сразу получаем их ID
students_data = [
    ('Alice Johnson', 2005),
    ('Brian Smith', 2004),
    ('Carla Reyes', 2006),
    ('Dantal Kim', 2005),
    ('Eva Thompson', 2003),
    ('Felix Nuyvert', 2007),
    ('Grace Patel', 2005),
    ('Henry Lopez', 2004),
    ('Isabella Martinez', 2006)
]

# Создаем словарь для хранения ID студентов
student_ids = {}

for full_name, birth_year in students_data:
    cursor.execute('INSERT INTO students (full_name, birth_year) VALUES (?, ?)', (full_name, birth_year))
    # Получаем ID только что вставленного студента
    student_id = cursor.lastrowid
    student_ids[full_name] = student_id

# Вставляем оценки используя правильные ID
grades_data = [
    (student_ids['Alice Johnson'], 'Math', 88),
    (student_ids['Alice Johnson'], 'English', 92),
    (student_ids['Alice Johnson'], 'Science', 85),
    (student_ids['Brian Smith'], 'Math', 75),
    (student_ids['Brian Smith'], 'History', 83),
    (student_ids['Brian Smith'], 'English', 79),
    (student_ids['Carla Reyes'], 'Science', 95),
    (student_ids['Carla Reyes'], 'Math', 91),
    (student_ids['Carla Reyes'], 'Art', 89),
    (student_ids['Dantal Kim'], 'Math', 84),
    (student_ids['Dantal Kim'], 'Science', 88),
    (student_ids['Dantal Kim'], 'Physical Education', 93),
    (student_ids['Eva Thompson'], 'English', 90),
    (student_ids['Eva Thompson'], 'History', 85),
    (student_ids['Eva Thompson'], 'Math', 88),
    (student_ids['Felix Nuyvert'], 'Science', 72),
    (student_ids['Felix Nuyvert'], 'Math', 78),
    (student_ids['Felix Nuyvert'], 'English', 81),
    (student_ids['Grace Patel'], 'Art', 94),
    (student_ids['Grace Patel'], 'Science', 87),
    (student_ids['Grace Patel'], 'Math', 90),
    (student_ids['Henry Lopez'], 'History', 77),
    (student_ids['Henry Lopez'], 'Math', 83),
    (student_ids['Henry Lopez'], 'Science', 80),
    (student_ids['Isabella Martinez'], 'English', 99),
    (student_ids['Isabella Martinez'], 'Math', 89),
    (student_ids['Isabella Martinez'], 'Art', 92)
]

cursor.executemany('INSERT INTO grades (student_id, subject, grade) VALUES (?, ?, ?)', grades_data)

conn.commit()
conn.close()