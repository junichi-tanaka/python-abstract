from abc import *
import six

@six.add_metaclass(ABCMeta)
class Abstract(object):
    def __init__(self):
        pass

    @classmethod
    @abstractmethod
    def num_of_legs(cls):
        raise NotImplementedError()

    @abstractmethod
    def say(self):
        raise NotImplementedError()


class Dog(Abstract):
    @classmethod
    def num_of_legs(cls):
        return 4

    def say(self):
        return 'Bow!'

class Human(Abstract):
    @classmethod
    def num_of_legs(cls):
        return 2

    def say(self):
        return 'Hello!'


if __name__ == "__main__":
    dog = Dog()
    dog.say()
    human = Human()
    human.say()
