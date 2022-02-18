class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Johnny:
    def __init__(self, name, age, race):
        super().__init__(name, age)
        self.race = race

    def introduce(name, age, race):
        print(f"my name is {name}, I am {age} years old and I am {race}")


class Jonathan:
    def introduce(name, age, race):
        print(f"my name is {name}, I am {age} years old and I am {race}")


class Tyler:
    def introduce(name, age, race):
        print(f"my name is {name}, I am {age} years old and I am {race}")

Johnny.introduce("Johnny", "don't trip", "Vietnamese")
Jonathan.introduce("Jonathan", "idk", "Chinese")
Tyler.introduce("Tyler", "probably 14", "Vietnamese")