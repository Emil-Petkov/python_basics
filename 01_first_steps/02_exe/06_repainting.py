def repainting(meters_nylon: int, liters_paint: int, liters_thinner: int, hours):
    price_nylon_per_meter = 1.50
    price_paint_per_liter = 14.50
    price_thinner_per_liter = 5.00

    extra_paint = liters_paint * 0.10
    extra_nylon = 2  # meters
    garbage_bags = 0.40

    cost_materials = ((((meters_nylon + extra_nylon) * price_nylon_per_meter) +
                       ((liters_paint + extra_paint) * price_paint_per_liter)) +
                      (liters_thinner * price_thinner_per_liter) + garbage_bags)

    money_for_the_master = (cost_materials * 0.30) * hours

    total = cost_materials + money_for_the_master

    return total


n_meters_nylon = int(input())
n_liters_paint = int(input())
n_liters_paint_thinner = int(input())
n_hours = int(input())
print(repainting(n_meters_nylon, n_liters_paint, n_liters_paint_thinner, n_hours))
