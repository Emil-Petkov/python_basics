def projects_creation(architect_name: str, n_projects: int):
    calculate_needed_hours = n_projects * 3  # hours

    return f'The architect {architect_name} will need {calculate_needed_hours} hours to complete {n_projects} project/s.'


name = input()
projects = int(input())
print(projects_creation(name, projects))
