# Import the youtube transcription module
from youtube_transcript_api import YouTubeTranscriptApi

# Defines a function to get the transcript
def get_transcript(video_id):
   # Use the YouTubeTranscriptApi to get the transcript of the video
   # The transcript is returned as a list of dictionaries, where each dictionary
   # represents a piece of the transcript
    transcript = YouTubeTranscriptApi.get_transcript(video_id)
    return transcript

# Defines a function to write the transcript to a file
def write_transcript_to_file(video_id, transcript):
    # Open a text file with the same name as the video_id
    # The 'w' argument means that the file will be opened for writing

    with open(f'{video_id}.txt', 'w') as file:
        # Iterate over each entry in the transcript
        for entry in transcript:
            # Write the text of the entry to the file, followed by a newline character
            # The 'text' key of each entry contains the actual text of the transcript
            file.write(entry['text'] + '\n')

# Set the ID of the video you want to get the transcript for
video_id = 'u8vDZZa-88Y'

# Get the transcript of the video

transcript = get_transcript(video_id)

# Write the transcript to a file

write_transcript_to_file(video_id, transcript)
