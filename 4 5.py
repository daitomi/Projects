class TicTacToe:
    cells = input("Enter cells: ")

    cell_list = [cell for cell in cells]
    coordinate_list = [[1, 1], [1, 2], [1, 3], [2, 1], [2, 2], [2, 3], [3, 1], [3, 2], [3, 3]]
    available_coordinates = []
    not_available = []
    coordinate = None
    index_ = None

    X = False
    O = False
    empty_cells = False
    count_x = 0
    count_o = 0

    def grid(self):
        print(f"---------"
              f"\n| {self.cell_list[0]} {self.cell_list[1]} {self.cell_list[2]} |"
              f"\n| {self.cell_list[3]} {self.cell_list[4]} {self.cell_list[5]} |"
              f"\n| {self.cell_list[6]} {self.cell_list[7]} {self.cell_list[8]} |"
              f"\n---------")

    def coordinates(self):

        while True:
            self.coordinate = input("Enter the coordinates: ").split()

            try:
                self.coordinate = [int(x) for x in self.coordinate]

            except ValueError:
                print("You should enter numbers!")

            else:
                self.index_ = (((self.coordinate[0] - 1) * 3) + self.coordinate[1] + 2) - 3

                self.available_coordinates = [i for i in self.coordinate_list if
                                              self.cell_list[self.coordinate_list.index(i)] == "_"]
                self.not_available = [i for i in self.coordinate_list if
                                      self.cell_list[self.coordinate_list.index(i)] != "_"]

                # self.coordinate_list.index(i)

                if self.coordinate in self.available_coordinates:
                    self.cell_list[self.index_] = "X"
                    break

                elif self.coordinate in self.not_available:
                    print("This cell is occupied! Choose another one!")

                elif self.coordinate not in self.coordinate_list:
                    print("Coordinates should be from 1 to 3!")


def main():
    game = TicTacToe()
    game.grid()
    game.coordinates()
    game.grid()


if __name__ == '__main__':
    main()


