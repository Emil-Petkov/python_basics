def concatenate_data(f_name: str, l_name: str, age: int, town: str):
    return f'You are {f_name} {l_name}, a {age}-years old person from {town}.'


first_name = input()
last_name = input()
age = int(input())
town = input()
print(concatenate_data(first_name, last_name, age, town))
