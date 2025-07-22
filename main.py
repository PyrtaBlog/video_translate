from src.audio_extract import audio_extract
from src.args import args_list
from src.transcribe import transcribe_to_text
from src.spellchecker import check_spell


def main():
    args = args_list().parse_args()
    output_audio = "./media/temp/output_audio.wav"
    audio_extract(args.path_video, output_audio=output_audio)
    result = transcribe_to_text(args.model, output_audio)
    print("Транскрибация выполнена успешно!")
    print("Проверяем наличие ошибок в тексте: ")
    checked_result = check_spell(result)

    with open(args.output, "w", encoding="utf-8") as f:
        f.write(checked_result)


if __name__ == "__main__":
    main()
