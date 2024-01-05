def trade_commissions(town: str, sales: float):
    trade_commission = 0

    commissions = {
        'Sofia': [(500, 0.05), (1_000, 0.07), (10_000, 0.08), (float('inf'), 0.12)],
        'Varna': [(500, 0.045), (1_000, 0.075), (10_000, 0.10), (float('inf'), 0.13)],
        'Plovdiv': [(500, 0.055), (1_000, 0.08), (10_000, 0.12), (float('inf'), 0.145)],

    }

    if sales < 0 or town not in commissions:
        return 'error'

    for value, percentage in commissions[town]:
        if sales <= value:
            return f'{sales * percentage:.2f}'

    return 'error'


town = input()
sales_volume = float(input())

print(trade_commissions(town, sales_volume))
