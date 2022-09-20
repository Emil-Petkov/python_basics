nylon = int(input())
paint = int(input())
thinner = int(input())
hours = int(input())

nylon_price = nylon * 1.50 + 3
pain_price = (paint * 14.50) * 1.10
thinner_price = thinner * 5.00
bags = 0.40

sum_per_materials = nylon_price + pain_price + thinner_price + bags

sum_per_hour = sum_per_materials * 0.30

master_salary = hours * sum_per_hour

total = sum_per_materials + master_salary

print(f'{total}')
