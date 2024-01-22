def fruit_or_vegetable(user_input: str):
    fruits = ['banana', 'apple', 'kiwi', 'cherry', 'lemon', 'grapes', ]
    vegetables = ['tomato', 'cucumber', 'pepper', 'carrot', ]

    if user_input in fruits:
        return 'fruit'

    elif user_input in vegetables:
        return 'vegetable'

    else:
        return 'unknown'


user_input = input()
print(fruit_or_vegetable(user_input))
