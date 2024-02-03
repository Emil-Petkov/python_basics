











total_tickets = 0
student_tickets = 0
standard_tickets = 0
kid_tickets = 0

while True:
    movie_name = input()
    if movie_name == "Finish":
        break

    free_seats = int(input())
    tickets_for_movie = 0

    for _ in range(free_seats):
        ticket_type = input()
        if ticket_type == "End":
            break

        tickets_for_movie += 1
        if ticket_type == "student":
            student_tickets += 1
        elif ticket_type == "standard":
            standard_tickets += 1
        elif ticket_type == "kid":
            kid_tickets += 1

    total_tickets += tickets_for_movie
    occupancy = (tickets_for_movie / free_seats) * 100
    print(f"{movie_name} - {occupancy:.2f}% full.")

print(f"Total tickets: {total_tickets}")
print(f"{(student_tickets / total_tickets) * 100:.2f}% student tickets.")
print(f"{(standard_tickets / total_tickets) * 100:.2f}% standard tickets.")
print(f"{(kid_tickets / total_tickets) * 100:.2f}% kids tickets.")
