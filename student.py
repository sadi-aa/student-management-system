from abc import ABC,abstractmethod
class Person(ABC):
    def __init__(self,name,age):
        self.__name=name
        self.__age=age

    @abstractmethod
    def details(self):
        pass
class student(Person):
    def __init__(self, name, age,id):
        super().__init__(name, age)
        self.__id=id
    def details(self):
        return f"name:{self.__name},age:{self.__age},student-id:{self.__id}"
    

        