class MyClass():
    def __init__(self):
        self.public_attribute = 'Public attribute' #Доступ із будь-якої точки
        self.__private_attribute = 'Private attribute' #Доступ заборонений із будь-якої точки
        self._protected_attribute = 'Protected attribute' #Доступ у класі (між методами)
        
    def public_method(self):
        print('This is public method')
        
    def __private_method(self):
        print('This is private method')
        
    def _protected_method(self):
        print('This is protected method')
        
obj = MyClass()
print(obj.public_attribute)
obj.public_method()

print(obj._protected_attribute)
obj._protected_method()
        