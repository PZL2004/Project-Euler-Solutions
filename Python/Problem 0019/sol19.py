"""
How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
"""
import time
from datetime import datetime

start = time.time()

def weekday_first_of_month(start_year, end_year, day):
    day_count = 0
    for i in range(start_year, end_year+1): #inclusive
        for j in range(1, 13): # always 12 months in a year
            if datetime(i,j,1).weekday() == day: # does all the work for me
                day_count += 1
    return day_count

if __name__ == "__main__":
    print(weekday_first_of_month(1901,2000,6)) # Monday - Sunday : 0 - 6
    end = time.time()
    print(f"Computation time: {1000*(end-start)} ms")    