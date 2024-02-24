#!/usr/bin/env python3

class Character:
    def __init__(self, name, bio, age):
        self.name = name
        self.bio = bio
        self.age = age

    def __repr__(self):
        return f"<Character {self.name} (Age: {self.age})>"