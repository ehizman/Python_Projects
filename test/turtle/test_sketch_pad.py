from unittest import TestCase

from turtle_graphics.sketch_pad import SketchPad


class Test(TestCase):
    def test_sketch_pad(self):
        sketch_pad = SketchPad(6)
        self.assertListEqual([[0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0]], sketch_pad.display_board)
