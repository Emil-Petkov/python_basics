budget = float(input())
video_cards = int(input())
processors = int(input())
ram_memory = int(input())

video_cards_price = video_cards * 250
processors_price = processors * (video_cards_price * 0.35)
ram_memory_price = (video_cards_price * 0.10) * ram_memory

total = video_cards_price + processors_price + ram_memory_price

if video_cards > processors:
    total -= total * 0.15

diff = abs(total - budget)

if budget >= total:
    print(f'You have {diff:.2f} leva left!')

else:
    print(f'Not enough money! You need {diff:.2f} leva more!')
