import time


def countdown(time_in_sec):
    while time_in_sec > -1:
        mins, secs = divmod(time_in_sec, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print('\r', timeformat, sep='', end='')
        time.sleep(1)
        time_in_sec -= 1
    
    print("\rstop")


time_in_sec = int(input("Time (in seconds): "))

countdown(time_in_sec)
