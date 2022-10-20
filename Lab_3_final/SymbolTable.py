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
        # if the key already stored in the ST -> raise an error
        if self.key_exists(key):
            raise Exception("The key already exists")
        # if not already stored -> store it
        self.__table[self.hash(key)].append(key)

    def key_exists(self, key):
        """
        Checks if the given key exists in the ST
        :param key: The key for which the existence is checked
        :return: True, if it is present in the ST. False, otherwise.
        """
        return key in self.__table[self.hash(key)]

    def remove(self, key):
        """
        Removes an element from the ST
        :param key: the elem we want to remove
        :return: -
        :raise: exception, if the element is not present in the ST
        """
        if self.key_exists(key):
            self.__table[self.hash(key)].remove(key)
        else:
            raise Exception("Key not found in the symbol table")

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
