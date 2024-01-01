def concatenate_data(f_name: str, l_name: str, age: int, town: str):
    return f'You are {f_name} {l_name}, a {age}-years old person from {town}.'


f_name = input()
l_name = input()
age = int(input())
town = input()
result = concatenate_data(f_name, l_name, age, town)

print(result)
