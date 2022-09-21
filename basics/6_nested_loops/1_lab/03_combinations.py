entrance_number = int(input())

counter_combination = 0

for x1 in range(entrance_number + 1):  # 0 до entrance_number
    for x2 in range(entrance_number + 1):
        for x3 in range(entrance_number + 1):
            if x1 + x2 + x3 == entrance_number: # колко пъти сбора е равен на входното число
                counter_combination += 1

print(counter_combination)

