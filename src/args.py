import argparse

def args_list():
    parser = argparse.ArgumentParser(description="Видео переводчик")
    parser.add_argument("path_video", help="Путь до видео файла")
    parser.add_argument("-m", "--model", default="base", choices=["tiny", "base", "small", "medium", "large"], 
                      help="Выбор модели whisper, на выбор [\"tiny\", \"base\", \"small\", \"medium\", \"large\"], по умолчанию \"base\".")
    parser.add_argument("-o", "--output", default="./media/temp/result.txt", help="Имя файла после обработки")
    return parser