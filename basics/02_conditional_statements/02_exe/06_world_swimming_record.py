record_in_seconds = float(input())
distance_in_meters = float(input())
time_for_one_meter_swim = float(input())

needed_time = distance_in_meters * time_for_one_meter_swim

needed_time += (distance_in_meters // 15) * 12.5

if needed_time < record_in_seconds:
    print(f'Yes, he succeeded! The new world record is {needed_time:.2f} seconds.')

else:
    diff = abs(needed_time - record_in_seconds)
    print(f'No, he failed! He was {diff:.2f} seconds slower.')
