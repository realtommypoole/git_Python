
#parent class
class Element:
    name = "name"
    taste = "taste"
    mol_mkp = "mol_mkp"
    
    def information(self):
        msg = "\nName: {}\nTaste: {}\nMolecular Makeup: {}".format(self.name, self.taste, self.mol_mkp)
        return msg

#child class instance
class Earth(Element):
    name = "TerraFirma"
    taste = "Dry"
        
    def freeze(self):
        msg = "\nThe earth is begining to freeze!"
        return msg




if __name__ == "__main__":
    e2 = Earth()

    print(e2.information())
    print(e2.freeze())
