class LexicInserter:

    def __init__(self):
        self.separators = []
        self.operators = []
        self.reservedWords = []
        self.classify()

    def classify(self) -> None:
        with open('token.txt', 'r') as f:
            f.readline()
            for i in range(12):
                separator = f.readline().strip()
                if separator == "space":
                    separator = " "
                self.separators.append(separator)
            for i in range(13):
                self.operators.append(f.readline().strip())
            # for i in range(72):
            #     self.reservedWords.append(f.readline().strip())
            for i in range(10):
                self.reservedWords.append(f.readline().strip())
