import numpy as np
import whisper
from tqdm import tqdm
import librosa

def transcribe_to_text(model_arg, audio_path, chunk_size=30):
    """
    Транскрибирует аудиофайл, используя tqdm для отображения прогресс-бара.

    Args:
        audio_path: Путь к аудиофайлу.
        model_name: Название модели Whisper (tiny, base, small, medium, large).
        chunk_size: Размер чанка (в секундах).

    Returns:
        Полный текст транскрипции.
    """
    model = whisper.load_model(model_arg)

    y, sr = librosa.load(audio_path)
    duration = librosa.get_duration(y=y, sr=sr)
    num_chunks = int(np.ceil(duration / chunk_size))

    full_text = ""
    with tqdm(total=num_chunks, desc="Транскрипция", unit="чанк") as pbar:
        for i in range(num_chunks):
            start_time = i * chunk_size
            end_time = min((i + 1) * chunk_size, duration)

            chunk_start_sample = int(start_time * sr)
            chunk_end_sample = int(end_time * sr)
            audio_chunk = y[chunk_start_sample:chunk_end_sample]

            result = model.transcribe(
                audio_chunk.astype(np.float32), fp16=False, language="ru"
            )
            full_text += result["text"]

            pbar.update(1)  # Обновляем прогресс-бар
    return full_text
