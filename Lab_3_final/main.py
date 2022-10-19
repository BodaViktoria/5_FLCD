from re import match

from LexicInserter import LexicInserter
from SymbolTable import SymbolTable

if __name__ == '__main__':
    sc = LexicInserter()
    print("separators:", sc.separators)
    print("operators:", sc.operators)
    print("reserved words:", sc.reservedWords)

    symbolTable = SymbolTable(6)
    symbolTable.insert("a")
    symbolTable.insert("b")
    symbolTable.insert("c")
    symbolTable.insert("the minimum number is:")

    print(symbolTable.__str__())

