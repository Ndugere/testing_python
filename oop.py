class Student:
    def __init__(self, name, house):
        if not name:
            raise ValueError("Missing Name")
        self.name = name
        if house not in {"Kitengela", "Nairobi", "Kisumu", "Mombasa", "Eldoret"}:
            raise ValueError("House not in the accepted collection!")
        self.house = house
    
    def __str__(self):
        return f"{self.name} from {self.house}"

def main():
    student = get_student()
    print(student)

def get_student():
    while True:
        name = input("Enter name: ")
        house = input("Enter house: ")
        try:
            return Student(name, house)
        except ValueError as e:
            print(f"{e}")

if __name__ == "__main__":
    main()
