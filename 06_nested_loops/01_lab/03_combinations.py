














number = int(input())

counter = 0

for f in range(number + 1):
    for s in range(number + 1):
        for t in range(number + 1):
            if f + s + t == number:
                counter += 1

print(counter)
