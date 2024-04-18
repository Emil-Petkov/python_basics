def personal_titles(age: float, gender: str):
    if gender == 'm':
        if age < 16:
            return 'Master'

        else:
            return 'Mr.'

    elif gender == 'f':
        if age < 16:
            return 'Miss'

        else:
            return 'Ms.'


age = float(input())
gender = input()
print(personal_titles(age, gender))
