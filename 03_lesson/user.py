class User:

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def print_sayName(self):
        print(self.first_name)

    def print_saySurname(self):
        print(self.last_name)

    def print_sayN_S(self):
        print(f'{self.first_name} {self.last_name}')



