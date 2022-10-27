class Scanner:

    def __init__(self, symbolTable, programInternalForm, tokenIdentifier):
        self.ST = symbolTable
        self.PIF = programInternalForm
        self.tokenIdentifier = tokenIdentifier

    def compute_results(self, file_name: str):
        with open(file_name, 'r') as file:
            pif, st = self.tokenIdentifier.get_tokens(file)
        for token in st:
            self.ST.insert(token)
        for token in pif:
            if token[1] == -1:
                self.PIF.add(token[0], token[1])
            else:
                self.PIF.add(token[0], self.ST.return_index(token[0]))
        with open('st.out', 'w') as writer:
            writer.write(str(self.ST))
        with open('pif.out', 'w') as writer:
            writer.write(str(self.PIF))