from animal import Animal
from dog import Dog
from cat import Cat
class Home:
    def __init__(self, pets = []):
        self.pets = pets
    
    def adopt_pets(self,pet):
        for all in self.pets:
            if all == pet:
                raise Exception ("You can't adopt the same pet twice")
        self.pets.append(pet)
    
if __name__ == "__main__":
    home = Home()
    dog2 = Dog("Rax", "barks")
    cat2 = Cat("Stormy", "meow")
    home.adopt_pets(dog2)
    home.adopt_pets(cat2)
    print("current pets")
    print(home.pets[0].name)
    print(home.pets[1].name)