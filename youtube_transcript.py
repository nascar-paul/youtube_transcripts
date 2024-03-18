# Imports the string module, which contains a number of useful string constants and functions
import string

# Import the youtube transcription module
from youtube_transcript_api import YouTubeTranscriptApi
import os
# Import pytube to fetch the video title
from pytube import YouTube

# Defines a function to get the transcript
def get_transcript(video_id):
   # Use the YouTubeTranscriptApi to get the transcript of the video
   # The transcript is returned as a list of dictionaries, where each dictionary
   # represents a piece of the transcript
    transcript = YouTubeTranscriptApi.get_transcript(video_id)
    return transcript

# Defines a function to write the transcript to a file
def write_transcript_to_file(video_id, transcript):
    # Use pytube to get the video object, which includes the title
    video = YouTube(f'https://www.youtube.com/watch?v={video_id}')
    video_title = video.title
    
    # Remove any invalid characters from the video title
    valid_chars = "-_.() %s%s" % (string.ascii_letters, string.digits)
    video_title_clean = ''.join(c for c in video_title if c in valid_chars)
    
    # Use a sanitized version of the video title for the filename
    filename = f'{video_title_clean}.txt'
    
    # Write the transcript to the file named after the video title
    with open(filename, 'w') as file:
        for entry in transcript:
            file.write(entry['text'] + '\n')

# Set the ID of the video you want to get the transcript for
video_id = input("Enter the YouTube video ID: ")

# Get the transcript of the video
transcript = get_transcript(video_id)

# Write the transcript to a file
write_transcript_to_file(video_id, transcript)