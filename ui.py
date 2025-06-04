from service import Animal
from exceptions import CustomException
from service import Service


class UI:
    def __init__(self, service: Service):
        self.__service = service
        self.__commands = {
            "1": self.__add_animal,
            "2": self.__delete_animal,
            "3": self.__average_animal_age,
            "4": self.__show_all_animals,
        }

    def __print_menu(self):
        print("1.Add animal")
        print("2.Delete animal")
        print("3.Average zoo age")
        print("4.Show all animals")
        print("0.Exit")

    def __validate_age(self, age):
        try:
            int(age)
        except ValueError:
            raise CustomException('Animal age is not a number!')


    def __add_animal(self):
        name = input("Animal name: ")
        age = input("Animal age: ")
        self.__validate_age(age)
        self.__service.add_animal(Animal(name, int(age)))
        print('Animal added!')

    def __delete_animal(self):
        name = input("Animal to delete name: ")
        age = input("Animal to delete age: ")
        self.__validate_age(age)
        self.__service.delete_animal(Animal(name, int(age)))
        print('Animal deleted!')

    def __show_all_animals(self):
        for animal in self.__service.get_all_animals():
            print(animal)


    def __average_animal_age(self):
        average_age = round(self.__service.average_age(), 2)
        print(f'The average age of all the animals is {average_age}')

    def run(self):
        while True:
            self.__print_menu()
            try:
                command = input("Choose the command:").strip()
                # actions[command]()
                if command == "0":
                    return
                if command in self.__commands:
                    self.__commands[command]()
                else:
                    print('Command does not exist!')
            except CustomException as error:
                print(error)