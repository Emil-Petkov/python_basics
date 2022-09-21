current_record = float(input())
distance_in_meters = float(input())
time_per_seconds_for_one_meter_swimming = float(input())

time_per_all_distance_in_seconds = distance_in_meters * time_per_seconds_for_one_meter_swimming

delay = (distance_in_meters // 15) * 12.5

total_time = time_per_all_distance_in_seconds + delay

difference = abs(total_time - current_record)

if total_time < current_record:
    print(f'Yes, he succeeded! The new world record is {total_time:.2f} seconds.')
else:
    print(f'No, he failed! He was {difference:.2f} seconds slower.')
