class Repository:
    def __init__(self, entities_list):
        self.__entities_list = entities_list

    def __entity_exists(self, entity_to_find) -> bool:
        for entity in self.__entities_list:
            if entity == entity_to_find:
                return True
        return False

    def __find_position_of_entity(self, entity_to_find):
        entities = self.__entities_list
        for index in range(len(entities)):
            entity = entities[index]
            if entity == entity_to_find:
                return index

        return None

    def create(self, entity) -> bool:
        if self.__entity_exists(entity):
            return False
        self.__entities_list.append(entity)
        return True

    def delete(self, entity) -> bool:
        position = self.__find_position_of_entity(entity)
        if position is None:
            return False
        del self.__entities_list[position]
        return True

    def read(self):
        return self.__entities_list

