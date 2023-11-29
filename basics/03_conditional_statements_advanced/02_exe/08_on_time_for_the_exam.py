hour_of_exam = int(input())
minutes_of_exam = int(input())
arrive_hour = int(input())
arrive_minute = int(input())

time_exam_in_minutes = (hour_of_exam * 60) + minutes_of_exam
time_arrive_in_minutes = (arrive_hour * 60) + arrive_minute

diff = abs(time_exam_in_minutes - time_arrive_in_minutes)

if time_arrive_in_minutes > time_exam_in_minutes:
    print('Late')

    if diff < 60:
        print(f"{diff} minutes after the start")

    else:
        hours = diff // 60
        minutes = diff % 60

        if minutes < 10:
            print(f"{hours}:0{minutes} hours after the start")

        else:
            print(f"{hours}:{minutes} hours after the start")

elif time_arrive_in_minutes == time_exam_in_minutes or diff <= 30:
    print("On Time")

    if 1 <= diff <= 30:
        print(f"{diff} minutes before the start")

else:
    print("Early")

    if diff < 60:
        print(f"{diff} minutes before the start")

    else:
        hour = diff // 60
        minutes = diff % 60

        if minutes < 10:
            print(f"{hour}:0{minutes} hours before the start")

        else:
            print(f"{hour}:{minutes} hours before the start")
