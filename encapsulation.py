# Title:        Encapsulation

class employee:
    def __init__(self, num, name, sal):
        self._num = 'number' #protected attribute
        self._name = 'name' #protected attribute
        self.__sal = 'salary' #private attribute





if __name__ == "__main__":
    e1 =  employee('4536',"JOE",'1000')
    e1._num = 4536
    e1.__sal = 1000
    print(e1.__sal, e1._num)
    
