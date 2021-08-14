from turtle_graphics.direction import Direction
from turtle_graphics.pen import Pen


class Turtle:
    def __init__(self):
        self.__current_position = [0, 0]
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
        return self.__current_position

    def turn_right(self):
        if self.__direction == Direction.EAST:
            self.__direction = Direction.SOUTH

        elif self.__direction == Direction.SOUTH:
            self.__direction = Direction.WEST

        elif self.__direction == Direction.WEST:
            self.__direction = Direction.NORTH

        elif self.__direction == Direction.NORTH:
            self.__direction = Direction.EAST
