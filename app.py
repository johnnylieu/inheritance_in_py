class Human:
    def __init__(self, name, age, ethnicity):
        self.name = name
        self.age = age
        self.ethnicity = ethnicity

class Person(Human):
    def __init__(self, name, age, ethnicity):
        super().__init__(name, age, ethnicity)

    def introduce(self):
        print(f"my name is {self.name}, I am {self.age} years old and I am {self.ethnicity}")

Johnny = Person("Johnny", "21", "Vietnamese")
jintro = Johnny.introduce()

Jonathan = Person("Jonathan", "27", "Chinese")
j2intro = Jonathan.introduce()

Tyler = Person("Tyler", "probably 14", "Vietnamese")
tintro = Tyler.introduce()