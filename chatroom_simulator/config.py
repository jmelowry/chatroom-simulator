
# Chat configuration
characters = [
    {"name": "Alice", "bio": "A curious adventurer", "age": 30},
    {"name": "Bob", "bio": "A meticulous scientist", "age": 40},
]

discussion_topics = [
    {
        "topic": "What are the best ice cream flavors?",
        "length_of_responses": "short",
        "allowed_characters": ["Alice", "Bob"],
    },
]

global_settings = {
    "default_length_of_responses": "short",
    "max_conversation_turns": 20,
}

CHAT_CONFIG = {
    "characters": characters,
    "discussion_topics": discussion_topics,
    "global_settings": global_settings,
}

# Ollama API settings
OLLAMA_API_SETTINGS = {
    "model_name": "llama2",  # Ensure this model is available in your Ollama setup
}

# Duration of the conversation in minutes
DURATION_MINUTES = 3