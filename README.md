# Video Translation Utility

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Консольная утилита для перевода видео с английского на русский (с поддержкой новых языков в будущем) с использованием модели Whisper. Автоматически извлекает аудио, транскрибирует речь и переводит содержание на целевой язык.

## ✨ Особенности

- Транскрипция аудио с помощью модели **Whisper** от OpenAI
- Перевод текста между языками (в настоящее время en → ru)
- Поддержка различных форматов видео и аудио
- Настройка размера модели Whisper для баланса скорости/качества
- Гибкая настройка параметров обработки
- Режим отладки для детального анализа процесса
- Оптимизация производительности (CPU/GPU)

## ⚙️ Установка

1. Клонируйте репозиторий:

```bash
git clone https://github.com/yourusername/video-translation-tool.git
cd video-translation-tool
```

2. Установите зависимости:

```bash
pip install -r requirements.txt
```

## 🚀 Использование

Базовый пример:

```bash
python translate_video.py path/to/your/video.mp4
```

Пример с параметрами:

```bash
python translate_video.py presentation.mp4 \
 --model medium \
 --output translated_subtitles.txt \
 --source-lang en \
 --target-lang ru \
 --chunk-size 3000 \
 --device cuda
```

## 🔧 Параметры командной строки

Обязательные параметры:

Параметр | Описание

video_path | Путь к видеофайлу для перевода

Параметры модели Whisper:

Параметр | Описание | По умолчанию

-m, --model | Размер модели (tiny, base, small, medium, large) | base

Параметры вывода:

Параметр | Описание | По умолчанию

-o, --output | Файл для сохранения перевода | translation.txt

## 🌍 Поддерживаемые языки (планы)

В текущей версии поддерживаются:

Исходный язык: Английский (en)

Целевой язык: Русский (ru)

Планы по расширению поддержки:

Добавление новых языков перевода (de, es, fr, zh)

Поддержка мультиязычных видео
