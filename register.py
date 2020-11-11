from person import Person
from common import print_header


def format_line(line):
    return line.strip().replace('\n', '')


def load_contact_list(register_name):
    file = open(register_name + '.reg', 'r+', encoding='utf-8')
    contact_list = []

    current_line = file.readline()
    while not current_line == '':
        family_name = format_line(current_line)
        first_name = format_line(file.readline())
        phone_number = format_line(file.readline())
        address = format_line(file.readline())

        person = Person(family_name, first_name, phone_number, address)
        contact_list.append(person)

        current_line = file.readline()

    return contact_list


class Register:

    def __init__(self, register_name='register'):
        self.register_name = register_name
        self.contact_list = load_contact_list(register_name)
        self.sort_contact_list()

    def sort_contact_list(self):
        self.contact_list.sort(key=lambda person: person.family_name)

    def find_person_by_name(self, family_name, first_name):
        for person in self.contact_list:
            if person.family_name == family_name and person.first_name == first_name:
                return person

        return None

    def find_person_by_phone_number(self, phone_number):
        for person in self.contact_list:
            if person.phone_number == phone_number:
                return person

        return None

    def add_person(self, person):
        self.contact_list.append(person)
        self.sort_contact_list()

    def delete_person(self, person):
        self.contact_list.remove(person)

    def save(self):
        with open(self.register_name + '.reg', 'w+', encoding='utf-8') as file:
            for person in self.contact_list:
                file.write(person.family_name + '\n')
                file.write(person.first_name + '\n')
                file.write(person.phone_number + '\n')
                file.write(person.address + '\n')
        print('Register saved')

    def print(self):
        print_header()
        for person in self.contact_list:
            person.print()
