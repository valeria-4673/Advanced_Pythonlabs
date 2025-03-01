from datetime import datetime

def stampi (function):
    def internal_wrapper (*args):
        fecha_hora = (datetime.now())
        print(fecha_hora.strftime("%Y-%m-%d %H:%M:%S"))
        function (*args)
    return internal_wrapper
        

@stampi
def suma (*sumandos):
    suma = 0
    for element in sumandos:
        suma += element
    print(suma)
    
suma( 3, 2, 1, 4)
