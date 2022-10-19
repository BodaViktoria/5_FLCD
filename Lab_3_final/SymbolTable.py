class SymbolTable:
    def __init__(self, size):
        self.__size = size
        self.__table = [[] for _ in range(self.__size)]

    def insert(self, key):
        """
        Inserts an element in the ST
        :param key: the key we want to insert
        :return: position of the key in the ST
        """
        # if the key already stored in the ST -> return the index
        if key in self.__table[self.hash(key)]:
            return self.return_index(key)
        # if not already stored -> store it and return the index
        self.__table[self.hash(key)].append(key)
        return self.return_index(key)

    def remove(self, key):
        """
        Removes an element from the ST
        :param key: the elem we want to remove
        :return: -
        """
        index = self.hash(key)
        self.__table[index].remove(key)

    def return_index(self, key):
        """
        Return the index of the given key in the ST and in the list of symbols
        :param key: the key we search the index for
        :return: the index of the given key in the ST and in the list of symbols
        """
        return self.hash(key), self.__table[self.hash(key)].index(key)

    def hash(self, key):
        """
        Returns the hash index of a key
        :param key: the key we search the hash value for
        :return: the hash value / index
        """
        return sum(ord(ch) for ch in key) % self.__size

    def __str__(self) -> str:
        representation = ""
        for i in range(self.__size):
            representation += str(i) + " -> " + str(self.__table[i]) + "\n"
        return representation
