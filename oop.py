class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house
    
    def __str__(self):
        return f"{self.name} from {self.house}"
def main():
    student = get_student()
    print(f"{student.name} from {student.house}")

    
def get_student():
    name = input("Enter name: ")
    house = input("Enter house: ")
    return Student(name, house)


if __name__ == "__main__":
    main()