from entities import Animal
from exceptions import CustomException


class Service:
    def __init__(self):
        self.__animal_list = [Animal('Rex', 2), Animal('Luna', 5)]

    def add_animal(self, new_animal: Animal):
        """
        This adds an animal to the animal list
        :param new_animal: the animal to be added (Animal)
        """
        for animal in self.__animal_list:
            if animal == new_animal:
                raise CustomException(f'The animal {new_animal} already exists!')
        self.__animal_list.append(new_animal)

    def delete_animal(self, animal_to_delete):
        """
        Deletes an animal from the animal list
        :param animal_to_delete: Animal to delete from in the list (Animal)
        """
        animal_position = self.__get_animal_position(animal_to_delete)
        if animal_position is None:
            raise CustomException(f'The animal {animal_to_delete} does not exist!')
        del self.__animal_list[animal_position]

    def get_all_animals(self):
        """
        Returns the list containing all the animals
        :return: The list of all the animals (list)
        """
        return self.__animal_list

    def average_age(self):
        """
        Returns the average of all the animals in the list
        :return: The average age of all the animals (float)
        """
        sum = 0
        for animal in self.__animal_list:
            sum += animal.get_age()
        average_age = sum / len(self.__animal_list)
        return average_age

    def __get_animal_position(self, animal_to_find):
        """
        Returns the position of a animal in the animal list, None if it doesn't exist
        :param animal_to_find: Animal to search for in the list (Animal)
        :return: The position of the animal if it is in the list (int), otherwise None
        """
        for i in range(len(self.__animal_list)):
            if self.__animal_list[i] == animal_to_find:
                return i
        return None
