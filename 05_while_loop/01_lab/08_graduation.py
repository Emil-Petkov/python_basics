name = input()
excluded = 2
average_grade = []
current_class = 1

while current_class <= 12:
    grade = float(input())

    if grade >= 4.00:
        average_grade.append(grade)
        current_class += 1
    else:
        excluded -= 1
        if excluded == 0:
            print(f'{name} has been excluded at {current_class} grade')
            break

if excluded > 0 and average_grade:
    average = sum(average_grade) / len(average_grade)
    print(f'{name} graduated. Average grade: {average:.2f}')
