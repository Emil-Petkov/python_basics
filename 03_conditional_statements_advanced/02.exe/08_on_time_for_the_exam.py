def on_time_for_the_exam(hour_exam: int, minute_exam: int, hour_arrival: int, minute_arrival: int):
    time_exam_in_minutes = hour_exam * 60 + minute_exam
    time_arrival_in_minutes = hour_arrival * 60 + minute_arrival

    time_difference = time_arrival_in_minutes - time_exam_in_minutes

    if time_difference < -30:
        status = 'Early'
    elif time_difference <= 0:
        status = 'On time'
    else:
        status = 'Late'

    hours = abs(time_difference) // 60
    minutes = abs(time_difference) % 60
    if hours > 0:
        time_str = f'{hours}:{minutes:02d} hours'
    else:
        time_str = f'{minutes} minutes'

    if time_difference != 0:
        if time_difference > 0:
            time_str += ' after the start'
        else:
            time_str += ' before the start'
        return f'{status}\n{time_str}'
    else:
        return status


hour_exam = int(input())
minute_exam = int(input())
hour_arrival = int(input())
minute_arrival = int(input())
print(on_time_for_the_exam(hour_exam, minute_exam, hour_arrival, minute_arrival))
