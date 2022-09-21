count_groups = int(input())

musala_count = 0
montblanc_count = 0
kilimanjaro_count = 0
k2_count = 0

everest_count = 0
total_count_people = 0

for i in range(1, count_groups + 1):
    count_people = int(input())
    total_count_people += count_people

    if count_people <= 5:
        musala_count += count_people
    elif count_people <= 12:
        montblanc_count += count_people
    elif count_people <= 25:
        kilimanjaro_count += count_people
    elif count_people <= 40:
        k2_count += count_people
    else:
        everest_count += count_people

musala_percent = musala_count / total_count_people * 100
print(f"{musala_percent:.2f}%")

montblanc_percent = montblanc_count / total_count_people * 100
print(f"{montblanc_percent:.2f}%")

kilimanjaro_percent = kilimanjaro_count / total_count_people * 100
print(f"{kilimanjaro_percent:.2f}%")

k2_percent = k2_count / total_count_people * 100
print(f"{k2_percent:.2f}%")

everest_percent = everest_count / total_count_people * 100
print(f"{everest_percent:.2f}%")
