n_lines = int(input())
p1 = []
p2 = []
p3 = []
p4 = []
p5 = []

for _ in range(n_lines):
    current_number = int(input())

    if current_number < 200:
        p1.append(current_number)

    elif current_number <= 399:
        p2.append(current_number)

    elif current_number <= 599:
        p3.append(current_number)

    elif current_number <= 799:
        p4.append(current_number)

    else:
        p5.append(current_number)

print(
    f'{(len(p1) / n_lines) * 100:.2f}%\n'
    f'{(len(p2) / n_lines) * 100:.2f}%\n'
    f'{(len(p3) / n_lines) * 100:.2f}%\n'
    f'{(len(p4) / n_lines) * 100:.2f}%\n'
    f'{(len(p5) / n_lines) * 100:.2f}%\n')
