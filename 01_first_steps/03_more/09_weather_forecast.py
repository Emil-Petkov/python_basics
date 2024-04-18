def weather(current_weather: str):
    if current_weather == 'sunny':
        return 'It\'s warm outside!'

    else:
        return 'It\'s cold outside!'


current_weather = input()
print(weather(current_weather))
