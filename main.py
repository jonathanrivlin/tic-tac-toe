import random
from typing import List, Union


class Game:
    def __init__(self) -> None:
        self.player: str = random.choice(['X', 'O'])
        self.board: List[List[str]] = [['-' for _ in range(3)] for _ in range(3)]

    def enter_loc(self, row: int, col: int, mark: str) -> None:
        self.board[row][col] = mark

    def print_board(self) -> None:
        for line in self.board:
            print(line)

    def check_for_win(self) -> Union[bool, str]:
        for line in self.board:
            if line[0] == line[1] == line[2] and line[0] != '-':
                return line[0]

        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] and self.board[0][col] != '-':
                return self.board[0][col]

        if (self.board[0][0] == self.board[1][1] == self.board[2][2] or self.board[0][2] == self.board[1][1] ==
                self.board[2][0]) and self.board[1][1] != '-':
            return self.board[1][1]
        return False

    def empty_spaces(self) -> bool:
        for line in self.board:
            for item in line:
                if item == '-':
                    return True
        return False

    def switch_player(self) -> None:
        if self.player == 'X':
            self.player = 'O'
        else:
            self.player = 'X'


game = Game()
game.print_board()
while not game.check_for_win() and game.empty_spaces():
    try:
        yx = input(f"{game.player}'s turn! choose a line and a column (y,x): ").split(',')
        if not yx[0].isdigit() or not yx[1].isdigit():
            raise ValueError
        y, x = int(yx[0]) - 1, int(yx[1]) - 1
        if game.board[y][x] == '-':
            game.enter_loc(y, x, game.player)
            game.print_board()
            game.switch_player()
    except ValueError:
        print("Enter a line number and column number separated by comma (1,2 for example). Please Try again...")
        continue
    except IndexError:
        print("Choose a line/column between 1 to 3. Please Try again...")
        continue

if game.check_for_win():
    print(f'{game.check_for_win()} Won!')
else:
    print("Tie! Game Over...")
