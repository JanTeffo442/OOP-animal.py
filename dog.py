from animal import Animal
class Dog(Animal):

    def __init__(self, name, animal_sound):
        super().__init__(name, animal_sound)

    def food(self):
        print(self.name + " eats")
    
    def sound(self):
        print(self.sounds + " barks")

dog1 = Dog("Rax", "Dog")
dog1.food()
dog1.sound()