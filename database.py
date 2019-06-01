# database.py
import sys, shelve

def store_person(db):
    """
    让用户输入数据并将其存储到shelf对象中
    :param db:
    :return:
    """
    pid = input('Enter unique ID number: ')
    person = {}
    person['name'] = input('Enter name: ')
    person['age'] = input('Enter age: ')
    person['phone'] = input('Enter phone number: ')
    db[pid] = person

def looup_person(db):
    """
    让用户输入ID和所需的字段,并从shelf对象中获取相应的数据
    :param db:
    :return:
    """
    pid = input('Enter ID number: ')
    field = input('What would you like to know?(name,age,phone)')
    field = field.strip().lower()

    print(field.capitalize() + ':',db[pid][field])

def print_help():
    print('The available commands are:')
    print('store:Stores information about a person')
    print('lookup:Looks up a person from ID number')
    print('quit:Save changes and exit')
    print('?:Prints this message')

def enter_command():
    cmd = input('Enter command (? for help): ')
    cmd = cmd.strip().lower()
    return cmd

def main():
    database = shelve.open('D:\\database.dat')
    try:
        while True:
            cmd = enter_command()
            if cmd == 'store':
                store_person(database)
            elif cmd == 'lookup':
                looup_person(database)
            elif cmd == '?':
                print_help()
            elif cmd == 'quit':
                return
    finally:
        database.close()

if __name__ == '__main__':main()








