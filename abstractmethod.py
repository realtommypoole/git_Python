


from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod
    def move(self):
        pass

class Human(Animal):
    def move(self):
        print("I can walk and run")

class Snake(Animal):
    def move(self):
        print("I can slither")


if __name__ == "__main__":
    a1 = Human()
    a1.move()

    a2 = Snake()
    a2.move()
