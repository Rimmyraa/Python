# class Person():
#     name: str = ''
#     age: int = 0
#     gender: str = ''

#     def say_hello(self):
#         print(f'Hello, my name is {self.name}')

# person1 = Person()
# person1.name = 'Rimma'
# person1.age = 14
# person1.gender = 'Female'

# print(person1.name)

# person1.say_hello()

# print(person1.__dict__)

# print(dir(person1)) #dir - выдаст все действия над об'ектом

#/////////////////////////////////////////////////////////////////////////////////////////

# class Animal():
#     name = ''
#     age = ''
    
#     def cat_dog(self):
#         print(f'Name - {self.name}\nAge - {self.age}')


# cat = Animal()
# cat.name = 'Sima'
# cat.age = 3

# cat.cat_dog()

# dog = Animal()
# dog.name = 'Zyza'
# dog.age = 4


# print(cat.__dict__)
# print(dog.__dict__)


#/////////////////////////////////////////////////////////////////////////////////////////

# class Car():
    
#     # brand = ''
#     # year = ''
#     # max_speed = ''
    
#     def __init__(self, brand: str, year: int, max_speed: str):
#         self.brand = brand
#         self.year = year
#         self.max_speed = max_speed
        
#     def get_max_speed(self):
#         return self.max_speed
    
#     def set_max_speed(self, new_max_speed):
#         self.max_speed = new_max_speed
        
# volvo = Car(
#     brand='Volvo',
#     year=2022,
#     max_speed=260
# )

# print(volvo.get_max_speed())

# volvo.set_max_speed(310) #тут меняем скорость

# print(volvo.get_max_speed())


#/////////////////////////////////////////////////////////////////////////////////////////

# class BankAccount():
#     def __init__(self, owner_name, account_id, balance=0):
#         self.owner = owner_name
#         self.account = account_id
#         self.balance = balance
        
#     def add_money(self, invoice):
#         self.balance += invoice 
#         print(f'You added {invoice}$. Your balance: {self.balance}$')
        
#     def withdraw(self, money):
#         if money > self.balance:
#             print('You dont have to enough money')
#         else:
#             self.balance -= money
#             print(f'You successfully cashed out {money}$. Your balance: {self.balance}$')
        
# account1 = BankAccount('Rimma', 2334534, 2789)
# account1.add_money(1000)
# account1.withdraw(3789)

#/////////////////////////////////////////////////////////////////////////////////////////

