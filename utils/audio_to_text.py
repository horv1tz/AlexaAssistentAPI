import speech_recognition as sr
import os

def recognize_speech_from_audio_file(audio_file):
    # Инициализация распознавателя
    recognizer = sr.Recognizer()

    # Используем аудиофайл в качестве источника
    with sr.AudioFile(audio_file) as source:
        # Запись данных из файла в объект AudioData
        audio_data = recognizer.record(source)

        try:
            # Распознавание речи с помощью Google Web Speech API
            text = recognizer.recognize_google(audio_data, language='ru-RU')
            return text
        except sr.UnknownValueError:
            return "Распознавание не удалось: речь не распознана."
        except sr.RequestError as e:
            return f"Ошибка запроса к Google Speech Recognition; {e}"
        
# with open("demo/audio.wav", "rb") as audio_file:
#     print(recognize_speech_from_audio_file(audio_file))