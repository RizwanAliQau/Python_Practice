class Mammal:     # DRY
    def walk(self):
        print("walk")


class dog(Mammal):
    def bark(self):
        print("bark")

class cat(Mammal):
    pass


dog1 = dog()
dog1.bark()

