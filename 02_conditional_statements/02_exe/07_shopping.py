def shopping(budget, n_video_cards, n_video_processors, n_rams):
    total = 0

    price_per_video_cards = n_video_cards * 250
    price_processor = n_video_processors * (price_per_video_cards * 0.35)
    price_ram = n_rams * (price_per_video_cards * 0.10)

    total = price_per_video_cards + price_processor + price_ram

    if n_video_cards > n_video_processors:
        total -= total * 0.15  # discount

    diff = abs(budget - total)
    if budget >= total:
        return f'You have {diff:.2f} leva left!'

    else:
        return f'Not enough money! You need {diff:.2f} leva more!'


budget = float(input())
n_video_cards = int(input())
n_video_processors = int(input())
n_rams = int(input())
print(shopping(budget, n_video_cards, n_video_processors, n_rams))
