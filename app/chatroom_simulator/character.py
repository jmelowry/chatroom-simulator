#!/usr/bin/env python3

class Character:
    def __init__(self, name, bio="", age=None):
        self.name = name
        self.bio = bio
        self.age = age

    def speak(self, message):
        # Simple print statement to simulate speaking
        print(f"{self.name} says: {message}")
    
    def __repr__(self):
        return f"<Character(name={self.name}, bio={self.bio}, age={self.age})>"