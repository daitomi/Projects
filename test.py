class TicTacToe:
    cells = input("Enter cells: ")
    X = False
    O = False
    empty_cells = False
    count_x = 0
    count_o = 0

    def grid(self):
        print(f"---------"
              f"\n| {self.cells[0]} {self.cells[1]} {self.cells[2]} |"
              f"\n| {self.cells[3]} {self.cells[4]} {self.cells[5]} |"
              f"\n| {self.cells[6]} {self.cells[7]} {self.cells[8]} |"
              f"\n---------")

    def wins(self, start, stop, step):
        win_x = []
        win_o = []
        for x in range(start, stop, step):
            if self.cells[x] == "X":
                win_x.append("yes")
                if len(win_x) == 3:
                    self.X = True

            elif self.cells[x] == "O":
                win_o.append("yes")
                if len(win_o) == 3:
                    self.O = True

            elif self.cells[x] == "" or "_":
                self.empty_cells = True

    def counter(self):
        for x in range(0, 9, 1):
            if self.cells[x] == "X":
                self.count_x += 1
            elif self.cells[x] == "O":
                self.count_o += 1

    def checking(self):
        TicTacToe.wins(self, 0, 7, 3)
        TicTacToe.wins(self, 1, 8, 3)
        TicTacToe.wins(self, 2, 9, 3)
        TicTacToe.wins(self, 0, 3, 1)
        TicTacToe.wins(self, 3, 6, 1)
        TicTacToe.wins(self, 6, 9, 1)
        TicTacToe.wins(self, 0, 9, 4)
        TicTacToe.wins(self, 2, 7, 2)

    def result(self):

        if self.count_x - self.count_o not in (0, 1, -1):
            print("Impossible")

        elif self.O is True and self.X is True:
            print("Impossible")

        elif self.O:
            print("O wins")
        elif self.X:
            print("X wins")

        elif self.O is False and self.X is False:
            if self.empty_cells is False:
                print("Draw")
            elif self.empty_cells is True:
                print("Game not finished")


def main():
    game = TicTacToe()
    game.grid()
    game.checking()
    game.counter()
    game.result()


if __name__ == '__main__':
    main()


