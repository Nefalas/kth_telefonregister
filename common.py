import os


def __print_columns(family_name, first_name, phone_number, address):
    print('{:<15}{:<15}{:<15}{:^30}'.format(
        family_name,
        first_name,
        phone_number,
        address))


def print_header():
    __print_columns('First name', 'Last name', 'Phone number', 'Address')
    print('=' * 75)


def print_person(person):
    __print_columns(
        person.family_name,
        person.first_name,
        person.phone_number,
        person.address)


def enter_phone_number(prompt):
    phone_number = input(prompt)
    if not phone_number.isnumeric():
        print('Phone number can only contain digits and no spaces')
        return enter_phone_number(prompt)
    else:
        return phone_number


def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')
