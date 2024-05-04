import os
import string
from youtube_transcript_api import YouTubeTranscriptApi
from pytube import YouTube
import json

# Assuming openai_assistant.py is in the same directory
from openai_assistant import get_api_key, initialize_openai_client, interact_with_custom_assistant

def get_transcript(video_id):
    """
    Retrieves the transcript of a YouTube video given its ID.
    :param video_id: The YouTube video ID.
    :return: The video transcript as a list of dictionaries.
    """
    transcript = YouTubeTranscriptApi.get_transcript(video_id)
    return transcript

def write_transcript_to_file(video_id, transcript, output_format):
    """
    Writes the YouTube video transcript to a file in the specified format.
    :param video_id: The YouTube video ID.
    :param transcript: The transcript data.
    :param output_format: The format to write the transcript ('text', 'json', or 'both').
    """
    video = YouTube(f'https://www.youtube.com/watch?v={video_id}')
    video_title = video.title
    valid_chars = "-_.() %s%s" % (string.ascii_letters, string.digits)
    video_title_clean = ''.join(c for c in video_title if c in valid_chars)

    # Create filename base without extension
    filename_base = f'{video_title_clean}'

    if output_format == 'json' or output_format == 'both':
        json_filename = f'{filename_base}.json'
        with open(json_filename, 'w') as json_file:
            json.dump(transcript, json_file, indent=4)

    if output_format == 'text' or output_format == 'both':
        text_filename = f'{filename_base}.txt'
        with open(text_filename, 'w') as file:
            for entry in transcript:
                file.write(entry['text'] + '\n')

video_id = input("Enter the YouTube video ID: ")
output_format = input("Enter the output format (text, json or both): ").lower()

if output_format not in ['text', 'json', 'both']:
    print("Invalid output format selected. Defaulting to text.")
    output_format = 'text'

transcript = get_transcript(video_id)
write_transcript_to_file(video_id, transcript, output_format)

engage_option = input("Would you like to forward this transcript to the assistant for summarization and analysis? (yes/no): ").lower()
if engage_option == 'yes':
    api_key = get_api_key()  # Prompt the user for the API key
    initialize_openai_client(api_key)  # Initialize the OpenAI client with the API key

    combined_transcript = ' '.join([entry['text'] for entry in transcript])
    response = interact_with_custom_assistant(combined_transcript)
    if response:
        print("Assistant Response:\n", response)
    else:
        print("Failed to get a response from the custom assistant.")

