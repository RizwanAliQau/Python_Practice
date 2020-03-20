class Person:  # upper case first
    def __init__(self, name):  # constructor
        self.name = name

    def talk(self):  # method
        print(f"hi, talk {self.name}")


john = Person("john smith")  # object
john.talk()

bob = Person ("bob")  # note: each object is a different instance of a class
bob.talk()