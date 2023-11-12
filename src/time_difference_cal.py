from datetime import datetime, timezone
import math

def time_difference_cal(start_time):
    current_time = datetime.now(timezone.utc).timestamp
    
    #live_start_time = datetime.strptime(live_start_time_before_convert, "%Y-%m-%dT%H:%M:%SZ")

    ##print(f"{live_start_time.date()} {live_start_time.hour}:{live_start_time.minute}:{live_start_time.second}")
    ##print(float(live_start_time))
    
    return (float(current_time()) - float(start_time))/60
    




