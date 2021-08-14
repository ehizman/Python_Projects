from turtle_graphics.pen_position import PenPosition


class Pen:
    def __init__(self):
        self.__pen_position = PenPosition.UP

    @property
    def get__pen_position(self):
        return self.__pen_position

    def set_pen_up(self):
        self.__pen_position = PenPosition.UP

    def set_pen_down(self):
        self.__pen_position = PenPosition.DOWN

