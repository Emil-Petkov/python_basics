deposit = float(input())
term_of_the_deposit = int(input())
year_interest_percentage = float(input())

interest_per_month = (deposit * year_interest_percentage / 12) / 100

total_sum = deposit + (interest_per_month * term_of_the_deposit)

print(total_sum)
