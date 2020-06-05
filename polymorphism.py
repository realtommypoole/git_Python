#Polymorhpism Assignment
#
#
#
# Tommy Poole


#parent class
class Person():
    name = "unknown"
    age = None

    def getInfo(self):
        entry_name = input ("Enter your name: ")
        entry_age = int(input ("Enter your age: "))
        if (entry_age > 20):
            print ("Hi {}, you are an adult!".format(entry_name))
        else:
            print ("Hi {}, you are almost an adult!".format(entry_name))


#child class 1
class Male(Person):
    gender = "Male"

    def getInfo(self):
        entry_name = input ("Enter your name: ")
        entry_age = int(input ("Enter your age: "))
        entry_gender = input ("Enter your gender: ")
        if (entry_age > 20 and entry_gender == self.gender):
            print ("You are an adult {}!".format(entry_gender))
        else:
            print ("{}, is not an adult male!".format(entry_name))

# child class 2
class Female(Person):
    gender = "Female"

    def getInfo(self):
        entry_name = input ("Enter your name: ")
        entry_age = int(input ("Enter your age: "))
        entry_gender = input("Enter your gender: ")
        if (entry_age >= 21 and entry_gender == self.gender):
            print ("{}, she is an adult!".format(entry_name))
        else:
            print ("{}, is not an adult female!".format(entry_name))





if __name__ == "__main__":

    p1 = Person()
    p1.getInfo()

    p2 = Male()
    p2.getInfo()

    p3 = Female()
    p3.getInfo()
