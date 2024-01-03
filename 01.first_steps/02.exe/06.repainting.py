def repainting(nylon: int, paint: int, thinner: int, hours: int):
    price_for_nylon_square_meter = 1.50
    price_for_paint = 14.50
    price_for_thinner_liters = 5.00

    extra_nylon = nylon + 2  # add 2 square meters nylon
    extra_paint = paint * 1.10  # add 10% more paint
    garbage_bags = 0.40

    money_for_materials = ((price_for_nylon_square_meter * extra_nylon) + (price_for_paint * extra_paint) +
                           (price_for_thinner_liters * thinner) + garbage_bags)

    price_per_master = (money_for_materials * 0.30) * hours

    total = money_for_materials + price_per_master

    return total


nylon_square_meters = int(input())
needed_paint = int(input())
paint_thinner_in_liters = int(input())
work_hours = int(input())

result = repainting(nylon_square_meters, needed_paint, paint_thinner_in_liters, work_hours)

print(result)
