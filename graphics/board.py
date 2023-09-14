from enum import Enum

class Cell(Enum):
    EMPTY = " "
    CROSS = "X"
    CIRCLE = "O"

class Board():

    def __init__(self) -> None:
        self.ROW = 15
        self.COL = 15
        self.board = [[Cell.EMPTY for i in range(self.COL)] for j in range(self.ROW)]

    def __str__(self) -> str:
        board_str = "  ┌" + "───┬" * (self.COL - 1) + "───┐\n"

        for i in range(self.ROW):
            num_of_row = 15 - i
            row = str(num_of_row) + "│" if num_of_row >= 10 else " " + str(num_of_row) + "│"

            for j in range(self.COL):
                row += " " + self.board[i][j].value + " │"
            board_str += row + "\n"

            if i < self.ROW - 1:
                board_str += "  ├" + "───┼" * (self.COL - 1) + "───┤\n"

        board_str += "  └" + "───┴" * (self.COL - 1) + "───┘\n"
        board_str += "    " + "   ".join(chr(ord('A') + i) for i in range(self.COL))

        return board_str
    
    def add_move(self, input, symbol) -> int:
        try:
            col = int(ord(input[0]) - ord('A'))
            row = int(input[1:3]) - 1
        except ValueError:
            print("Координаты записаны неверно")
            return -1
        
        if (not -1 < col < self.COL or not -1 < row < self.ROW):
            print("Координаты записаны неверно")
            return -1
        
        if symbol not in [Cell.CROSS, Cell.CIRCLE, Cell.EMPTY]:
            print("Ошибка с определением символа")
            return -2
        
        if self.board[14-row][col] != Cell.EMPTY:
            print("Клетка уже занята")
            return -3
        
        self.board[14-row][col] = symbol
        return 0


if __name__ == "__main__":
    board = Board()

    board.add_move("G7", Cell.CROSS)
    board.add_move("H5", Cell.CIRCLE)
    board.add_move("A5", Cell.CROSS)
    board.add_move("O15", Cell.CIRCLE)
    board.add_move("A1", Cell.CROSS)
    board.add_move("A15", Cell.CIRCLE)
    board.add_move("O1", Cell.CROSS)

    board.add_move("!!", Cell.CIRCLE)

    print(board)
