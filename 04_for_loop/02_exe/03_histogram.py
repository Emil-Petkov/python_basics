n_numbers = int(input())

mapper = {
    'p1': [],
    'p2': [],
    'p3': [],
    'p4': [],
    'p5': [],
}

for num in range(n_numbers):
    concurrent_number = int(input())

    if concurrent_number < 200:
        mapper['p1'].append(concurrent_number)

    elif 200 <= concurrent_number <= 399:
        mapper['p2'].append(concurrent_number)

    elif 400 <= concurrent_number <= 599:
        mapper['p3'].append(concurrent_number)

    elif 600 <= concurrent_number <= 799:
        mapper['p4'].append(concurrent_number)

    else:
        mapper['p5'].append(concurrent_number)

print(f"{(len(mapper['p1']) / n_numbers) * 100:.2f}%")
print(f"{(len(mapper['p2']) / n_numbers) * 100:.2f}%")
print(f"{(len(mapper['p3']) / n_numbers) * 100:.2f}%")
print(f"{(len(mapper['p4']) / n_numbers) * 100:.2f}%")
print(f"{(len(mapper['p5']) / n_numbers) * 100:.2f}%")
