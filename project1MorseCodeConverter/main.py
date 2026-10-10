from MorseCodeConverter import MorseCodeConverter
from PlaySound import PlaySound

# Step 1. Input
# Catch the user's message
user_str = input(f"Type the sentence to be translated into morse code: ")

# Step 2. Proccessing
# Proccess the message coming from the user
converter = MorseCodeConverter()
code_morse = converter.str_to_morse(user_str)

# Step 3. Output
# Deliver the morse code if it is validated formate
while type(code_morse) is not list:
    print(code_morse)
    user_str = input(f"Try it again: ")
    code_morse = converter.str_to_morse(user_str)
else:
    play_sound = PlaySound(code_morse)
    play_sound.play_code_morse()