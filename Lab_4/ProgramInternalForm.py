class ProgramInternalForm:
    def __init__(self):
        self.__table = []

    def add(self, key, position):
        self.__table.append((key, position))

    def __str__(self):
        result = ""
        for key_position_tuple in self.__table:
            result += key_position_tuple[0] + "->" + str(key_position_tuple[1]) + "\n"
        return result