import requests
from dotenv import load_dotenv
import os
from datetime import datetime, timezone

def obtain_api_key():
    load_dotenv()

def fetch_and_time_format_convertion(youtube_video_id):
    
    obtain_api_key()

    response = requests.get(f"https://youtube.googleapis.com/youtube/v3/videos?part=liveStreamingDetails&id={youtube_video_id}&key={os.getenv('api_key')}").json()
    live_start_time_before_convert = response['items'][0]['liveStreamingDetails']['actualStartTime']

    
    new_live_start_time = datetime.strptime(live_start_time_before_convert, '%Y-%m-%dT%H:%M:%SZ').replace(tzinfo=timezone.utc).timestamp()
    return new_live_start_time