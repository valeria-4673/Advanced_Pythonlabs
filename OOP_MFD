class Scanner:
    def scan (self):
        print('scan() method from Scanner class')
        
class Printer:
    def printi (self):
        print('printi () method from Printer class')

class Fax:
    def send (self):
        print('send () method from Fax class')
    def printi (self):
        print('printi () method from Fax class')

class MFD_SPF(Scanner, Printer, Fax):
    pass

class MFD_SFP(Scanner, Fax, Printer):
    pass
        

MFD_SPF().scan()
MFD_SPF().printi()
MFD_SPF().send()

MFD_SFP().scan()
MFD_SFP().printi()
MFD_SFP().send()
