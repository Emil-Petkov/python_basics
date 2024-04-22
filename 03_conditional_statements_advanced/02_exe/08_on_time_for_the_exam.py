def on_time_for_the_exam(hour_exam, minute_exam, hour_arrival, minute_arrival):
    exam_time_in_minutes = hour_exam * 60 + minute_exam
    arrival_time_in_minutes = hour_arrival * 60 + minute_arrival

    time_difference = arrival_time_in_minutes - exam_time_in_minutes

    if time_difference < -30:
        status = "Early"
    elif time_difference <= 0:
        status = "On time"
    else:
        status = "Late"

    print(status)

    if time_difference != 0:
        hours = abs(time_difference) // 60
        minutes = abs(time_difference) % 60
        if hours > 0:
            print(f"{hours}:{minutes:02d} hours {'before' if time_difference < 0 else 'after'} the start")
        else:
            print(f"{minutes} minutes {'before' if time_difference < 0 else 'after'} the start")


hour_exam = int(input())
minute_exam = int(input())
hour_arrival = int(input())
minute_arrival = int(input())

on_time_for_the_exam(hour_exam, minute_exam, hour_arrival, minute_arrival)
