#!/usr/bin/env python3

from setuptools import setup, find_packages

setup(
    name='chatroom-simulator',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'ollama',
        'PyYAML',
    ],
    entry_points={
        'console_scripts': [
            'chatroom-simulator=chatroom_simulator.main:main',
        ],
    },
)