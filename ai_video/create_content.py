from openai import OpenAI
import re
import base64
from dotenv import load_dotenv
import os
from PIL import Image

current_dir = os.path.dirname(os.path.abspath(__file__))
os.makedirs(f"{current_dir}/input", exist_ok=True)
os.makedirs(f"{current_dir}/output", exist_ok=True)
os.makedirs(f"{current_dir}/input/image", exist_ok=True)
os.makedirs(f"{current_dir}/input/voice", exist_ok=True)

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
)


def create_narration(sample_input):
    """
    request create narration

    sample_input: string
    """
    try:
        response = client.chat.completions.create(model="gpt-4", messages=[
            {
                "role": "user",
                "content": "Create a short YouTube video of 30 seconds about \"{}\" for learners. Write a video narration with 5 main points. Each point in the video script has a background image. Please provide the following format: \n [Description of the background] \n((Narration content))".format(
                    sample_input)
            }
        ])
        return response.choices[0].message.content
    except Exception as e:
        print("create_narration Some thing went wrong ", e)
        return None


def create_voice(voice_input, audio_output):
    """
    request create voice

    voice_input: string
    audio_output: string
    """
    try:
        unused_list = re.findall(r"(Narration.*:)", voice_input)
        need_to_remove_phase = unused_list[0] if len(unused_list) > 0 else None
        new_voice_input = voice_input
        if need_to_remove_phase:
            new_voice_input = voice_input.replace(need_to_remove_phase, '')
        with client.audio.speech.with_streaming_response.create(
                input=new_voice_input,
                model="tts-1",
                voice="alloy",
        ) as audio:
            audio.stream_to_file(audio_output)
            return audio_output
    except Exception as e:
        print("create_voice Some thing went wrong ", e)
        return None


def create_image(image_des, output_image):
    """
    request create image

    image_des: string
    output_image: string
    """
    try:
        response = client.images.generate(
            model="dall-e-3",
            prompt=image_des,
            size="1024x1024",
            quality="standard",
            n=1,
            response_format="b64_json",
        )
        image_b64 = response.data[0].b64_json
        with open(output_image, "wb") as f:
            f.write(base64.b64decode(image_b64))
            return output_image
    except Exception as e:
        print("create_image Some thing went wrong ", e)
        return None


def create_content_file(sample_input):
    """
    request create content file

    sample_input: string
    """
    print("Creating narration ....")
    content = create_narration(sample_input)
    if not content:
        return

    # Extract prompts
    image_description_list = re.findall(r"\[(.*?)\]", content)
    script_list = re.findall(r"\((.*?)\)", content)

    # Generate visual representations of the concept image
    print("Generating visual representations of the concept image ...")
    # visual_file_name = "{}/output/mindMap.webp".format(current_dir)
    # create_image("\n".join(
    #     script_list) + " visual representations of the concept in mind maps",
    #              visual_file_name)

    visual_file_name = "{}/output/labeledDiagrams.webp".format(current_dir)
    create_image("\n".join(
        script_list) + " visual representations of the concept in labeled diagrams",
                 visual_file_name)

    # visual_file_name = "{}/output/infographics.webp".format(current_dir)
    # create_image("\n".join(
    #     script_list) + " visual representations of the concept in infographics",
    #              visual_file_name)

    # convert to jpg
    im = Image.open(visual_file_name).convert("RGB")
    new_visual_file_name = visual_file_name.replace(".webp", ".jpg")
    im.save(new_visual_file_name, "jpeg")
    print(
        "\n Generated visual representations of the concept image: {}\n".format(
            new_visual_file_name))
    os.remove(visual_file_name)

    # create images
    image_file_list = []
    len_img_des = len(image_description_list)
    for i, image_des in enumerate(image_description_list):
        print("Creating image ... [{}/{}]".format(i + 1, len_img_des))
        output_image = "{}/input/image/image{}.webp".format(current_dir, i)
        temp = create_image(image_des, output_image)
        if temp:
            image_file_list.append(temp)

    # create voices
    voice_file_list = []
    len_script_des = len(script_list)
    for i, script in enumerate(script_list):
        print("Creating voice ... [{}/{}]".format(i + 1, len_script_des))
        audio_output = "{}/input/voice/voice{}.mp3".format(current_dir, i)
        temp = create_voice(script, audio_output)
        if temp:
            voice_file_list.append(temp)

    return image_file_list, voice_file_list
