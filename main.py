from ai_video import create_ai_video

if __name__ == '__main__':
    while True:
        try:
            user_input = input(
                "Please provide the content to create AI video: \t")
            if user_input:
                create_ai_video(user_input)
        except EOFError:
            break
