from src.audio_extract import audio_extract
from src.args import args_list


def main():
    args = args_list().parse_args()
    audio_extract(args.path_video)
    

if __name__ == '__main__':
    main()