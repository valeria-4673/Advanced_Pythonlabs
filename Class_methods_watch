class InvalidText (Exception):
    pass

class Watch:
    __watches_created = 0
    
    def __init__(self):
        Watch.__watches_created += 1
    
    @classmethod
    def get_number_of_watches_created(cls):
        return cls.__watches_created
        
    @staticmethod
    def validate(text):
        if len(text) < 40 and text.isalnum():
            return True
        else:
            raise InvalidText ("No se permiten espacios en blanc o simbol")
            return False
    
    @classmethod
    def graving(cls, text):
        if cls.validate:
            _watch = cls()
            _watch.text = text
        return _watch
    

        
o1 = Watch ()
Watch.validate("Alabama")
o2 = Watch.graving("Alabama")

try:
    Watch.validate("·%%4 ")
    o3 = Watch("·%%4 ")
except InvalidText as e:
    print(e)

print (Watch.get_number_of_watches_created())
