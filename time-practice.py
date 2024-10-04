import keyboard
import time


start_timer = input('start timer? Y/N\n')


if start_timer.lower() == 'y':
    time_local_1 = 0
    print('hold N to break the loop')
    while start_timer != 'n':
        if keyboard.is_pressed('n'):
            break
        else:
            time_local = time.localtime() # WHO NEEDS ASYNCIO WHEN WE GOTS THE MATH
            time_thing = time.strftime('%H:%M:%S', time_local)
            if time_local == time_local_1:
                continue
            time_m = time_s / 60 # there is 100% a better way to do this but I love it so damn much
            left_time_s = time_s % 60
            print(f'{time_m:.0f}:{left_time_s}')
            time_s += 1
            time_local_1 = time_local
    print(f'Total time: {time_m:.0f} minutes and {left_time_s} seconds.')
elif start_timer.lower() == 'n':
    print('Okie doke!')
else:
    print('Y or N ONLY')
