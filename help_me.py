from datetime import datetime
import sys
import os
import argparse
import time 


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_fucked_level(h):
    if h < 12:
        return 'You\'re good'
    elif h < 18:
        return 'You\'re fine, I guess'
    elif h < 24:
        return 'You should go to sleep'
    else:
        return 'You\'re fucked, Fix your fucking sleeping schedule !!!!'


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("Year", help="start year",type=int)
    parser.add_argument("Month", help="start month",type=int)
    parser.add_argument("Day", help="start day",type=int)
    parser.add_argument("Hour", help="start hour", type=int)
    args = parser.parse_args()

    d0 = datetime(args.Year, args.Month, args.Day, args.Hour)
    cls()

    while True:
        d1 = datetime.now()
        delta = d1 - d0

        hours, remainder = divmod(delta.total_seconds(), 3600)
        minutes, seconds = divmod(remainder, 60)

        print("You did not sleep in : {:02}h {:02}m {:02}s => {}".format(
            int(hours), 
            int(minutes), 
            int(seconds), 
            get_fucked_level(hours)), end='\r')

        time.sleep(1)
