import os
import argparse
import whisper
import time
from tqdm import tqdm
from pydub import AudioSegment

# Установите стабильную версию googletrans
# pip install googletrans==4.0.0-rc1
from googletrans import Translator


def extract_audio(video_path, audio_output="temp_audio.wav"):
    """Извлекает аудио из видео с помощью pydub"""
    print(f"Извлечение аудио из {video_path}...")
    try:
        # Загружаем видеофайл
        video = AudioSegment.from_file(video_path)

        # Конвертируем в нужный формат
        audio = video.set_frame_rate(16000).set_channels(1)

        # Экспортируем в WAV
        audio.export(audio_output, format="wav")

        return audio_output
    except Exception as e:
        print(f"Ошибка при извлечении аудио: {e}")
        return None


def transcribe_and_translate(audio_path, model, source_lang="en", target_lang="ru"):
    """Транскрибирует аудио и переводит текст"""
    print("Начата транскрипция... (это может занять некоторое время)")

    # Запускаем транскрипцию
    result = model.transcribe(
        audio_path,
        language=source_lang,
        task="transcribe",
        verbose=True,  # Включаем встроенный прогресс-бар Whisper
    )

    print(f"✅ Транскрипция завершена! Длина текста: {len(result['text'])} символов")

    # Перевод текста
    print("Начат перевод...")
    translator = Translator()
    try:
        # Разбиваем текст на части, если он слишком длинный
        max_chunk_size = 5000
        text = result["text"]
        chunks = [
            text[i : i + max_chunk_size] for i in range(0, len(text), max_chunk_size)
        ]

        translated_text = ""
        for chunk in tqdm(chunks, desc="Перевод текста"):
            # СИНХРОННЫЙ перевод с использованием стабильной версии
            translation = translator.translate(chunk, src=source_lang, dest=target_lang)
            translated_text += translation.text + " "

        return translated_text.strip()
    except Exception as e:
        print(f"Ошибка перевода: {e}")
        return text


def save_to_file(text, filename):
    """Сохраняет текст в файл"""
    with open(filename, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"Результат сохранен в {filename}")


def main():
    # Настройка парсера аргументов
    parser = argparse.ArgumentParser(
        description="Перевод видео с английского на русский"
    )
    parser.add_argument("video_path", help="Путь к видеофайлу")
    parser.add_argument(
        "-m",
        "--model",
        default="base",
        choices=["tiny", "base", "small", "medium", "large"],
        help="Модель Whisper (по умолчанию: base)",
    )
    parser.add_argument(
        "-o",
        "--output",
        default="translation.txt",
        help="Имя выходного файла (по умолчанию: translation.txt)",
    )
    parser.add_argument(
        "-s", "--source-lang", default="en", help="Исходный язык (по умолчанию: en)"
    )
    parser.add_argument(
        "-t", "--target-lang", default="ru", help="Целевой язык (по умолчанию: ru)"
    )

    args = parser.parse_args()

    # Проверка существования видеофайла
    if not os.path.exists(args.video_path):
        print(f"❌ Ошибка: файл {args.video_path} не найден!")
        return

    print(f"Загрузка модели Whisper ({args.model})...")
    start_time = time.time()
    model = whisper.load_model(args.model)
    print(f"Модель загружена за {time.time() - start_time:.1f} секунд")

    # Извлечение аудио
    audio_file = extract_audio(args.video_path)
    if audio_file is None or not os.path.exists(audio_file):
        print("❌ Не удалось извлечь аудио.")
        return

    # Получаем размер файла для информации
    file_size = os.path.getsize(audio_file) / (1024 * 1024)
    print(f"Аудио извлечено успешно ({file_size:.1f} MB): {audio_file}")

    # Транскрипция и перевод
    translated_text = transcribe_and_translate(
        audio_file, model, source_lang=args.source_lang, target_lang=args.target_lang
    )

    # Сохранение результата
    save_to_file(translated_text, args.output)

    # Удаляем временный аудиофайл
    try:
        os.remove(audio_file)
        print(f"Временный файл {audio_file} удален")
    except Exception as e:
        print(f"⚠️ Не удалось удалить временный файл: {e}")

    # Вывод информации о результате
    print("\n" + "=" * 50)
    print(f"✅ Перевод завершен успешно!")
    if translated_text:
        print(f"Файл результата: {args.output}")
    else:
        print("❌ Перевод не был выполнен")
    print("=" * 50)


if __name__ == "__main__":
    main()
