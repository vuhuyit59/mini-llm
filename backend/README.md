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

## Usage - Backend

### Running the CLI
Start the interactive CLI:
```bash
gurnicorn backend:main:app -bind 0.0.0.0:8000 -k uvicorn.workers.UvicornWorker
```

## Configuration

Set up your API keys and preferences in a `.env` file base on .env.sample:

You can also modify the `config.json` file to customize the behavior of the CLI and model connections.

---

## Tools and Libraries Used

- **OpenAI**: For integrating OpenAI's language models.
- **MoviePy**: To create and edit video clips programmatically.
- **python-dotenv**: For managing environment variables.
- **Pillow**: For image processing and manipulation.
- **Alembic**: For orm database migration .
- **ByteScale**: For File upload
---

## Migrate database with [Alembic](https://alembic.sqlalchemy.org/en/latest/index.html) 
 
- Setting PYTHONPATH = currentPath to environment
 `export PYTHONPATH=${currentPath}`
- Work directory : `/app`
- Auto generate version (auto detect models change): `alembic revision --autogenerate -m "your_text"` --> a new version will be created in `migration/versions/` (commands are auto generated so double check is needed) 
- Upgrade database to version: `alembic upgrade ${version}` version is revision number or 'head' text
- Downgrade database to version: `alembic downgrade ${version}` version is revision number or 'head' text
- Skip database migration to version: `alembic stamp ${version}` version is revision number or 'head' text


## How It Works

- **Api request create video**: The application takes input from the user, such as a text prompt throught the api.
- **Generate Narration and Image Description:**: Uses OpenAI to create a narration script and describe corresponding images.
- **Text-to-Speech for Audio**: Converts the narration into audio using a TTS (Text-to-Speech) engine.
- **Video Creation:**: Combines the generated audio and images using MoviePy to produce a complete video.

---


## OpenAI Models Used

- **GPT-4**: For generating narration and text-based outputs.
- **TTS-1**: For text-to-speech audio generation.
- **DALL-E 3**: For generating image descriptions and visuals.

---

## Directory Structure

```plaintext
mini-llm/
├── commands              
├── constants            
├── migrations            
├── core            
├── models            
├── queries            
├── routes            
├── serializers            
├── services           
├── utils           
├── .env.sample          
├── Dockerfile       
├── requirements.txt       
├── alembic.ini       
├── __init__.py       
├── responses.py       
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


