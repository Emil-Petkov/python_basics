def invalid_number(num: int):
    if not 100 <= num <= 200 and not num == 0:
        print('invalid')


number = int(input())
invalid_number(number)
