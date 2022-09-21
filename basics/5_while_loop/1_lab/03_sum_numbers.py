target_number = int(input())

counter = 0

while counter < target_number:
    current_number = int(input()) #всяко следващо число което се прочита
    counter += current_number

print(counter)
