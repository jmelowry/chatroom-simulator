#!/usr/bin/env python3

import random
import time

class Chatroom:
    def __init__(self, name, topics, characters, settings, model_settings):
        self.name = name
        self.topics = topics
        self.characters = characters
        self.settings = settings
        self.model_settings = model_settings

    def simulate_conversation(self):
        print(f"Starting conversation in chatroom: {self.name}")
        print(f"Topics: {', '.join(self.topics)}")
        for topic in self.topics:
            # Announce the topic to discuss
            print(f"Chatroom topic announced: {topic}")
            for character in self.characters:
                # Generate a random delay between 2 and 5 seconds
                delay = random.randint(2, 5)
                time.sleep(delay)  # Pause execution for a random duration
                
                # Simulate the character speaking
                character.speak(f"excited to discuss {topic}")