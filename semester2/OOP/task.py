# class Kotik():
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def present(self):
#         print(f'Name: {self.name}, Age: {self.age}')
         
# cat = Kotik('Sima', 3)   
# cat.present()

#/////////////////////////////////////////////////////////////////////////////////////////

# class Student():
#     def __init__(self, name, course):
#         self.name = name
#         self.course = course
#         self.subject = []
        
#     def new_subject(self, new_subject):
#         self.subject.append(new_subject)
        
#     def present(self):
#         print(f'Name: {self.name}, course: {self.course}, subject: {self.subject}')
        
# student = Student('A', 'b')
# student.new_subject('c')
# student.present()
        
#/////////////////////////////////////////////////////////////////////////////////////////

# class Book():
#     def __init__(self, title, author, year):
#         self.title = title
#         self.author = author
#         self.year = year
        
#     def __str__(self):
#         return f'title - {self.title}, author - {self.author}, year - {self.year}'
    
# book = Book('a', 'b', 'c')
# print(book)

#/////////////////////////////////////////////////////////////////////////////////////////

# Реалізуйте клас "Телефонний довідник", який зберігає контакти (ім'я та номер телефону)
# та має методи для додавання нового контакту, видалення контакту за ім'ям та отримання номеру телефону за ім'ям.

class Phone_book():
    def __init__(self):
        self.contacts = {}
        
    def add_contact(self, name, phone_number):
        self.contacts[name] = phone_number
        
    def remove_contact(self, name):
        if name in self.conacts:
            del self.contacts[name]
        else:
            print('Contact not found')
            
    def get_phone_number(self, name):
        return self.contacts.get(name, 'Contact not found')
    
phone = Phone_book()
phone.add_contact('Rimma', '380950111959')
phone.add_contact('Bibza', '380666180588')
print(phone.contacts)