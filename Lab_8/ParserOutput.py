class ParserOutput:
    def __init__(self, output_file, input_file, parser):
        self.__output_file = output_file
        self.__input_file = input_file
        self.__parser = parser
        self.tree = []

    def run(self):
        random_list = []
        with open(self.__input_file, 'r') as file:
            for line in file:
                random_list.append(line.strip('\n').split('->')[0])
        result, productionString = self.__parser.parseSequence(random_list)
        if result:
            print("The word is syntactically correct")
            print("Production string: " + str(productionString))

            f = open(self.__output_file, "w")

            parserOutputString = self.__parser.parserOutputString

            for line in parserOutputString:
                f.write(str(line) + '\n')

            table = self.__parser.createParseTree(productionString)
            table.sort(key=lambda x: x.index)

            f.write("Parse tree with father-sibling relation:\n")
            f.write("info | value | father | right sibling\n")
            for entry in table:
                f.write(str(entry) + '\n')
            f.close()
        else:
            print("The word is not syntactically correct")

            f = open(self.__output_file, "w")

            parserOutputString = self.__parser.parserOutputString

            for line in parserOutputString:
                f.write(str(line) + '\n')

            f.close()
