students = []

while(True):
    print("\n--- Student Grade Analyzer ---")
    print("1. Add a new student")
    print("2. Add a grade for a student")
    print("3. Show report(all students)")
    print("4. Find top performer")
    print("5. Exit")
    try:
        choice = input("Enter your choice: ")
        choice_int = int(choice)

        if(choice_int == 1):
            name = input("Enter student name: ").strip()
            if any(student["name"] == name for student in students):
                print("A student with that name already exists.")
            else:
                new_student = {"name": name, "grades": []}
                students.append(new_student)
                print(students)
        elif(choice_int == 2):
            name = input("Enter student name: ").strip()
            found_student = None
            for student in students:
                if student["name"] == name:
                    found_student = student
                    break
            if found_student:
                while(True):
                    grade = input("Enter a grade (or 'done' to finish): ").strip()
                    if(grade.lower() == "done"):
                        break
                    try:
                        grade_int = int(grade)
                        if(0 <= grade_int <= 100):
                            found_student["grades"].append(grade_int)
                        else:
                            print("Invalid Input: the grade must be from 0 to 100.")
                    except ValueError:
                        print("Invalid Input. Please enter a number.")
                        continue
            else:
                print("There is no student with that name.")
        elif(choice_int == 3):
            print("3")
        elif(choice_int == 4):
            print("4")
        elif(choice_int == 5):
            print("Exiting program.")
            break
        elif(choice_int < 1 or choice_int > 5):
            print("Error: please enter number between 1-5.")
    except ValueError:
        print("Error: incorrect choice. Please enter a number.")