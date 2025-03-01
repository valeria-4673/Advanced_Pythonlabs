import copy

class Delicacy:
    def __init__(self, name, price, weight):
        self.name = name
        self.price = price
        self.weight = weight

    def __str__(self):

        return "name:{}, price:{}, weight:{}".format(self.name, self.price, self.weight)
    
warehouse = list()
warehouse.append(Delicacy('Lolly Pop',0.4 ,133))
warehouse.append(Delicacy('Licorice', 0.1, 251))
warehouse.append(Delicacy('Chocolate', 1, 601))
warehouse.append(Delicacy('Sours', 0.01, 513))
warehouse.append(Delicacy('Hard candies', 0.3, 433))

print('Source list of candies')
for item in warehouse:
    print(item)

warehouse2 = copy.deepcopy(warehouse)

print("Result")

for item in warehouse2:  
        if item.weight > 300:
            item.price = item.price *0.8
        print(item)
