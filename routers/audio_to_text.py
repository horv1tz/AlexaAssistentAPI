from fastapi import FastAPI, File, UploadFile
from app import app
from utils.audio_to_text import recognize_speech_from_audio_file
import io

@app.post("/audio_to_text")
async def router(file: UploadFile = File(...)):
    with io.BytesIO() as audio_io:
        audio_io.write(await file.read())
        audio_io.seek(0)

        # Используем нашу функцию для распознавания речи
        text = recognize_speech_from_audio_file(audio_io)

        return {"text": text}
