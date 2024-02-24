import argparse
import yaml

# Assuming the Character and Chatroom classes are defined in separate modules and imported here
from chatroom_simulator.chatroom import Chatroom
from chatroom_simulator.character import Character

def load_configuration(file_path):
    """Load YAML configuration from the given file path."""
    try:
        with open(file_path, 'r') as file:
            return yaml.safe_load(file)
    except FileNotFoundError:
        print(f"Error: Configuration file '{file_path}' not found.")
        exit(1)
    except yaml.YAMLError as exc:
        print(f"Error parsing YAML configuration: {exc}")
        exit(1)

def main():
    parser = argparse.ArgumentParser(description="Chatroom Simulator")
    parser.add_argument("-f", "--file", type=str, default="default.yaml", help="Path to the configuration file.")
    args = parser.parse_args()

    # Load the YAML configuration
    config = load_configuration(args.file)

    # Initialize chatroom(s) from the configuration
    chatrooms = []
    for chatroom_config in config.get('chatrooms', []):
        # Initialize characters for this chatroom
        characters = [Character(**char_data) for char_data in chatroom_config.get('characters', [])]
        
        # Create the Chatroom instance with the loaded configuration and characters
        chatroom = Chatroom(name=chatroom_config.get('name'),
                            topics=chatroom_config.get('topics'),
                            characters=characters,
                            settings=chatroom_config.get('settings'),
                            model_settings=chatroom_config.get('model_settings'))
        chatrooms.append(chatroom)
    
    # Simulate conversations in each chatroom
    for chatroom in chatrooms:
        chatroom.simulate_conversation()

if __name__ == "__main__":
    main()
