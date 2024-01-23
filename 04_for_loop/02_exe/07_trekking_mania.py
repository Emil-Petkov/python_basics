n_group = int(input())

peaks = {
    'Мусала': [],
    'Монблан': [],
    'Килиманджаро': [],
    'К2': [],
    'Еверест': [],
}

total_peoples = 0

for _ in range(n_group):
    current_group = int(input())
    total_peoples += current_group

    if current_group <= 5:
        peaks['Мусала'].append(current_group)

    elif current_group <= 12:
        peaks['Монблан'].append(current_group)

    elif current_group <= 25:
        peaks['Килиманджаро'].append(current_group)

    elif current_group <= 40:
        peaks['К2'].append(current_group)

    else:
        peaks['Еверест'].append(current_group)

print(f"{(sum(peaks['Мусала']) / total_peoples) * 100:.2f}%")
print(f"{(sum(peaks['Монблан']) / total_peoples) * 100:.2f}%")
print(f"{(sum(peaks['Килиманджаро']) / total_peoples) * 100:.2f}%")
print(f"{(sum(peaks['К2']) / total_peoples) * 100:.2f}%")
print(f"{(sum(peaks['Еверест']) / total_peoples) * 100:.2f}%")
