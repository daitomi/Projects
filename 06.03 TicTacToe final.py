class TicTacToe:

    cells = "         "
    cell_list = [cell for cell in cells]

    # boolean values for later
    X_win = False
    O_win = False
    player_X = True

    def grid(self):
        print(f"---------"
              f"\n| {self.cell_list[0]} {self.cell_list[1]} {self.cell_list[2]} |"
              f"\n| {self.cell_list[3]} {self.cell_list[4]} {self.cell_list[5]} |"
              f"\n| {self.cell_list[6]} {self.cell_list[7]} {self.cell_list[8]} |"
              f"\n---------")

    def coordinates(self):

        coordinate_list = [[1, 1], [1, 2], [1, 3], [2, 1], [2, 2], [2, 3], [3, 1], [3, 2], [3, 3]]

        while True:
            coordinate = input("Enter the coordinates: ").split()

            try:
                coordinate = [int(x) for x in coordinate]

            except ValueError:
                print("You should enter numbers!")

            else:
                index_ = (((coordinate[0] - 1) * 3) + coordinate[1] + 2) - 3

                available_coordinates = [i for i in coordinate_list if self.cell_list[coordinate_list.index(i)] == " "]
                not_available = [i for i in coordinate_list if self.cell_list[coordinate_list.index(i)] != " "]

                if coordinate in available_coordinates and self.player_X is True:
                    self.cell_list[index_] = "X"
                    self.player_X = False
                    break

                elif coordinate in available_coordinates and self.player_X is False:
                    self.cell_list[index_] = "O"
                    self.player_X = True
                    break

                elif coordinate in not_available:
                    print("This cell is occupied! Choose another one!")

                elif coordinate not in coordinate_list:
                    print("Coordinates should be from 1 to 3!")

    # checks if X or O won using the wins() method
    def checking(self):
        TicTacToe.wins(self, 0, 7, 3)
        TicTacToe.wins(self, 1, 8, 3)
        TicTacToe.wins(self, 2, 9, 3)
        TicTacToe.wins(self, 0, 3, 1)
        TicTacToe.wins(self, 3, 6, 1)
        TicTacToe.wins(self, 6, 9, 1)
        TicTacToe.wins(self, 0, 9, 4)
        TicTacToe.wins(self, 2, 7, 2)

    def wins(self, start, stop, step):

        win_x = []
        win_o = []

        for x in range(start, stop, step):
            if self.cell_list[x] == "X":
                win_x.append("yes")
                if len(win_x) == 3:
                    self.X_win = True
                    print("X wins")

            elif self.cell_list[x] == "O":
                win_o.append("yes")
                if len(win_o) == 3:
                    self.O_win = True
                    print("O wins")


def main():
    game = TicTacToe()
    game.grid()

    while True:

        game.coordinates()
        game.grid()

        game.checking()
        if game.O_win is True or game.X_win is True:
            break

        elif " " not in game.cell_list:
            print("Draw")
            break


if __name__ == '__main__':
    main()
