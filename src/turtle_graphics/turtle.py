from turtle_graphics.direction import Direction
from turtle_graphics.pen import Pen
from turtle_graphics.pen_position import PenPosition


class Turtle:
    def __init__(self):
        self.__current_row_position = 0
        self.__current_column_position = 0
        self.__pen = Pen()
        self.__direction = Direction.EAST

    @property
    def get__pen(self):
        return self.__pen

    @property
    def get__pen_position(self):
        return self.__pen.get__pen_position

    def penDown(self):
        self.__pen.set_pen_down()

    def penUp(self):
        self.__pen.set_pen_up()

    @property
    def get_direction(self):
        return self.__direction

    @property
    def get__current_position(self):
        return self.__current_row_position, self.__current_column_position

    def turn_right(self):
        if self.__direction == Direction.EAST:
            self.change_direction_to(Direction.SOUTH)

        elif self.__direction == Direction.SOUTH:
            self.change_direction_to(Direction.WEST)

        elif self.__direction == Direction.WEST:
            self.change_direction_to(Direction.NORTH)

        elif self.__direction == Direction.NORTH:
            self.change_direction_to(Direction.EAST)

    def change_direction_to(self, direction):
        self.__direction = direction

    def turn_left(self):
        if self.__direction == Direction.EAST:
            self.change_direction_to(Direction.NORTH)

        elif self.__direction == Direction.NORTH:
            self.change_direction_to(Direction.WEST)

        elif self.__direction == Direction.WEST:
            self.change_direction_to(Direction.SOUTH)

        elif self.__direction == Direction.SOUTH:
            self.change_direction_to(Direction.EAST)

    def move(self, sketch_pad, number_of_steps):
        if self.__direction == Direction.EAST:
            self.move_east(sketch_pad, number_of_steps)
        elif self.__direction == Direction.SOUTH:
            self.move_south(sketch_pad, number_of_steps)
        elif self.__direction == Direction.WEST:
            self.move_west(sketch_pad, number_of_steps)
        elif self.__direction == Direction.NORTH:
            self.move_north(sketch_pad, number_of_steps)


    def move_east(self, sketch_pad, number_of_steps):
        if self.get__pen_position == PenPosition.DOWN:
            for i in range(number_of_steps):
                sketch_pad.write_on(self.__current_row_position, self.__current_column_position)
                if i != number_of_steps - 1:
                    self.__current_column_position += 1
        else:
            self.__current_column_position += number_of_steps - 1

    def move_south(self, sketch_pad, number_of_steps):
        if self.get__pen_position == PenPosition.DOWN:
            for i in range(number_of_steps):
                sketch_pad.write_on(self.__current_row_position, self.__current_column_position)
                if i != number_of_steps - 1:
                    self.__current_row_position += 1
        else:
            self.__current_row_position += number_of_steps - 1

    def move_west(self, sketch_pad, number_of_steps):
        if self.get__pen_position == PenPosition.DOWN:
            for i in range(number_of_steps):
                sketch_pad.write_on(self.__current_row_position, self.__current_column_position)
                if i != number_of_steps - 1:
                    self.__current_column_position -= 1
        else:
            self.__current_column_position -= number_of_steps - 1

    def move_north(self, sketch_pad, number_of_steps):
        if self.get__pen_position == PenPosition.DOWN:
            for i in range(number_of_steps):
                sketch_pad.write_on(self.__current_row_position, self.__current_column_position)
                if i != number_of_steps - 1:
                    self.__current_row_position -= 1
        else:
            self.__current_row_position += number_of_steps - 1






