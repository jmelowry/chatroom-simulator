import argparse
import yaml

# Assuming Character and Chatroom classes are defined here or imported

def load_configuration(file_path):
    """Load YAML configuration from the given file path."""
    with open(file_path, 'r') as file:
        return yaml.safe_load(file)

def main(config_file):
    config = load_configuration(config_file)
    chatrooms = [Chatroom(**chatroom_config) for chatroom_config in config.get('chatrooms', [])]
    
    for chatroom in chatrooms:
        chatroom.simulate_conversation()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Chatroom Simulator")
    parser.add_argument("-f", "--file", type=str, default="default.yaml", help="Path to the configuration file.")
    args = parser.parse_args()

    main(args.file)