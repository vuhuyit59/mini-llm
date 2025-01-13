from moviepy import concatenate_videoclips, AudioFileClip, ImageClip, \
    concatenate_audioclips
from moviepy.video.fx import Resize, CrossFadeIn, CrossFadeOut
from itertools import cycle, islice
import os

from backend.services.bytescale import upload_file

current_dir = os.path.dirname(os.path.abspath(__file__))

video_width, video_height = 1024, 1024


# Function to create a fading clip from an image
def create_fade_clip(image_path, duration=2):
    # Load the image
    clip = ImageClip(image_path, duration=duration)
    # Resize to fit vertical dimensions
    Resize(clip, height=video_height, width=video_width)
    # Add fade-in and fade-out effects
    fade_in = CrossFadeIn(duration=1)
    fade_in.apply(clip)
    fade_out = CrossFadeOut(duration=1)
    fade_out.apply(clip)
    return clip


def create_video(image_paths, voice_paths):
    try:
        print("Creating video ....")
        audio_clips = [AudioFileClip(voice_name) for voice_name in voice_paths]
        composite_audio = concatenate_audioclips(audio_clips)
        new_image_paths = image_paths
        if len(image_paths) != len(audio_clips):
            new_image_paths = list(
                islice(cycle(image_paths), len(audio_clips)))
        image_clips = [
            create_fade_clip(
                img_name,
                duration=audio_clips[i].duration
            )
            for i, img_name in enumerate(new_image_paths)
        ]

        # Concatenate the clips with crossfade effects
        video = concatenate_videoclips(image_clips, method="compose")

        video.audio = composite_audio
        video.with_audio = composite_audio

        # Export the final video
        output_path = "{}/output/output.mp4".format(current_dir)
        video.write_videofile(output_path, fps=24, audio_codec="aac")
        for x in voice_paths + image_paths:
            os.remove(x)

        # Upload video
        with open(output_path, "rb") as file:
            file_url = upload_file(file)
            os.remove(output_path)
            return file_url
    except Exception as e:
        print("create_video failed ", e)
        return None
