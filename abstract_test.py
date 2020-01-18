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

    # https://stackoverflow.com/questions/35673474/using-abc-abcmeta-in-a-way-it-is-compatible-both-with-python-2-7-and-python-3-5
    def test_raises_exception(self):
        with self.assertRaises(TypeError) as error:
            processor = Abstract()
        actual = str(error.exception)
        expected = "Can't instantiate abstract class Abstract with abstract methods say"
        self.assertEqual(expected, actual)

if __name__ == "__main__":
    unittest.main()
