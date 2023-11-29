budget = float(input())
type_ticket = input()
peoples = int(input())

vip_ticket = 499.99
normal_ticket = 249.99

ticket_cost = 0
transport_cost = 0

if type_ticket == 'VIP':
    ticket_cost += peoples * vip_ticket

elif type_ticket == 'Normal':
    ticket_cost += peoples * normal_ticket

if 1 <= peoples <= 4:
    transport_cost = budget * 0.75

elif 5 <= peoples <= 9:
    transport_cost = budget * 0.60

elif 10 <= peoples <= 24:
    transport_cost = budget * 0.50

elif 25 <= peoples <= 49:
    transport_cost = budget * 0.40

elif peoples >= 50:
    transport_cost = budget * 0.25

total_transport_cost = budget - transport_cost

if ticket_cost <= total_transport_cost:
    print(f'Yes! You have {abs(total_transport_cost - ticket_cost):.2f} leva left.')

else:
    print(f'Not enough money! You need {abs(total_transport_cost - ticket_cost):.2f} leva.')
