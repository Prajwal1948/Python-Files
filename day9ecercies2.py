class Animal:
    def __init__(self, name, species):
        self.name=name
        self._species=species

    def get_species(self):
        return self._species

class Dog(Animal):
    def __init__(self, name, species):
        super(Dog, self).__init__(name,species)

    def get_dog_spcies(self):
        return self.__species

class Cat(Animal):
    def __init__(self, name, species):
        super(Cat, self).__init__(name,species)

    def get_cat_spcies(self):
        return self._species

def main():
    animal=Animal("caeaser","XYZ")
    print(animal._species, animal.name)
    dog=Dog('Caeaser','Dog')
    cat=Cat('ABC','Cat')

if __name__=="__main__":
    main()