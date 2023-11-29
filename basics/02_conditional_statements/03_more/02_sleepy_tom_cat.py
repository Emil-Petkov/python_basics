res_days = int(input())

year = 365

work_day = year - res_days

total_play_time = (res_days * 127) + (work_day * 63)

diff = abs(total_play_time - 30000)

hours = diff // 60
minutes = diff % 60

if total_play_time > 30000:  # minutes play time per year
    print('Tom will run away')
    print(f'{hours} hours and {minutes} minutes more for play')

else:
    print('Tom sleeps well')
    print(f'{hours} hours and {minutes} minutes less for play')
