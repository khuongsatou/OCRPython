#Định nghĩa một lớp gồm có tham số lớp và có cùng tham số instance
class Person:
    #instance
    name="Person"
    def __init__(self, name = None):
        self.name = name


objName = Person("Khuong")
print("%s name is %s" %(Person.name,objName.name))