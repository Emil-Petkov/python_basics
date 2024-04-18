def number_100_to_200(number: int):
    # match number:
    #     case number if number < 100:
    #         return 'Less than 100'
    #
    #     case number if number >= 100 and number <= 200:
    #         return 'Between 100 and 200'
    #
    #     case number if number > 200:
    #         return 'Greater than 200'
    #

    if number < 100:
        return 'Less than 100'

    elif number <= 200:
        return 'Between 100 and 200'

    elif number > 200:
        return 'Greater than 200'


current_number = int(input())
print(number_100_to_200(current_number))
