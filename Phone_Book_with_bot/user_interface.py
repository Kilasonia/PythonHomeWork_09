import crude as cr
import logger as lg


print('\nThe phone book welcomes you')


def ls_menu():
    while True:
        print('\nMENU')
        print('1. Show all entries.')
        print('2. Find a number by last name.')
        print('3. Find a number by name.')
        print('4. Search by phone number.')
        print('5. Add a new entry.')
        print('6. Edit an existing record.')
        print('7. Delete an entry.')
        print('8. Close the program.\n')
        n = сhecking_the_number(input('Select a menu item: '))

        if n == 1:
            lg.logging.info('The user has selected item number 1')
            print(cr.retrive())

        elif n == 2:
            lg.logging.info('The user has selected item number 2')
            search = input('Enter your last name: ')
            lg.logging.info('User entered: {search}')
            print(cr.retrive(surname=search))

        elif n == 3:
            lg.logging.info('The user has selected item number 3')
            search = input('Enter a name: ')
            lg.logging.info('User entered: {search}')
            print(cr.retrive(name=search))

        elif n == 4:
            lg.logging.info('The user has selected item number 4')
            search = input('Enter phone number: ')
            lg.logging.info('User entered: {search}')
            print(cr.retrive(number=search))

        elif n == 5:
            lg.logging.info('The user has selected item number 5')
            name = input('Enter a name: ')
            lg.logging.info('User entered: {name}')
            surname = input('Enter your last name: ')
            lg.logging.info('User entered: {surname}')
            number = input('Enter phone number: ')
            lg.logging.info('User entered: {number}')
            email = input('Enter your email address: ')
            lg.logging.info('User entered: {email}')
            cr.create(name, surname, number, email)

        elif n == 6:
            lg.logging.info('The user has selected item number 6')
            print('1. Find a number by last name.')
            print('2. Find a number by name.')
            print('3. Search by phone number.')
            change = сhecking_the_number(input('Enter the item number: '))

            if change == 1:
                lg.logging.info('The user has selected item number 6.1')
                search = input('Enter your last name: ')
                lg.logging.info('User entered: {search}')
                cr.retrive(surname=search)
                user_id = input('Enter the record id: ')
                lg.logging.info('User entered: {user_id}')
                new_number = input('Enter a new phone number: ')
                lg.logging.info('User entered: {new_number}')
                cr.update(id=user_id, new_number=new_number)

            elif change == 2:
                lg.logging.info('The user has selected item number 6.2')
                search = input('Enter a name: ')
                lg.logging.info('User entered: {search}')
                cr.retrive(name=search)
                user_id = input('Enter the record id: ')
                lg.logging.info('User entered: {user_id}')
                new_number = input('Enter a new phone number: ')
                lg.logging.info('User entered: {new_number}')
                cr.update(id=user_id, new_number=new_number)

            elif change == 3:
                lg.logging.info('The user has selected item number 6.3')
                search = input('Enter your phone number: ')
                lg.logging.info('User entered: {search}')
                cr.retrive(number=search)
                user_id = input('Enter the record id: ')
                lg.logging.info('User entered: {user_id}')
                new_number = input('Enter a new phone number: ')
                lg.logging.info('User entered: {new_number}')
                cr.update(id=user_id, new_number=new_number)

            else:
                lg.logging.info('User entered an invalid menu value')
                print(
                    '\nThere is no such menu item.\nEnter a number, corresponding to the menu item.')

        elif n == 7:
            lg.logging.info('The user has selected item number 7')
            print('1. Find a number by last name.')
            print('2.Find a number by name.')
            print('3. Search by phone number.')
            deleting = сhecking_the_number(input('Enter the item number: '))

            if deleting == 1:
                lg.logging.info('The user has selected item number 7.1')
                search = input('Enter your last name: ')
                lg.logging.info('User entered: {search}')
                print(cr.retrive(surname=search))
                user_id = input('Enter the record id: ')
                lg.logging.info('User entered: {user_id}')
                cr.delete(id=user_id)

            elif deleting == 2:
                lg.logging.info('The user has selected item number 7.2')
                search = input('Enter a name: ')
                lg.logging.info('User entered: {search}')
                print(cr.retrive(name=search))
                user_id = input('Enter the record id: ')
                lg.logging.info('User entered: {user_id}')
                cr.delete(id=user_id)

            elif deleting == 3:
                lg.logging.info('The user has selected item number 7.3')
                search = input('Enter phone number: ')
                lg.logging.info('User entered: {search}')
                print(cr.retrive(number=search))
                user_id = input('Enter the record id: ')
                lg.logging.info('User entered: {user_id}')
                new_number = input('Enter a new phone number: ')
                cr.delete(id=user_id)

            else:
                lg.logging.info('User entered an invalid menu value')
                print(
                    '\nThere is no such menu item.\nEnter the number corresponding to the menu item.')

        elif n == 8:
            lg.logging.info('End')
            print('Thanks for the work!')
            break

        else:
            lg.logging.info('User entered an invalid menu value: {n}')
            print(
                '\nThere is no such menu item.\nEnter the number corresponding to the menu item.')

# def find(user_choice(n)):
# делаем срез по таблице и выдаем необходимые данные.


def сhecking_the_number(arg):
    while arg.isdigit() != True:
        lg.logging.info('User entered an invalid menu value: {arg}')
        print('\nYou didn,t enter a number.')
        arg = input('Enter the appropriate menu item: ')
    return int(arg)
