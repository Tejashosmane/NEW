class Person:
    __name="anonymous"

    def __init__(self) -> None:
        print("init")
        self.clsmtd()

    def __hello(self):
        print("hello")

    def clsmtd(self):
        print(self.__name)
        self.__hello()

class man(Person):
    def __init__(self) -> None:
        super().__init__()
        

m1=man()
