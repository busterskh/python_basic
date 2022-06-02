class Cell:
    def __init__(self, num):
        self.sign = ' '
        self.cell_num = num
        self.busy = False


class Board:
    board_data = []
    for index in range(9):
        board_data.append(Cell(index))

    def print_board(self):
        print()
        print(self.board_data[0].sign, '|', self.board_data[1].sign, '|', self.board_data[2].sign)
        print('–' * 10)
        print(self.board_data[3].sign, '|', self.board_data[4].sign, '|', self.board_data[5].sign)
        print('–' * 10)
        print(self.board_data[6].sign, '|', self.board_data[7].sign, '|', self.board_data[8].sign)

    def move(self, cell, sign):
        self.board_data[cell - 1].sign = sign
        self.board_data[cell - 1].busy = True
        self.print_board()

    def check_win(self, sign):
        win_coord = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
        for each in win_coord:
            if self.board_data[each[0]].sign == self.board_data[each[1]].sign == self.board_data[each[2]].sign \
               and self.board_data[each[0]].sign == sign:
                return 1
        else:
            if all(cell.busy for cell in self.board_data):
               return 2


class Player:
    def __init__(self, name, sign):
        self.name = name
        self.sign = sign

    def player_move(self):
        cell_num = int(input(f'\n{self.name}, в какую клетку ставим {self.sign}?\n'))
        if not board.board_data[cell_num - 1].busy:
            board.move(cell_num, self.sign)
            if board.check_win(self.sign) == 1:
                print(f'{self.name} победил!')
                return True
            elif board.check_win(self.sign) == 2:
                print('\nНичья!')
                return True
        else:
            print('Клетка занята.')
            self.player_move()


player_1 = Player('Ivan', 'X')
player_2 = Player('Tom', 'O')
board = Board()

count = 0
while count != 9:
    if player_1.player_move():
        break
    count += 1
    if player_2.player_move():
        break
    count += 1
