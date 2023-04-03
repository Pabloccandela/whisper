import os
import openai

openai.organization = "org-5BYtUCyiQegfqc44wjzi2pzo"
openai.api_key = "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"
openai.Model.list()

# Definir la ruta del archivo Whisper
file = open(os.path.join(os.path.dirname(__file__),"audio.mp3"), "rb")
transcription = openai.Audio.transcribe("whisper-1", file)

print(transcription)