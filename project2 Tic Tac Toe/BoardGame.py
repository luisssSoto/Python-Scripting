class BoardGame:
    def __init__(self):
        self.__board_dict = {
            'l1': '-------------------\n',
            1: '|     ',
            2: '|     ',
            3: '|     ',
            'l2': '|\n-------------------\n',
            4: '|     ',
            5: '|     ',
            6: '|     ',
            'l3': '|\n-------------------\n',
            7: '|     ',
            8: '|     ',
            9: '|     ',
            'l4': '|\n-------------------\n',}
        self.__winner = ''

    def __str__(self):
        '''Show the board'''
        self.board = ''
        for val in self.__board_dict.values():
            self.board += val
        return self.board

    def modify_board(self, square, piece):
        '''Modify the board if the num of square is valid and if the square is empty'''
        is_it_success = False
        while is_it_success is False:
            while square < 0 or square > 9:
                print(f"Sorry but the number of square: {square} is out of the range: 1 - 9 ")
                square = int(input("Try it again! "))
            if self.__board_dict[square] == '|     ':
                self.__board_dict[square] = f'|  {piece}  '
                is_it_success = True
            else:
                print(f"The square is not empty: {self.__board_dict[square]}")
                square = int(input("Try it again! "))
                is_it_success = False
        
    def ways_to_win(self, piece):
        if self.__board_dict[1] == f'|  {piece}  ' and self.__board_dict[2] == f'|  {piece}  ' and self.__board_dict[3] == f'|  {piece}  ' or\
            self.__board_dict[4] == f'|  {piece}  ' and self.__board_dict[5] == f'|  {piece}  ' and self.__board_dict[6] == f'|  {piece}  ' or\
            self.__board_dict[7] == f'|  {piece}  ' and self.__board_dict[8] == f'|  {piece}  ' and self.__board_dict[9] == f'|  {piece}  ' or\
            self.__board_dict[1] == f'|  {piece}  ' and self.__board_dict[4] == f'|  {piece}  ' and self.__board_dict[7] == f'|  {piece}  ' or\
            self.__board_dict[2] == f'|  {piece}  ' and self.__board_dict[5] == f'|  {piece}  ' and self.__board_dict[8] == f'|  {piece}  ' or\
            self.__board_dict[3] == f'|  {piece}  ' and self.__board_dict[6] == f'|  {piece}  ' and self.__board_dict[9] == f'|  {piece}  ' or\
            self.__board_dict[1] == f'|  {piece}  ' and self.__board_dict[5] == f'|  {piece}  ' and self.__board_dict[9] == f'|  {piece}  ' or\
            self.__board_dict[3] == f'|  {piece}  ' and self.__board_dict[5] == f'|  {piece}  ' and self.__board_dict[7] == f'|  {piece}  ':
            return True
        else:
            return False

    def declare_winner(self, piece):
        '''Declare a winner or a tie'''
        if self.ways_to_win(piece):
            self.__winner = piece
        elif self.__board_dict[1] != '|     ' and self.__board_dict[2] != '|     ' and self.__board_dict[3] != '|     ' and\
            self.__board_dict[4] != '|     ' and self.__board_dict[5] != '|     ' and self.__board_dict[6] != '|     ' and\
            self.__board_dict[7] != '|     ' and self.__board_dict[8] != '|     ' and self.__board_dict[9] != '|     ':
            self.__winner = 'Tie'
        return self.__winner
