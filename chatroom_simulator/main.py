#!/usr/bin/env python3

from datetime import datetime, timedelta
import time
import re
from ollama import chat
from .config import CHAT_CONFIG, OLLAMA_API_SETTINGS, DURATION_MINUTES

def filter_response(content):
    """Filter out emojis and modern slang, returning a more '90s-style response."""
    # Remove emojis
    content = re.sub(r'[^\x00-\x7F]+', '', content)
    # Optionally, trim the response or take the first sentence for brevity
    sentences = content.split('. ')
    if sentences:
        return sentences[0] + '.'
    return content

def clean_response(message):
    message = re.sub(r"\*laughs\*", "😄", message)
    message = re.sub(r"<biggrin>", "😁", message)
    message = re.sub(r"^\w+:\s+\w+:\s+", "", message)
    message = re.sub(r"\s{2,}", " ", message)
    message = message.strip().rstrip('.').rstrip()
    return message

def simulate_random_conversation(characters, topics, settings, duration_minutes, verbose=False):
    print("Simulating Random Conversation in a 90's style chat room...\n")
    
    end_time = datetime.now() + timedelta(minutes=duration_minutes)
    conversation_history = []

    try:
        for topic in topics:
            print(f"Topic: {topic['topic']}\n")

            while datetime.now() < end_time:
                for character in characters:
                    context = " ".join(conversation_history[-2:])
                    prompt = f"{character['name']} is thinking about {topic['topic']}. Remember, express reactions with words or traditional emoticons only."

                    response = chat(OLLAMA_API_SETTINGS["model_name"], messages=[{'role': 'user', 'content': prompt}], stream=False)
                    message_content = response['message']['content'] if 'message' in response else "No response."

                    message_content = filter_response(message_content)
                    message_content = clean_response(message_content)

                    formatted_message = f"{character['name']}: {message_content}"
                    print(formatted_message + "\n")
                    
                    conversation_history.append(message_content)

                    time.sleep(1)

                    if datetime.now() >= end_time:
                        break

                if datetime.now() >= end_time:
                    break

    except KeyboardInterrupt:
        print("\nConversation ended by user.")

def main():
    simulate_random_conversation(CHAT_CONFIG["characters"], CHAT_CONFIG["discussion_topics"], CHAT_CONFIG["global_settings"], DURATION_MINUTES, verbose=True)

if __name__ == "__main__":
    main()
