import sqlite3
import sys

class Todo:
    def __init__(self):
        self.conn = sqlite3.connect('todo2.db')
        self.c = self.conn.cursor()
        self.create_task_table()
        
    def create_task_table(self):
        self.c.execute('''CREATE TABLE IF NOT EXISTS tasks (
                     id INTEGER PRIMARY KEY,
                     name TEXT NOT NULL,
                     priority INTEGER NOT NULL
                     );''')
    
    def add_task(self):
        
        while True:
            name = input('Enter task name: ')
            if name != "" and name != " ":
                break
                
        while True:
            priority = int(input('Enter priority: '))
            if priority >= 1:
                break
        
        self.c.execute('INSERT INTO tasks (name, priority) VALUES (?,?)', (name, priority))

    def find_task(self):
        name_to_find = input('Enter task name to find: ')
        for row in self.c.execute('SELECT * FROM tasks'):
            if row[1]== name_to_find:
                print("retrieved", row)
        
    def show_tasks(self):
        self.c.execute('SELECT * FROM tasks')
        rows = self.c.fetchall()
        print("todas ", rows)
        for row in rows:
            print("t", row)

    def change_priority(self):
        while True:
            name = input('Enter task name to update: ')
            if name != "" and name != " ":
                break
        while True:
            priority = int(input('Enter new priority: '))
            if priority >= 1:
                break
        self.c.execute('UPDATE tasks SET priority = ? WHERE name = ?', (priority, name))

    def delete_task(self):
        idid = input("Enter the id to delete: ")
        self.c.execute('DELETE FROM tasks WHERE id = ?', (idid,))

app = Todo()

def menu ():
    print("1. Show Tasks \n 2. Add Task \n 3. Change Priority \n 4. Delete Task \n 5. Exit")
    option = input("Select the option: ")
    if option == "5":
        sys.exit()
    if option == "1":
        app.show_tasks()
    if option == "2":
        app.add_task()        
    if option == "3":
        app.change_priority()
    if option == "4":
        app.delete_task()
        
while True:
    menu()
