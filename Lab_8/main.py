from Parser import Parser
from ParserOutput import ParserOutput
from grammar import Grammar

if __name__ == '__main__':
    grammar = Grammar.get_grammar_from_file("g3.txt")
    parser = Parser(grammar)

    parserOutput = ParserOutput("out1.txt", "seq.txt", parser)
    parserOutput.run()

    grammar1 = Grammar.get_grammar_from_file("g2.txt")
    parser1 = Parser(grammar1)

    parserOutput1 = ParserOutput("out2.txt", "pif.out", parser1)
    parserOutput1.run()
