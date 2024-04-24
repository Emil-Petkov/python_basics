




n_open_tabs = int(input())
salary = int(input())

fines = {
    'Facebook': 150,
    'Instagram': 100,
    'Reddit': 50,
}

for tab in range(n_open_tabs):
    current_tab = input()

    if current_tab in fines:
        salary -= fines[current_tab]

    if salary <= 0:
        print('You have lost your salary.')
        exit()

print(salary)
