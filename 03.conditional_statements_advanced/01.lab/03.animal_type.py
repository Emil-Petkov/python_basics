def animal_type(animal: str):
    mammals_list = ['dog', ]
    reptiles_list = ['crocodile', 'tortoise', 'snake', ]

    if animal in mammals_list:
        return 'mammal'

    elif animal in reptiles_list:
        return 'reptile'

    else:
        return 'unknown'


animal = input()
print(animal_type(animal))
