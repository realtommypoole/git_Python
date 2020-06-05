#This is an example of a class with two children

class Animal:
    #Define the main attributes
    name = 'Scientific Name not Specified'
    avg_weight = ' '
    avg_height = ' '
    
class Mammal(Animal):
    whale = False
    color = 'Mammal color not specified'

class Reptile(Animal):
    amphibious = True
    nocturnal = True
    
