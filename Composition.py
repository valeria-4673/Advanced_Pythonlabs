
class Engine:
    def __init__(self,fuel):
        self.state = "off"
        self.fuel = fuel
        
    def start(self):
        self.state = "on"
        print("Engine has startedn with ", self.fuel)
    
    def stop(self):
        self.state = "off"
        print("Engine has stopped")

    def get_state(self):
        print("The engine has status is ", self.state)

class ElectricEngine (Engine):
    def __init__(self):
        super().__init__("Electricity")

    def start(self):
        print("Battery will work")
        super().start()
        
    def stop(self):
        print("Battery will stop working")
        super().stop()
        
class GasEngine (Engine):
    def __init__(self):
        super().__init__("Gas")

    def start(self):
        print("Tank will work")
        super().start()
        
    def stop(self):
        print("Tank will stop working")
        super().stop()
        
class Vehicle:
    def __init__(self, vin, engine):
        self.vin = vin
        self.engine = engine

o1 = Vehicle("452C", ElectricEngine())
o1.engine.start()
o1.engine.get_state()
o1.engine.stop()
o1.engine.get_state()

o2 = Vehicle("dfsdf3", GasEngine())
o2.engine.start()
o2.engine.get_state()
o2.engine.stop()
o2.engine.get_state()
