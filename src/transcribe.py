import numpy as np
import whisper


def transcribe_to_text(model_arg, audio_path):
    print('Загружаем модель Whisper: ')
    model = whisper.load_model(model_arg)
    print("Модель загружена делаем транскрибацию: ")
    return model.transcribe(audio=audio_path, fp16=False)

