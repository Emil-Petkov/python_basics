def deposit_calculator(deposit: float, months: int, interest_rate: float):
    total_interest = deposit * (interest_rate / 100)
    interest_per_one_month = total_interest / 12  # months

    total = deposit + (months * interest_per_one_month)

    return total


deposit = float(input())
n_months = int(input())
annual_interest_rate = float(input())
print(deposit_calculator(deposit, n_months, annual_interest_rate))
