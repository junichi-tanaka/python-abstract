import unittest
from abstract import *

class TestAbstract(unittest.TestCase):
    def test_abstract_dog(self):
        expected = "Bow!"
        dog = Dog()
        actual = dog.say()
        self.assertEqual(expected, actual)

    def test_abstract_human(self):
        expected = "Hello!"
        human = Human()
        actual = human.say()
        self.assertEqual(expected, actual)

if __name__ == "__main__":
    unittest.main()
