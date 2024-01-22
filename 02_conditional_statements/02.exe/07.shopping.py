def shopping(budget: float, n_video_cards: int, n_cpu: int, n_ram: int):
    # price
    video_card = 250
    total_price_for_video_cards = video_card * n_video_cards
    cpu_price = total_price_for_video_cards * 0.35
    ram_price = total_price_for_video_cards * 0.10

    total = total_price_for_video_cards + (n_cpu * cpu_price) + (n_ram * ram_price)

    if n_video_cards > n_cpu:
        total -= total * 0.15

    diff = abs(budget - total)
    if budget >= total:
        return f'You have {diff:.2f} leva left!'

    return f'Not enough money! You need {diff:.2f} leva more!'


budget = float(input())
n_video_cards = int(input())
n_cpu = int(input())
n_ram = int(input())

print(shopping(budget, n_video_cards, n_cpu, n_ram))
