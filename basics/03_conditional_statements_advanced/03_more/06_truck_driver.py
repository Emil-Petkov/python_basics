season_of_year = input()
kilometers_for_month = float(input())

truck_driver_salary = 0
total_kilometers = 0

tax = 0.10  # 10% tax

if kilometers_for_month <= 5_000 and season_of_year in ['Spring', 'Autumn', ]:
    truck_driver_salary = kilometers_for_month * 0.75

elif 5_000 < kilometers_for_month <= 10_000 and season_of_year in ['Spring', 'Autumn', ]:
    truck_driver_salary = kilometers_for_month * 0.95

if kilometers_for_month <= 5_000 and season_of_year == 'Summer':
    truck_driver_salary = kilometers_for_month * 0.90

elif 5_000 < kilometers_for_month <= 10_000 and season_of_year == 'Summer':
    truck_driver_salary = kilometers_for_month * 1.10

if kilometers_for_month <= 5_000 and season_of_year == 'Winter':
    truck_driver_salary = kilometers_for_month * 1.05

elif 5_000 < kilometers_for_month <= 10_000 and season_of_year == 'Winter':
    truck_driver_salary = kilometers_for_month * 1.25

if 10_000 < kilometers_for_month <= 20_000:
    truck_driver_salary = kilometers_for_month * 1.45

salary_for_all_season = truck_driver_salary * 4
total_after_tax = salary_for_all_season - (salary_for_all_season * tax)

print(f'{total_after_tax:.2f}')
