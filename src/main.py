import youtube_api
from time_difference_cal import * 
from minutes_converter import * 
from file_creation_handler import * 


def init():
    user_input_video_id = str(input("Enter the video id: "))
    
    while len(user_input_video_id) <= 1: 
        user_input_video_id = str(input("Enter the video id: "))
    else:
        global live_start_time 
        live_start_time = youtube_api.fetch_and_time_format_convertion(user_input_video_id)
            
init()

while len(str(live_start_time)) != 0:
    enter_listener = input("Press enter to mark")
        
    if enter_listener == "":
        
        time_difference_in_minutes = time_difference_cal(live_start_time)
        timestamp = minutes_converter(time_difference_in_minutes)
        #print(timestamp)

        
        user_timestamp_confirmation = input(f"Confirm: {timestamp[0]}:{timestamp[1]}:{timestamp[2]}? (y/n) ")

        while user_timestamp_confirmation == "" or user_timestamp_confirmation == "n": 
            break
        else: 
            user_input_song_name = str(input("Enter the song name: "))
            file_creator(timestamp[0], timestamp[1], timestamp[2], user_input_song_name)
            continue