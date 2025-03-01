class AccountException(Exception):
    pass
class MovInvalid(Exception):
    pass
class SuprimirException(Exception):
    pass

class IndivAccnt:
    def __init__(self, number):
        self.__number = number
        self.__balance = 0
        
    @property
    def number (self):
        return self.__number

    @number.setter
    def number (self, number):
        raise AccountException ("Not possible to modify the account number")

    @property
    def balance (self):
        return self.__balance
    
    @balance.setter
    def balance (self, amount):
        if amount > 0:
            self.__balance += amount
            if amount > 100000:
                print("El mov será auditado")
        else:
            raise MovInvalid("No se puede set un negativo o 0 en balance")

    @number.deleter
    def number (self):
        if self.__balance > 0:
            self.__number = None
        else:
            raise SuprimirException ("Account has founds I can not delete them")
    
o1 = IndivAccnt(45856993256)
print(o1.number)

try:
    o1.number = 563789
except AccountException as ae:
    print(ae)

try:
    o1.balance = 5000
    print(o1.balance)
    o1.balance = -3000
    o1.balance = 130000
    print("El balance tras super suma", o1.balance)
except MovInvalid as mi:
    print(mi)
    
o2 = IndivAccnt (589632)
print("Cuenta 2",o2.number)
print("Vaciada", o2.balance)

try:
    del o2.number
    
except SuprimirException as se:
    print(se)
