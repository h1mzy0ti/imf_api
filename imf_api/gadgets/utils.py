import random

CODENAMES = [
    "The Nightingale", "The Kraken", "Phantom Viper", "Shadow Fox",
    "The Whisper", "Ghost Talon", "Crimson Widow", "Iron Falcon"
]

def generate_codename():
    return random.choice(CODENAMES)

def generate_success_probability():
    return f"{random.randint(50, 100)}%"  # range: 50% to 100%
