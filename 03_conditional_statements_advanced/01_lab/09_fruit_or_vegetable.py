def fruit_or_vegetable(product: str):
    fruits = ['banana', 'apple', 'kiwi', 'cherry', 'lemon', 'grapes', ]
    vegetables = ['tomato', 'cucumber', 'pepper', 'carrot', ]

    if product in fruits:
        return 'fruit'

    elif product in vegetables:
        return 'vegetable'

    else:
        return 'unknown'


current_product = input()
print(fruit_or_vegetable(current_product))
