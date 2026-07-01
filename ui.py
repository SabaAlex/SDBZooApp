from entities import Animal
from service import AnimalServices
from exceptions import EmptyExceptions

class UI:
    DEFAULT_AGE = 0

    def __init__(self, service: AnimalServices):
        self.__service = service

    def __print_menu(self):
        print("1. Add animal")
        print("2. Remove animal")
        print("3. Median age")
        print("4. Print all animals")
        print("0. Exit")

    def __validate_age(self, value:str):
        try:
            value = int(value)
        except ValueError:
            return False

        if value < 0 or value > 100:
            return False

        return True

    def __add_animal(self):
        name = input("Enter animal name: ")
        age_str = input("Enter animal's age: ")

        if not self.__validate_age(age_str):
            print("Age must be between 0 and 100")
            return

        age = int(age_str)
        result = self.__service.add_animal(Animal(name, age))
        if result:
            print("Successfully added animal")
        else:
            print("Animal already exists")

    def __remove_animal(self):
        name = input("Enter animal name: ")

        animal = Animal(name, UI.DEFAULT_AGE)
        if self.__service.delete_animal(animal):
            print("Animal successfully removed")
        else:
            print("Animal does not exist")

    def __median_age(self):
        try:
            result = self.__service.average_age()
            print(f"Median age is {result}")
        except EmptyExceptions:
            print("No animals")

    def __print_animals(self):
        animals = self.__service.get_all_animals()

        if len(animals) == 0:
            print("No animals")
            return

        for animal in animals:
            print(animal)

    def run(self):
        running = True
        while running:
            self.__print_menu()
            command = input("Enter your choice: ")
            print(f"Processing {command}")
            if command == "0":
                print("Exiting...")
                running = False
            elif command == "1":
                self.__add_animal()
            elif command == "2":
                self.__remove_animal()
            elif command == "3":
                self.__median_age()
            elif command == "4":
                self.__print_animals()
            else:
                print("Invalid command. Please enter a valid command.")
