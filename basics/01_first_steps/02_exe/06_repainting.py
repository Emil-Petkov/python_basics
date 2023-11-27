needed_nylon_in_qm2 = int(input())
needed_paint_in_liters = int(input())
needed_paint_thinner = int(input())
needed_hours = int(input())

price_per_q2m_nylon = 1.5
price_per_one_pack_paint = 14.5
price_per_one_liter_paint_thinner = 5

garbage_bags = 0.4

sum_for_materials = (((needed_nylon_in_qm2 * price_per_q2m_nylon + (2 * price_per_q2m_nylon)) +
                      (needed_paint_in_liters * 1.10) * price_per_one_pack_paint) + (
                             needed_paint_thinner * price_per_one_liter_paint_thinner) + garbage_bags)

sum_for_master_per_hour = sum_for_materials * 0.30

total_sum = sum_for_materials + (sum_for_master_per_hour * needed_hours)

print(total_sum)
