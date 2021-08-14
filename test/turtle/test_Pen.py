from unittest import TestCase

from turtle_graphics.pen import Pen, PenPosition


class Test(TestCase):
    def test_pen_constructor(self):
        pen = Pen()
        self.assertIs(PenPosition.UP, pen.get__pen_position)

    def test_can_set_pen_down(self):
        pen = Pen()
        pen.set_pen_down()
        self.assertIs(PenPosition.DOWN, pen.get__pen_position)

    def test_can_set_pen_position_up_when_down(self):
        pen = Pen()
        pen.set_pen_down()
        pen.set_pen_up()
        self.assertIs(PenPosition.UP, pen.get__pen_position)

