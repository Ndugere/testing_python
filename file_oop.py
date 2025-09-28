import csv
import os

filename = 'phonebook.csv'
fieldnames = ['Name', 'Number']

# Check if the file exists
file_exists = os.path.isfile(filename)

# Open the file in append mode
with open(filename, mode='a', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    # If the file doesn't exist, write the header
    if not file_exists:
        writer.writeheader()

    # Example entry to add
    name = input("Enter name: ")
    number = input("Enter number: ")

    # Write the entry
    writer.writerow({'Name': name, 'Number': number})
