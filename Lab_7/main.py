from Parser import Parser
from grammar import Grammar

if __name__ == '__main__':
    grammar = Grammar.get_grammar_from_file("g3.txt")
    parser = Parser(grammar)
    parser.testFirst()
    print('------------')
    parser.testFollow()
    print('------------')
    parser.testParsingTable()

    print(parser.parseSequence(['a', '*', '(', 'a', '+', 'a', ')']))
    print(parser.parseSequence(['a', '*', '(', 'a', '+', 'a']))

