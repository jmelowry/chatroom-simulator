from datetime import datetime, timedelta
import time
from ollama import chat
from config import CHAT_CONFIG, OLLAMA_API_SETTINGS, DURATION_MINUTES

def simulate_random_conversation(characters, topics, settings, duration_minutes, verbose=False):
    print("Simulating Random Conversation in a 90's style chat room...\n")
    
    end_time = datetime.now() + timedelta(minutes=duration_minutes)
    try:
        for topic in topics:
            print(f"Topic: {topic['topic']}\n")
            conversation_history = []

            while datetime.now() < end_time:
                for character in characters:
                    # Use the last few messages for context
                    context = " ".join(conversation_history[-2:])
                    prompt = f"Given the topic '{topic['topic']}', if {character['name']} were typing a message in a chat room right now, what would they type? Keep it casual and feel free to use emojis. Previous messages: {context}"

                    # Call the chat function with the refined prompt
                    response = chat(OLLAMA_API_SETTINGS["model_name"], messages=[{'role': 'user', 'content': prompt}], stream=False)
                    message_content = response['message']['content'] if 'message' in response else "No response."
                    
                    # Print the direct message without narrative descriptions
                    print(f"{character['name']}: {message_content}\n")
                    
                    # Update conversation history with the new message
                    conversation_history.append(f"{character['name']}: {message_content}")

                    time.sleep(1)  # Simulate typing delay

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