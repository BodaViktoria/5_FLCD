class ProgramInternalForm:
    def __init__(self):
        self.__table = []

    def add(self, key, position):
        self.__table.append((key, position))

    def __str__(self):
        result = ""
        for tuple in self.__table:
            result += tuple[0] + "->" + str(tuple[1]) + "\n"
        return result