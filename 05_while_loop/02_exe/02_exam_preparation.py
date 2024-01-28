poor_grades_limit = int(input())
count_poor_grades = 0
sum_grades = 0
count_problems = 0
last_problem = ""

while True:
    task_name = input()
    if task_name == "Enough":
        break

    current_grade = int(input())
    sum_grades += current_grade
    count_problems += 1
    last_problem = task_name

    if current_grade <= 4:
        count_poor_grades += 1
        if count_poor_grades == poor_grades_limit:
            print(f"You need a break, {count_poor_grades} poor grades.")
            break

if count_poor_grades < poor_grades_limit:
    average_grade = sum_grades / count_problems if count_problems > 0 else 0
    print(f"Average score: {average_grade:.2f}")
    print(f"Number of problems: {count_problems}")
    print(f"Last problem: {last_problem}")
