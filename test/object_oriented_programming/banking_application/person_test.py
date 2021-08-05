import unittest

from object_oriented_programming_in_python.banking_application.person import Person


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, True)  # add assertion here

    def test_constructor(self):
        ehis = Person("Ehis", "Edemakhiota", "edemaehiz@gmail.com")
        self.assertEqual("Ehis", ehis.get_first_name)
        self.assertEqual("Edemakhiota", ehis.get_last_name)
        self.assertEqual("edemaehiz@gmail.com", ehis.get_email)

    def test_person_has_account_number_upon_creation(self):
        ehis = Person("Ehis", "Edemakhiota", "edemaehiz@gmail.com")
        print(ehis.get__accounts)
        self.assertNotEqual(0, len(ehis.get__accounts))


if __name__ == '__main__':
    unittest.main()
