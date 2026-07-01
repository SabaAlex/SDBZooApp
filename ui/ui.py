from domain.animal import Animal
from domain.caretaker import Caretaker
from service.animal_service import AnimalService
from domain.exceptions import EmptyExceptions
from service.caretaker_service import CaretakerService
from service.statistics_service import StatisticsService


class UI:
    DEFAULT_AGE = 0

    def __init__(self, animal_service: AnimalService, caretaker_service: CaretakerService, statistics_service: StatisticsService):
        self.__animal_service = animal_service
        self.__caretaker_service = caretaker_service
        self.__statistics_service = statistics_service

    def __print_menu(self):
        print("1. Add animal")
        print("2. Remove animal")
        print("3. Median age of animals")
        print("4. Print all animals")
        print("5. Add caretaker")
        print("6. Remove caretaker")
        print("7. Median age of caretakers")
        print("8. Print all caretakers")
        print("9. Animals without caretaker")
        print("0. Exit")

    def __validate_age(self, value:str):
        try:
            value = int(value)
        except ValueError:
            return False

        if value < 0 or value > 100:
            return False

        return True

    def __add_caretaker(self):
        name = input("Enter caretaker name: ")
        age_str = input("Enter caretaker's age: ")
        animal_name = input("Enter caretaker's animal: ")

        if not self.__validate_age(age_str):
            print("Age must be between 0 and 100")
            return

        age = int(age_str)
        animal = self.__animal_service.get_animal(animal_name)
        if animal is None:
            print(f"Animal named {animal_name} does not exist!")
        result = self.__caretaker_service.add_caretaker(Caretaker(name, age, animal))
        if result:
            print("Successfully added caretaker")
        else:
            print("Caretaker already exists")

    def __remove_caretaker(self):
        name = input("Enter caretaker name: ")

        caretaker = Caretaker(name, UI.DEFAULT_AGE, None)
        if self.__caretaker_service.delete_caretaker(caretaker):
            print("Caretaker successfully removed")
        else:
            print("Caretaker does not exist")

    def __median_age_caretakers(self):
        try:
            result = self.__statistics_service.average_age_caretakers()
            print(f"Median age of all caretakers is {result}")
        except EmptyExceptions:
            print("No caretakers")

    def __print_caretakers(self):
        caretakers = self.__caretaker_service.get_all_caretakers()

        if len(caretakers) == 0:
            print("No caretakers")
            return

        for caretaker in caretakers:
            print(caretaker)

    def __print_animals_without_caretakers(self):
        animals_without_caretaker = self.__statistics_service.animals_without_caretaker()
        for animal in animals_without_caretaker:
            print(animal)

    def __add_animal(self):
        name = input("Enter animal name: ")
        age_str = input("Enter animal's age: ")

        if not self.__validate_age(age_str):
            print("Age must be between 0 and 100")
            return

        age = int(age_str)
        result = self.__animal_service.add_animal(Animal(name, age))
        if result:
            print("Successfully added animal")
        else:
            print("Animal already exists")

    def __remove_animal(self):
        name = input("Enter animal name: ")

        animal = Animal(name, UI.DEFAULT_AGE)
        if self.__animal_service.delete_animal(animal):
            print("Animal successfully removed")
        else:
            print("Animal does not exist")

    def __median_age_animals(self):
        try:
            result = self.__statistics_service.average_age_animals()
            print(f"Median age is {result}")
        except EmptyExceptions:
            print("No animals")

    def __print_animals(self):
        animals = self.__animal_service.get_all_animals()

        if len(animals) == 0:
            print("No animals")
            return

        for animal in animals:
            print(animal)

    def run(self):
        running = True
        while running:
            try:
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
                    self.__median_age_animals()
                elif command == "4":
                    self.__print_animals()
                elif command == "5":
                    self.__add_caretaker()
                elif command == "6":
                    self.__remove_caretaker()
                elif command == "7":
                    self.__median_age_caretakers()
                elif command == "8":
                    self.__print_caretakers()
                elif command == "9":
                    self.__print_animals_without_caretakers()
                else:
                    print("Invalid command. Please enter a valid command.")
            except Exception as e:
                print('An unknown error has occurred', e)
