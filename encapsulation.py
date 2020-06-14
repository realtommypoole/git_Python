# Title:        Encapsulation

class employee:
    def __init__(self, name, sal):
        self._name = name #protected attribute
        self.__sal = sal #private attribute

    def pSal(self):
        print("An employee makes " + self.__sal)

        





if __name__ == "__main__":
     e1 = employee('JOE','1000')
     e1.pSal()
    
