num = int(input())

for n in range(num + 1):
    if n == 0 or n % 2 == 0:
        print(2 ** n)
