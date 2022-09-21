budget = float(input())
count_video_cards = float(input())
count_processors = float(input())
count_rams = float(input())

price_video_cards = count_video_cards * 250
price_processor = (price_video_cards * 0.35) * count_processors
price_ram = (price_video_cards * 0.10) * count_rams

total = price_video_cards + price_processor + price_ram

if count_video_cards > count_processors:
    total = total - (total * 0.15)

difference = abs(budget - total)

if budget >= total:
    print(f'You have {difference:.2f} leva left!')
else:
    print(f'Not enough money! You need {difference:.2f} leva more!')
