class Player():
    def __init__(self, piece):
        self.piece = piece

    def give_instructions(self):
        return f'Type the number of the square you want to add "{self.piece}": '