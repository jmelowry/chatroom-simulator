# AI Chat Room Simulator

This project simulates a chat room conversation using AI characters, powered by the Ollama API. It demonstrates a simple yet effective way to generate dynamic conversations between predefined characters on various topics.

## Features

- Simulates conversations with AI-generated responses.
- Supports random conversation flow.
- Configuration through `config.py` for easy adjustments.
- Utilizes the Ollama API for generating chat completions.
- Graceful handling of conversation duration and interruption.

## Setup

1. **Install Requirements:** Ensure Python 3.7+ is installed on your system. Then install the required packages using:

    ```
    pip install -r requirements.txt
    ```

2. **Ollama API:** This project requires access to the Ollama API. Ensure the Ollama service is running and accessible.

3. **Configuration:** Adjust the `config.py` file to set up characters, discussion topics, and Ollama API settings. The default model name and API URL can be changed according to your setup.

## Running the Simulation

To start the simulation, run:

```
python3 main.py
```

The script will initiate a chat room simulation based on the configuration provided in `config.py`. The conversation will run for the duration specified in the configuration or until manually stopped with a keyboard interrupt (Ctrl+C).

## Customization

You can customize the simulation by editing the `config.py` file:

- `characters`: Define the characters participating in the chat.
- `discussion_topics`: Set up topics for discussion.
- `OLLAMA_API_SETTINGS`: Configure the Ollama API URL and model name.
- `DURATION_MINUTES`: Specify how long the simulation should run.

This project is designed for experimentation and demonstration purposes, showcasing how AI can be utilized to create dynamic and engaging chat simulations.

