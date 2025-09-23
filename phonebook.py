import csv

name = input("Enter Name: ")
number = input("Enter Phone Number: ")

with open("phonebook.csv", "a") as file:
    file.write(f"{name}, {number}\n")
