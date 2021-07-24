from unittest import TestCase

from chapter_four.string_rangoli import string_rangoli


class Test(TestCase):
    def test_string_rangoli(self):
        result = string_rangoli(3)
        self.assertEqual("""----c----
        --c-b-c--
        c-b-a-b-c
        --c-b-c--
        ----c----""", result)

