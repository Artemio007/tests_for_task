from random import randint

# Task_1 lesson 16 task_3


class Bird:
    def __init__(self, name):
        self.name = name

    def fly(self):
        return f"The {self.name} can fly"

    def walk(self):
        return f"the {self.name} can walk"


class FlyingBird(Bird):
    def __init__(self, name, ration: int = None):
        self.name = name
        self.ration = {
            1: "meat",
            2: "chicken",
            3: "apples"
        }
        self.eat = self.ration.get(ration, self.ration.get(randint(1, 3)))
        super().__init__(name)

    def fly(self):
        return f"The {self.name} can fly"

    def walk(self):
        return f"the {self.name} can walk"

    def eats(self):
        if self.eat is None:
            return f"the {self.name} like {self.ration.get(randint(1, 3))}"
        else:
            return f"the {self.name} like {self.eat}"


class NonFlyingBird(Bird):
    def __init__(self, name):
        self.name = name
        super().__init__(name)

    def walk(self):
        return f"the {self.name} can walk"

    def fly(self):
        return f"the {self.name} can't fly"


class SuperBird(FlyingBird):
    def __init__(self, name, ration: int = None):
        self.name = name
        self.ration = ration
        super().__init__(name)

    def fly(self):
        return f"the {self.name} can fly"

    def walk(self):
        return f"the {self.name} can walk"

    def eats(self):
        if self.eat is None:
            return f"the {self.name} like {self.ration.get(randint(1, 3))}"
        else:
            return f"the {self.name} like {self.eat}"

    def swim(self):
        return f"the {self.name} can swim"
