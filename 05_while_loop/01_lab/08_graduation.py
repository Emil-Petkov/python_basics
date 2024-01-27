name = input()
grade = float(input())
excluded = 2
average_grade = []
current_class = 1

while current_class <= 12:
    current_grade = grade

    if current_grade >= 4.00:
        average_grade.append(current_grade)
    else:
        excluded -= 1

        if excluded == 0:
            current_class -= 1
            print(f'{name} has been excluded at {current_class} grade')
            break

    current_class += 1

    if current_class <= 12:
        grade_input = input()
        if grade_input:
            grade = float(grade_input)
        else:
            break
if excluded > 0:
    print(f'{name} graduated. Average grade: {sum(average_grade) / len(average_grade):.2f}')
