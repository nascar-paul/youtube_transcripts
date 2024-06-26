# Imports the string module, which contains a number of useful string constants and functions
import string

# Import the youtube transcription module
from youtube_transcript_api import YouTubeTranscriptApi
import os
# Import pytube to fetch the video title
from pytube import YouTube

# Import json module for serialization
import json  

# Defines a function to get the transcript
def get_transcript(video_id):
   # Use the YouTubeTranscriptApi to get the transcript of the video
   # The transcript is returned as a list of dictionaries, where each dictionary
   # represents a piece of the transcript
    transcript = YouTubeTranscriptApi.get_transcript(video_id)
    return transcript

# Defines a function to write the transcript to a file
def write_transcript_to_file(video_id, transcript, output_format):
    # Use pytube to get the video object, which includes the title
    video = YouTube(f'https://www.youtube.com/watch?v={video_id}')
    video_title = video.title
    
    # Remove any invalid characters from the video title
    valid_chars = "-_.() %s%s" % (string.ascii_letters, string.digits)
    video_title_clean = ''.join(c for c in video_title if c in valid_chars)
    
    # Determine the filename and format based on user choice
    if output_format == 'json':
        filename = f'{video_title_clean}.json'
        with open(filename, 'w') as json_file:
            json.dump(transcript, json_file, indent=4)  # Serialize and write as JSON
    else:  # Default to text output
        filename = f'{video_title_clean}.txt'
        with open(filename, 'w') as file:
            for entry in transcript:
                file.write(entry['text'] + '\n')

video_id = input("Enter the YouTube video ID: ")
output_format = input("Enter the output format (text or json): ").lower()

# Validate the output format
if output_format not in ['text', 'json']:
    print("Invalid output format selected. Defaulting to text.")
    output_format = 'text'

# Get the transcript of the video
transcript = get_transcript(video_id)

# Write the transcript to a file in the selected format
write_transcript_to_file(video_id, transcript, output_format)  # Fixed function call