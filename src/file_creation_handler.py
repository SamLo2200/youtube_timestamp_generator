from dotenv import load_dotenv
import os

load_dotenv()

def file_creator(hours, remainingMinutes, seconds, song_name):
        with open(os.getenv('file_name'), "a") as file:
            outputString = f"{hours}:{remainingMinutes}:{seconds} {song_name}"
            file.write(f"{outputString}\n")

