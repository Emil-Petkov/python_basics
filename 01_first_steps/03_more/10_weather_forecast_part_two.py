def weather(degrees: float):
    match degrees:
        case degrees if 5.0 <= degrees <= 14.9:
            return 'Cold'

        case degrees if 15.0 <= degrees <= 20.0:
            return 'Mild'

        case degrees if 20.1 <= degrees <= 25.9:
            return 'Warm'

        case degrees if 26.00 <= degrees <= 35.0:
            return 'Hot'

        case _:
            return 'unknown'


degrees_outside = float(input())
print(weather(degrees_outside))

################################################################

temperature = float(input())

if 5 <= temperature <= 11.9:
    print('Cold')

elif 12 <= temperature <= 14.9:
    print('Cool')

elif 15 <= temperature <= 20:
    print('Mild')

elif 20.1 <= temperature <= 25.9:
    print('Warm')

elif 26 <= temperature <= 35:
    print('Hot')

else:
    print('unknown')
