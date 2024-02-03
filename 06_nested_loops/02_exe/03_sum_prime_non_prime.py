command = input()

sum_prime_number = 0
sum_non_prime_number = 0

while not command == 'stop':
    current_number = int(command)
    if current_number < 0:
        print('Number is negative.')

    else:
        is_prime = True

        if current_number > 1:
            for i in range(2, current_number):

                if current_number % i == 0:
                    is_prime = False
                    break
        else:
            is_prime = False

        if is_prime:
            sum_prime_number += current_number

        else:
            sum_non_prime_number += current_number

    command = input()

print(f'Sum of all prime numbers is: {sum_prime_number}')
print(f'Sum of all non prime numbers is: {sum_non_prime_number}')
