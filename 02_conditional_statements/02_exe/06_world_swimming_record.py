def world_swimming_record(record: float, distance: float, time_for_one_meter: float):
    time_per_all_distance = distance * time_for_one_meter
    delay = distance // 15  # every 15 meters have delay by 12.5 seconds

    total_time_in_seconds = time_per_all_distance + (delay * 12.5)

    if total_time_in_seconds < record:
        return f'Yes, he succeeded! The new world record is {total_time_in_seconds:.2f} seconds.'

    diff = abs(total_time_in_seconds - record)
    return f'No, he failed! He was {diff:.2f} seconds slower.'


record_in_seconds = float(input())
distance_in_meters = float(input())
time_for_swim_one_meter = float(input())

print(world_swimming_record(record_in_seconds, distance_in_meters, time_for_swim_one_meter))
