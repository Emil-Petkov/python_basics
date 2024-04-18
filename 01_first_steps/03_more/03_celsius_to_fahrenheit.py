def convert_celsius_to_fahrenheit(celsius):
    convert = (celsius * 1.8) + 32

    return f'{convert:.2f}'


current_celsius = float(input())
print(convert_celsius_to_fahrenheit(current_celsius))
