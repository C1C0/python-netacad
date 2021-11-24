class X:
    def __init__(self):
        self.a = 1
        self.__privateA = 2

    def __Xahoj(self):
        print('X Ahoj')

class Y(X):
    def __init__(self):
        super().__init__()
        self.b = 2

    def __Yahoj(self):
        print('Y Ahoj')

class Z(Y):
    def __init__(self):
        super().__init__()
        self.c = 3

    def ahoj(self):
        print(super().__privateA)
        # self.__Yahoj(self)
        # self.__Xahoj(self)
        


myZ = Z()

print(myZ.__dict__)
myZ.ahoj()