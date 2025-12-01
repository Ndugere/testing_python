def write_into_phonebook():    
    name = input("Enter name: ")
    phone_number = input("Enter Phone Book: ")
    with open("phonebook.txt", 'w') as file:
        file.write(f"{name}, {phone_number} \n")

def read_from_the_phonebook():
    with open("phonebook.txt", "r") as file:
        row = file.readline()
        name, phonenumber = row.split(",")
        print(f"Name: {name.strip()}, Number: {phonenumber.strip()}")


read_from_the_phonebook()