from re import match


class TokenIdentifier:
    def __init__(self, lexicInserter, finite_automata_for_identifiers, finite_automata_for_integer_constants):
        self.__lexicInserter = lexicInserter
        self.__finite_automata_for_identifiers = finite_automata_for_identifiers
        self.__finite_automata_for_integer_constants = finite_automata_for_integer_constants

    def get_reserved_words(self):
        return self.__lexicInserter.reservedWords

    def get_operators(self):
        return self.__lexicInserter.operators

    def get_separators(self):
        return self.__lexicInserter.separators

    @staticmethod
    def is_identifier(token) -> bool:
        return match(r'^[a-z](_|[a-zA-Z]|[0-9])*$', token) is not None

    @staticmethod
    def is_numerical_constant(token) -> bool:
        return match(r'^(0|[+-]?[1-9][0-9]*)$|^\'.\'$|^\'.[0-9]*\'$', token) is not None

    @staticmethod
    def is_string_constant(token) -> bool:
        return match(r'"(.*)"', token) is not None

    def get_tokens(self, file):
        pif = []
        st = []
        line_number = 0
        lexically_correct = True
        for line in file:
            line = line.strip()
            separators = []
            i = 0
            number_of_quotes = 0
            while i < len(line):
                for separator in self.get_separators():
                    if separator == line[i]:
                        if separator == '"':
                            number_of_quotes += 1
                            idx2 = line.find('"', i + 1, len(line))
                            if idx2 != -1 and number_of_quotes % 2 != 0:
                                separators.append(line[i])
                                i = idx2 + 1
                        else:
                            separators.append(line[i])
                i += 1
            tokens = []
            for separator in separators:
                if separator == '"':
                    next_separator_index = line.find(separator)
                    if next_separator_index != -1:
                        line = line[next_separator_index + 1: len(line)]
                        next_separator_index1 = line.find(separator)
                        tokens.append('"' + line[next_separator_index:next_separator_index1] + '"')
                        line = line[next_separator_index1 + 1: len(line)]
                else:
                    next_separator_index = line.find(separator)
                    word = line[0:next_separator_index]
                    line = line[next_separator_index + 1:len(line)]
                    if word != '':
                        tokens.append(word)
                    if separator != ' ':
                        tokens.append(separator)
            for w in tokens:
                if w in self.get_separators() + self.get_operators() + self.get_reserved_words():
                    pif.append((w, -1))
                elif self.__finite_automata_for_identifiers.is_sequence_accepted(w) or \
                        self.__finite_automata_for_integer_constants.is_sequence_accepted(w) \
                        or self.is_string_constant(w):
                    if w not in st:
                        pif.append((w, None))
                        st.append(w)
                    elif w in st:
                        pif.append((w, None))
                else:
                    print("Lexical error at line: " + str(line_number) + ", with the unknown token " + str(w))
                    lexically_correct = False
            line_number += 1
        if lexically_correct:
            print("Lexically correct")
        return pif, st
