class TimeInterval():
    
    def __init__(self, hour, minut, secs):
        self.hour = hour
        self.minut = minut
        self.secs = secs
        self.tod_secs = self.hour * 3600 + self.minut *60\
                        + self.secs
        
    def combinar(self, t2, operacion):
        
        if not isinstance(t2, TimeInterval):
            t2 = TimeInterval(hour = 0, minut = 0 , secs = t2)
            
        hour_2 = t2.hour
        minut_2 = t2.minut
        secs_2 = t2.secs
        tod_secs_2 = hour_2 * 3600 + minut_2 * 60 \
                     + secs_2
        
        if operacion == 'sumar':
            sumando = self.tod_secs + tod_secs_2
            mi_sum = self.conversor(sumando)
            return self.formateador(mi_sum)
        
        elif operacion == 'restar':
            restando = self.tod_secs - tod_secs_2
            mi_rest = self.conversor(restando)
            return self.formateador(mi_rest)

    def mi_mult(self, num):
        result = self.tod_secs * num
        mi_mult_HHMMSS = self.conversor(result)
        return self.formateador(mi_mult_HHMMSS)

    def conversor(self, result):
        
        hour = str(result // 3600)
        minut = str((result % 3600) // 60)
        secs = str((result % 3600) % 60)
        return [hour, minut, secs]
    
    def formateador (self, lista):
        final = ':'.join(lista)
        return final
        
    def __str__(self):      
        return str(self.hour)+':'+str(self.minut)+':'+str(self.secs)
           
t1 = TimeInterval(hour=21, minut=58, secs=50)
t2 = TimeInterval(1, 45, 22)    
print(t1)
print(t1.mi_mult(2))
print(t1.combinar(t2, 'sumar'))
print(t1.combinar(t2, 'restar'))
print(t1.combinar(62, 'sumar'))
print(t1.combinar(62, 'restar'))
