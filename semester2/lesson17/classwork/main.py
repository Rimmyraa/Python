# first_name1 = "Rimma"
# last_name1 = "Sergeeva"
# age1 = 15
#
# first_name2 = "Evan"
# last_name2 = "Peters"
# age2 = 36
#
# def print_user(first_name, last_name, age):
#     print(f"User {first_name}, {last_name}, {age}")
#
# print_user(first_name1, last_name1, age1)
# print_user(first_name2, last_name1, age2)


user1 = {
    "first_name":"Rimma",
    "last_name":"Segeeva",
    "age": 15
}

user2 = {
    "first_name":"Evan",
    "last_name":"Peters",
    "age": 36
}

def print_user(user):
    print(f"User {user['first_name']}, {user['last_name']}, {user['age']}")

print_user(user1)
print_user(user2)