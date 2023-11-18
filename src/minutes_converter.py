import math 

def minutes_converter(minutes):

        #10 seconds delay
        minutes = minutes - 0.166667

        hours = math.floor(minutes / 60)
        remainingMinutes = math.floor(minutes % 60)
        seconds = math.floor((minutes * 60) % 60)
        #seconds = 20

        remainingMinutes = str(remainingMinutes).zfill(2)
        seconds = str(seconds).zfill(2)
        
        return hours, remainingMinutes, seconds
        




