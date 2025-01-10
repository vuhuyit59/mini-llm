# Mini-LLM

**Mini-LLM** is a Python 3 project that provides a simplified framework for working with Language Learning Models (LLMs). This project is designed to help developers quickly integrate, test, and explore LLM capabilities in a lightweight and modular way.

## Features

- **Easy Integration**: Supports connecting to various LLM APIs (e.g., OpenAI).
- **Modular Design**: Add custom modules to extend functionality.
- **Interactive CLI**: Provides an interactive command-line interface for experimentation.
- **Prompt Engineering**: Tools to test and refine prompts.
- **Basic Fine-Tuning**: Lightweight mechanisms to customize models for specific tasks.

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/vuhuyit59/mini-llm
   cd mini-llm
   ```

2. Set up a virtual environment (optional but recommended):
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

## Usage

### Running the CLI
Start the interactive CLI:
```bash
python main.py
```

### Example Commands
- **Provide the content to create ai video**:
  ```bash
  > Please provide the content to create AI video: 
  ```

---

## Configuration

Set up your API keys and preferences in a `.env` file:
```env
OPENAI_API_KEY=your_openai_api_key
```

You can also modify the `config.json` file to customize the behavior of the CLI and model connections.

---


## Tools and Libraries Used

- **OpenAI**: For integrating OpenAI's language models.
- **MoviePy**: To create and edit video clips programmatically.
- **python-dotenv**: For managing environment variables.
- **Pillow**: For image processing and manipulation.

---

## How It Works

- **Get User Input**: The application takes input from the user, such as a text prompt.
- **Generate Narration and Image Description:**: Uses OpenAI to create a narration script and describe corresponding images.
- **Text-to-Speech for Audio**: Converts the narration into audio using a TTS (Text-to-Speech) engine.
- **Video Creation:**: Combines the generated audio and images using MoviePy to produce a complete video.

---


## OpenAI Models Used

- **GPT-4**: For generating narration and text-based outputs.
- **TTS-1**: For text-to-speech audio generation.
- **DALL-E 3**: For generating image descriptions and visuals.

---

## Next Steps

1. **Write FastAPI for Backend**: Develop a FastAPI-based backend to handle user inputs, API calls, and processing tasks.
2. **Self-Hosted File Upload**: Implement a self-hosted solution to store the created AI-generated videos.
3. **Next.js for Frontend**: Build a modern frontend interface using Next.js to provide an interactive user experience.

---

## Directory Structure

```plaintext
mini-llm/
├── main.py              # Entry point for the application
├── ai_video             # Create ai video service
├── .env.sample          # Env sample
├── requirements.txt     # Python dependencies
└── README.md            # Project documentation
```

---

## Contribution

Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a feature branch:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add feature description"
   ```
4. Push the branch:
   ```bash
   git push origin feature-name
   ```
5. Open a pull request.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Contact

For questions or support, reach out to [vuhuyit59@gmail.com].


