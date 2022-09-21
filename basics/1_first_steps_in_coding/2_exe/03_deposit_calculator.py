deposit = float(input())
months = int(input())
year_interest = float(input())

interest_per_all_period = deposit * year_interest / 100
interest_per_month = interest_per_all_period / 12

total = deposit + months * interest_per_month

print(total)
