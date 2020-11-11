from common import enter_phone_number, clear_console
from register import Register
from person import Person

register = Register()


def select_by_name():
    family_name = input('\nEnter family name: ')
    first_name = input('Enter first name: ')
    person = register.find_person_by_name(family_name, first_name)
    if person is not None:
        handle_person(person)
    else:
        print('Could not find person, select action')
        print('1: Try again with another name')
        print('2: Go back to main menu')

        _choice = input('\nEnter choice number: ')
        if _choice == '1':
            select_by_name()
        elif _choice == '2':
            return
        else:
            print('Unknown choice, going back to menu')
            return


def select_by_phone_number():
    phone_number = enter_phone_number('\nEnter phone number: ')
    person = register.find_person_by_phone_number(phone_number)
    if person is not None:
        handle_person(person)
    else:
        print('Could not find person, select action')
        print('1: Try again with another phone number')
        print('2: Go back to main menu')

        _choice = input('\nEnter choice number: ')
        if _choice == '1':
            select_by_phone_number()
        elif _choice == '2':
            return
        else:
            print('Unknown choice, going back to menu')
            return


def handle_person(person):
    print('\nSelected person:')
    person.print_with_header()

    print('\nSelect action for this person')
    print('1: Edit phone number')
    print('2: Edit address')
    print('3: Delete person')
    print('4: Go back to main menu')

    _choice = input('\nEnter choice number: ')
    if _choice == '1':
        new_phone_number = enter_phone_number('\nEnter new phone number: ')
        person.phone_number = new_phone_number
        print('Phone number saved')
        input('\nPress enter to go back to main menu')
    elif _choice == '2':
        new_address = input('\nEnter new address: ')
        person.address = new_address
        print('Address saved')
        input('\nPress enter to go back to main menu')
    elif _choice == '3':
        register.delete_person(person)
        print('Person deleted')
        input('\nPress enter to go back to main menu')
    elif _choice == '4':
        return
    else:
        print('Unknown choice, going back to menu')
        return


def add_person():
    print('\nAdd person')
    family_name = input('Enter family name: ')
    first_name = input('Enter first name: ')
    phone_number = enter_phone_number('Enter phone number: ')
    address = input('Enter address: ')

    person = Person(family_name, first_name, phone_number, address)
    register.add_person(person)
    print('Person added')
    input('\nPress enter to go back to main menu')


def print_register():
    print()
    register.print()
    input('\nPress enter to go back to main menu')


while True:
    clear_console()

    print('Select action')
    print('1: Select person by name')
    print('2: Select person by phone number')
    print('3: Add person')
    print('4: Print register')
    print('5: Quit')

    choice = input('Enter choice number: ')
    if choice == '1':
        select_by_name()
    elif choice == '2':
        select_by_phone_number()
    elif choice == '3':
        add_person()
    elif choice == '4':
        print_register()
    elif choice == '5':
        register.save()
        exit(0)
