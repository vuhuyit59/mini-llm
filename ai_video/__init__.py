from ai_video.create_content import create_content_file
from ai_video.create_video import create_video


def create_ai_video(sample_input):
    image_file_list, voice_file_list = create_content_file(sample_input)
    create_video(image_file_list, voice_file_list)
    return

