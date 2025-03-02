import json
option = int(input("What can I do for you? \n 1)Produce a JSON strin describing a "
                   +"vehicle\n 2) Decode JSON into data\n"))
print("your answer: ", option)

class Vehicle:
    def __init__(self, vin, year, mass):
        self.vin = vin
        self.year = year
        self.mass = mass
        
class MyEncoder(json.JSONEncoder):
    def default(self, objeto):
        if isinstance(objeto, Vehicle):
            return objeto.__dict__
        else:
            return super().default(self, z)
class MyDecoder(json.JSONDecoder):
    def __init__(self):
        json.JSONDecoder.__init__(self, object_hook=self.decode_veh)

    def decode_veh(self, d):
        return Vehicle(**d)
        
if option == 1:
    vin = input("VIN: ")
    year = input("Year: ")
    mass = float(input("Mass: "))
    ob= Vehicle(vin, year, mass)
    print(json.dumps(ob, cls=MyEncoder))

if option ==2:
    json_string = input("Enter json string: ")
    decodi = json.loads(json_string, cls=MyDecoder)
    print(decodi.__dict__)
