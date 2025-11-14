def generate_profile(age):
    if 0 <= age <= 12:
        return "Child"
    elif 13 <= age <= 19:
        return "Teenager"
    else:
        return "Adult"

user_name = input("Hello! Please, enter your full name:")
birth_year_str = input("Now, please, enter your birth year: ")
birth_year = int(birth_year_str)
current_age = 2025 - birth_year

hobbies = []
while True:
    user_input = input("Enter a favorite hobby or type 'stop' to finish: ")
    if user_input.lower() == 'stop':
        break
    hobbies.append(user_input)

life_stage = generate_profile(current_age)
user_profile = {"name": user_name, "age": current_age, "stage": life_stage, "hobbies": hobbies}

print("\n---\nProfile Summary:")
print(f"Name: {user_profile["name"]}")
print(f"Age: {user_profile["age"]}")
print(f"Life Stage: {user_profile["stage"]}")
if not hobbies:
    print("You didn't mention any hobbies.")
else:
    print(f"Favorite Hobbies ({len(hobbies)})")
    for hobby in hobbies:
        print(f"- {hobby}")
print("---")