





n_lines = int(input())

p1 = []
p2 = []
p3 = []
p4 = []
p5 = []

length_of_n_lines = 0

for n in range(n_lines):
    current_number = int(input())

    length_of_n_lines += 1

    if current_number < 200:
        p1.append(current_number)

    elif 200 <= current_number <= 399:
        p2.append(current_number)

    elif 400 <= current_number <= 599:
        p3.append(current_number)

    elif 600 <= current_number <= 799:
        p4.append(current_number)

    elif current_number >= 800:
        p5.append(current_number)

calculate_p1 = (len(p1) / length_of_n_lines) * 100
calculate_p2 = (len(p2) / length_of_n_lines) * 100
calculate_p3 = (len(p3) / length_of_n_lines) * 100
calculate_p4 = (len(p4) / length_of_n_lines) * 100
calculate_p5 = (len(p5) / length_of_n_lines) * 100

print(f'{calculate_p1:.2f}%')
print(f'{calculate_p2:.2f}%')
print(f'{calculate_p3:.2f}%')
print(f'{calculate_p4:.2f}%')
print(f'{calculate_p5:.2f}%')
