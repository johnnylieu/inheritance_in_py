class Human:
    def __init__(self, age, ethnicity):
        self.age = age
        self.ethnicity = ethnicity

class Johnny(Human):
    def __init__(self, name, age, ethnicity):
        super().__init__(age, ethnicity)
        self.name = name

        print(f"my name is {self.name}, I am {self.age} years old and I am {self.ethnicity}")


class Jonathan(Human):
    def __init__(self, name, age, ethnicity):
        super().__init__(age, ethnicity)
        self.name = name
        
        print(f"my name is {self.name}, I am {self.age} years old and I am {self.ethnicity}")


class Tyler(Human):
    def __init__(self, name, age, ethnicity):
        super().__init__(age, ethnicity)
        self.name = name

        print(f"my name is {self.name}, I am {self.age} years old and I am {self.ethnicity}")

Johnny("Johnny", "21", "Vietnamese")
Jonathan("Jonathan", "27", "Chinese")
Tyler("Tyler", "probably 14", "Vietnamese")