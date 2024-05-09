n_people_jury = int(input())

total_grades = 0
presentations_count = 0

while True:
    presentation_name = input()

    if presentation_name == 'Finish':
        break

    presentation_total_grade = 0

    for _ in range(n_people_jury):
        grade = float(input())
        presentation_total_grade += grade

    average_grade = presentation_total_grade / n_people_jury
    print(f"{presentation_name} - {average_grade:.2f}.")

    total_grades += average_grade
    presentations_count += 1

final_average = total_grades / presentations_count
print(f"Student's final assessment is {final_average:.2f}.")
