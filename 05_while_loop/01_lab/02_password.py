user = input()
password = input()

data = input()

while not password == data:
    data = input()

print(f'Welcome {user}!')
