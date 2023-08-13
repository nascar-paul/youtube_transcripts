
markdown
Copy code
# YouTube Transcript Extractor

This repository contains a Python script that can generate a text file containing the transcript of any YouTube video. It uses the `youtube_transcript_api` to fetch the transcripts.

## Prerequisites

- Python 3.x
- `youtube_transcript_api` library

## Installation

1. Clone this repository:
git clone https://github.com/nascar-paul/youtube_transcripts.git


2. Navigate to the cloned directory:
cd youtube_transcripts


### Setting Up a Virtual Environment (Highly Suggested)

Using a virtual environment is not mandatory, but it is highly recommended to avoid potential conflicts with other Python packages you may have installed.

1. Install `virtualenv` if you haven't:
pip install virtualenv


2. Create a virtual environment. While "Youtube" is a suggested name for the virtual environment, you can choose any name you prefer:
virtualenv Youtube


3. Activate the virtual environment:

- On Windows:
  ```
  .\Youtube\Scripts\activate
  ```

- On macOS and Linux:
  ```
  source Youtube/bin/activate
  ```

### Installing the Required Library

1. Install the `youtube_transcript_api` library:
pip install youtube_transcript_api


## Usage

1. Run the script:
python youtube_transcript.py

2. When prompted, enter the YouTube video ID for which you want to fetch the transcript.

3. The script will generate a text file containing the transcript of the video.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)
