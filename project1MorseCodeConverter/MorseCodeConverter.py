class MorseCodeConverter:
    def __init__(self):
        self.morse_code_dict = {
    'A': '.-',     'B': '-...',   'C': '-.-.',   'D': '-..',    'E': '.',
    'F': '..-.',   'G': '--.',    'H': '....',   'I': '..',     'J': '.---',
    'K': '-.-',    'L': '.-..',   'M': '--',     'N': '-.',     'O': '---',
    'P': '.--.',   'Q': '--.-',   'R': '.-.',    'S': '...',    'T': '-',
    'U': '..-',    'V': '...-',   'W': '.--',    'X': '-..-',   'Y': '-.--',
    'Z': '--..',

    '1': '.----',  '2': '..---',  '3': '...--',  '4': '....-',  '5': '.....',
    '6': '-....',  '7': '--...',  '8': '---..',  '9': '----.',  '0': '-----',

    ',': '--..--', '.': '.-.-.-', '?': '..--..', '/': '-..-.',  '-': '-....-',
    '(': '-.--.',  ')': '-.--.-', ' ': '/'
}

    def str_to_morse(self, message):
        '''Translate a message into a morse code'''
        morse = []
        for chr in message:
            try:
                if chr.isalpha():
                    chr = chr.capitalize()
                morse.append(self.morse_code_dict[chr])
            except BaseException as e:
                print(f"Your request {message} was not completed due of invalid character: {e}")
                return f'The character: {chr} does not exist in our morse code list: {self.morse_code_dict}'
        return morse