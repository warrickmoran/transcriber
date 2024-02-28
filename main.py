import os
import openai
from dotenv import load_dotenv

from sentiment_analysis import *
from transcription import *
from save_as_docx import *

import logging

logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.DEBUG)

load_dotenv()

openai.api_key = os.getenv('OPENAI_API_KEY')

def meeting_minutes(transcription):
    abstract_summary = abstract_summary_extraction(transcription)
    key_points = key_points_extraction(transcription)
    action_items = action_item_extraction(transcription)
    sentiment = sentiment_analysis(transcription)
    return {
        'abstract_summary': abstract_summary,
        'key_points': key_points,
        'action_items': action_items,
        'sentiment': sentiment
    }

audio_file_path = "./audio/audio.ogg"

try:
    api_key = os.environ['OPENAI_API_KEY']
    logging.info("OpenAI API KEY: %s", api_key)
except KeyError:
    print('OpenAI API Key Not Found')
    # Prompt for the API key
    #api_key = input("Enter your OpenAI API key: ")

    # Set the environment variable
    #os.environ["OPENAI_API_KEY"] = api_key

logging.info("Transcribing Audio File: %s", audio_file_path)
transcription = transcribe_audio(audio_file_path, openai)
logging.info("Transcription Completed")
logging.debug("Transcription Results: %s", transcription)
minutes = meeting_minutes(transcription)
print(minutes)

save_as_docx(minutes, 'meeting_minutes.docx')
