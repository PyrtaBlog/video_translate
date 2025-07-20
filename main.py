from src.audio_extract import audio_extract
from src.args import args_list
from src.transcribe import transcribe_to_text


def main():
    args = args_list().parse_args()
    output_audio = "./media/temp/output_audio.aac"
    audio_extract(args.path_video, output_audio=output_audio)
    result = transcribe_to_text(args.model, output_audio)
    print("Транскрибация выполнена успешно!")
    
    

if __name__ == '__main__':
    main()