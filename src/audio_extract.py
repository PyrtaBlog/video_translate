import ffmpeg
import os


def audio_extract(input_video, output_audio):
    try:

        if os.path.exists(output_audio):
            extract_a(input_video, output_audio)
        else:
            os.mkdir("./media/temp/")
            extract_a(input_video, output_audio)

        print(f"Аудио сохранено в {output_audio}")
    except ffmpeg.Error as e:
        print(f"Ошибка: {e.stderr}")


def extract_a(input_video, output_audio):
    ffmpeg.input(input_video).output(
        output_audio,
        format="wav",
        acodec="pcm_s16le",
        ar=16000,
        ac=1,
        vn=None,
    ).run(overwrite_output=True, quiet=True)
