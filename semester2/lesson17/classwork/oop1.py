class User:
    def __init__(self, name, last_name, age) -> None:
        self.name = name
        self.last_name = last_name
        self.age = age

    def print_user(self):
        print(f"User {self.name}, {self.last_name}, (age = {self.age})")

    def change_name(self, name):
        self.name = name
