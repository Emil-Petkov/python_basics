def projects_creation(name: str, num_of_projects: int):
    calculate_needed_hours = num_of_projects * 3  # hours for one project

    return f'The architect {name} will need {calculate_needed_hours} hours to complete {num_of_projects} project/s.'


name = input()
num_of_projects = int(input())
result = projects_creation(name, num_of_projects)

print(result)




