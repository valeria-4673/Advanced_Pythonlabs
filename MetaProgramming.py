from datetime import datetime

class My_Meta(type):
    classes_created = []
    def __new__(mcs, name, bases, dictionary):
        obj = super().__new__(mcs, name, bases, dictionary)
        My_Meta.classes_created.append(name)
        obj.instantiation_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return obj
    
class My_Class1(metaclass = My_Meta):
    def get_instantiation_time(self):
        return self.instantiation_time
    

o1 =My_Class1()
print(o1.get_instantiation_time())
print(My_Meta.classes_created)
