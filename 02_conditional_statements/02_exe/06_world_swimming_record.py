def swimming_record(record_in_seconds: float, distance_in_meters: float, time_swimming_one_meter: float):
    time_per_all_distance = distance_in_meters * time_swimming_one_meter
    delay = (distance_in_meters // 15) * 12.5  # seconds

    totaltime_in_seconds = time_per_all_distance + delay

    diff = abs(record_in_seconds - totaltime_in_seconds)

    if totaltime_in_seconds < record_in_seconds:
        return f'Yes, he succeeded! The new world record is {totaltime_in_seconds:.2f} seconds.'

    else:
        return f'No, he failed! He was {diff:.2f} seconds slower.'


record_in_seconds = float(input())
distance_in_meters = float(input())
time_swimming_one_meter = float(input())
print(swimming_record(record_in_seconds, distance_in_meters, time_swimming_one_meter))
