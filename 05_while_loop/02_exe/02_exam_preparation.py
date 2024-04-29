bad_grade_limit = int(input())
counter_bad_grades = 0
counter_problems = 0
total_score = 0
last_problem = ""

while True:
    task_name = input()

    if task_name == 'Enough':
        break

    current_grade = int(input())

    if current_grade <= 4:
        counter_bad_grades += 1

    if counter_bad_grades == bad_grade_limit:
        print(f"You need a break, {counter_bad_grades} poor grades.")
        break

    total_score += current_grade
    counter_problems += 1
    last_problem = task_name

if task_name == 'Enough':
    if counter_problems > 0:
        average_score = total_score / counter_problems

    else:
        average_score = 0

    print(f"Average score: {average_score:.2f}")
    print(f"Number of problems: {counter_problems}")
    print(f"Last problem: {last_problem}")
