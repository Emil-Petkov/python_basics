text = input()

sum_of_points = 0

for later in text:
    if later == 'a':
        sum_of_points += 1
    elif later == 'e':
        sum_of_points += 2
    elif later == 'i':
        sum_of_points += 3
    elif later == 'o':
        sum_of_points += 4
    elif later == 'u':
        sum_of_points += 5

print(sum_of_points)