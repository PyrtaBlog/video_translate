from googletrans import Translator
from tqdm import tqdm


def translate_text(text):
    translator = Translator()
    try:
        # Разбиваем текст на части, если он слишком длинный
        max_chunk_size = 5000
        chunks = [
            text[i : i + max_chunk_size] for i in range(0, len(text), max_chunk_size)
        ]

        translated_text = ""
        for chunk in tqdm(chunks, desc="Перевод текста"):
            # СИНХРОННЫЙ перевод с использованием стабильной версии
            translation = translator.translate(chunk, src="en", dest="ru")
            translated_text += translation.text + " "

        return translated_text.strip()
    except Exception as e:
        print(f"Ошибка перевода: {e}")
        return text
