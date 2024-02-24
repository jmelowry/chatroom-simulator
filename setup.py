from setuptools import setup, find_packages

setup(
    name='chatroom-simulator',
    version='0.1.0',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'chatroom-simulator=chatroom_simulator.main:main',
        ],
    },
    # include other setup arguments as needed
)