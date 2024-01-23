n_open_tabs = int(input())
salary = int(input())

sites = {
    'Facebook': 150,
    'Instagram': 100,
    'Reddit': 50,
}

for site in range(n_open_tabs):
    current_site = input()

    if current_site in sites:
        salary -= sites[current_site]

    if salary <= 0:
        print('You have lost your salary.')
        break

else:
    print(salary)
