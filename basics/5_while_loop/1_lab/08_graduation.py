name_student = input()

current_class = 1
sum_of_all_grades = 0
bad_grades = 0

while current_class <= 12:
    current_grade = float(input())
    if current_grade >= 4:
        current_class += 1
        sum_of_all_grades += current_grade
    else:
        bad_grades += 1

    if bad_grades > 1:
        print(f'{name_student} has been excluded at {current_class} grade')
        break

if current_class == 13: #заради ексклузива
    average_grade = sum_of_all_grades / 12  # 12 клас
    print(f'{name_student} graduated. Average grade: {average_grade:.2f}')
