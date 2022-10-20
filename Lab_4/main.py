from re import match

from LexicInserter import LexicInserter
from SymbolTable import SymbolTable

if __name__ == '__main__':
    sc = LexicInserter()
    print("separators:", sc.separators)
    print("operators:", sc.operators)
    print("reserved words:", sc.reservedWords)

    symbolTable = SymbolTable(6)

    try:
        symbolTable.insert("a")
        symbolTable.insert("b")
        symbolTable.insert("c")
        symbolTable.insert("the minimum number is:")
    except Exception as err:
        print(err)

    try:
        symbolTable.insert("c")
    except Exception as err:
        print(err)

    assert symbolTable.hash("a"), 1
    assert symbolTable.hash("b"), 2
    assert symbolTable.hash("c"), 3
    assert symbolTable.hash("the minimum number is:"), 2

    print(symbolTable.__str__())

    symbolTable.remove("b")

    try:
        symbolTable.remove("b")
        assert symbolTable.hash("b"), 2
    except Exception as err:
        print(err)

    assert symbolTable.hash("the minimum number is:"), 2

