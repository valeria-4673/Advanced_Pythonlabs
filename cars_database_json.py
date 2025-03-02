import requests
import json

key_names = ["id", "brand", "model", "production_year","convertible" ]
key_widths = [20, 20, 20, 20, 20]

def check_server(cid=None):
    try:
        reply = requests.head('http://localhost:3000/cars/')
    except requests.exceptions.RequestException:
        return False
    return reply.status_code == requests.codes.ok

def print_menu():
    print("+"+"-"*25+"+")
    print(" "*5+"Vintage cards Database"+" "*5)
    print("+"+"-"*25+"+")
    print("1)List a car\n 2)Add\n 3)Delete\n 4)Update\n 0)Exit\n")

def read_user_choice():
    choice = input("Your Choice: ")
    if choice not in ['0', '1', '2', '3', '4']:
        print("Invalid choice")
    return choice

def print_header():    
    for (n, w) in zip(key_names, key_widths):
        print(n.ljust(w), end='| ')
    print()

def print_car(car):
    for (n, w) in zip(key_names, key_widths):
        print(str(car[n]).ljust(w), end='| ')
    print()

def list_cars():
    try:
        reply = requests.get('http://localhost:3000/cars/')
        json = reply.json()
        print_header()
        for car in json:
            print_car(car)
    except requests.exceptions.RequestException:
        print("Couldnt connect to the server")
        
def add_car():
    pre = {"id": "" , "brand": "" , "model": "", "production_year": "" ,"convertible": ""}
    idid= input("Enter id: ")
    brand = input("Enter brand: ")
    model = input("Enter model: ")
    p_year = input("Enter production year: ")
    convertible = input("Enter convertible: ")
    
    pre["id"]= idid
    pre["brand"]= brand
    pre["model"]= model
    pre["production_year"]= p_year
    pre["convertible"]= convertible
    print(pre)
    
    try:
        reply = requests.post('http://localhost:3000/cars', data=json.dumps(pre))
    except requests.RequestException:
        print('Communication error')

def update_car():
    id_actualizar = input("id del car a actualizar: ")
    url = 'http://localhost:3000/cars/'+id_actualizar
    try:
        reply = requests.get(url)
        diction_dese = reply.json()
        print(diction_dese)
        to_upd= input("What do you wanna update? ")
        new_val = input("Write the new val: ")
        diction_dese[to_upd]= new_val
        print(diction_dese)
        
        try:
            reply = requests.put(url, data=json.dumps(diction_dese))
        except requests.exceptions.RequestException:
            print("Couldnt connect to the server")
                        
    except requests.exceptions.RequestException:
        print("Couldnt connect to the server")
        
def del_car():
    
    id_del = input("id del car a eliminar: ")
    url = 'http://localhost:3000/cars/'+id_del
    try:
        reply = requests.delete(url)
    except requests.exceptions.RequestException:
        print("Couldnt connect to the server")        

while True:
    if not check_server():
        print("Server is not responding - quitting!")
        exit(1)
    print_menu()
    choice = read_user_choice()
    if choice == '0':
        print("Bye!")
        exit(0)
    elif choice == '1':
        list_cars()
    elif choice == '2':
    
        add_car()
    elif choice == '3':
        del_car()
    elif choice == '4':
        update_car()
