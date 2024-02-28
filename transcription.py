import openai

def transcribe_audio(audio_file_path, openai):
    with open(audio_file_path, 'rb') as audio_file:
    #    transcription = openai.Audio.transcribe("whisper-1", audio_file)
    #return transcription['text']
        transcript = openai.audio.transcriptions.create(
            model="whisper-1", 
            file=audio_file
        )
    return transcript
