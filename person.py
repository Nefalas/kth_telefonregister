from common import print_header, print_person


class Person:

    def __init__(self, family_name, first_name, phone_number, address):
        self.family_name = family_name
        self.first_name = first_name
        self.phone_number = phone_number
        self.address = address

    def print(self):
        print_person(self)

    def print_with_header(self):
        print_header()
        print_person(self)
