def animal_type(type_animal: str):
    mammal = ['dog', ]
    reptile = ['crocodile', 'tortoise', 'snake', ]

    if type_animal in mammal:
        return 'mammal'

    elif type_animal in reptile:
        return 'reptile'

    else:
        return 'unknown'


animal = input()
print(animal_type(animal))
