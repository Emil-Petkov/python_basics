def deposit_calculator(deposit: float, months: int, year_interest: float):
    interest_for_month = (deposit * (year_interest / 100)) / 12
    total = deposit + (months * interest_for_month)

    return total


deposit = float(input())
months = int(input())
year_interest = float(input())

print(deposit_calculator(deposit, months, year_interest))
