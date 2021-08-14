from unittest import TestCase

from turtle_graphics.direction import Direction
from turtle_graphics.pen_position import PenPosition
from turtle_graphics.turtle import Turtle


class Test(TestCase):
    def test_turtle_constructor(self):
        turtle = Turtle()
        self.assertIsNotNone(turtle)

    def test_that_turtle_has_pen_upon_construction(self):
        turtle = Turtle()
        self.assertIsNotNone(turtle.get__pen)

    def test_that_turtle_pen_is_up_upon_creation(self):
        turtle = Turtle()
        self.assertIs(PenPosition.UP, turtle.get__pen_position)

    def test_that_turtle_can_tell_pen_to_set_its_position_down(self):
        turtle = Turtle()
        turtle.penDown()
        self.assertIs(PenPosition.DOWN, turtle.get__pen_position)

    def test_that_turtle_can_tell_pen_to_set_its_position_up_after_it_has_been_set_down(self):
        turtle = Turtle()
        turtle.penDown()
        turtle.penUp()
        self.assertIs(PenPosition.UP, turtle.get__pen_position)

    def test_that_turtle_direction_is_EAST_upon_creation(self):
        turtle = Turtle()
        self.assertIs(Direction.EAST, turtle.get_direction)

    def test_that_turtle_current_position_is_at_0_0_upon_creation(self):
        turtle = Turtle()
        self.assertListEqual([0, 0], turtle.get__current_position)

    def test_that_turtle_can_turn_right_when_facing_EAST(self):
        turtle = Turtle()
        turtle.turn_right()
        self.assertIs(Direction.SOUTH, turtle.get_direction)

    def test_that_turtle_can_turn_right_when_facing_south(self):
        turtle = Turtle()
        turtle.turn_right()
        turtle.turn_right()
        self.assertIs(Direction.WEST, turtle.get_direction)

    def test_that_turtle_can_turn_right_when_facing_west(self):
        turtle = Turtle()
        turtle.turn_right()
        turtle.turn_right()
        turtle.turn_right()
        self.assertIs(Direction.NORTH, turtle.get_direction)

    def test_that_turtle_can_turn_right_when_facing_north(self):
        turtle = Turtle()
        turtle.turn_right()
        turtle.turn_right()
        turtle.turn_right()
        turtle.turn_right()
        self.assertIs(Direction.EAST, turtle.get_direction)
