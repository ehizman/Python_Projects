class SketchPad:
    def __init__(self, dimension):
        self.__board = [[0 for i in range(dimension)]for j in range(dimension)]

    @property
    def get__board(self):
        return self.__board

    def write_on(self, current_row_position, current_column_position):
        self.__board[current_row_position][current_column_position] = 1

    @property
    def display_board(self):
        return self.__board
