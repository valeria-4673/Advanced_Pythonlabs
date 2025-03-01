import random

class Apple:
    apples_counter = 0
    weight_controler = 0
    
    def __init__(self, weight):
        Apple.apples_counter += 1
        Apple.weight_controler += weight
        
while(Apple.apples_counter < 1000 and Apple.weight_controler < 300):
    objecto = Apple(random.uniform(0.2, 0.5))

print('{} apples were created. The total weight of the pedido is: {}'.format(
    Apple.apples_counter, Apple.weight_controler))
