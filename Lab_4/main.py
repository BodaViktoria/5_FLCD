from re import match

from LexicInserter import LexicInserter
from ProgramInternalForm import ProgramInternalForm
from Scanner import Scanner
from SymbolTable import SymbolTable
from TokenIdentifier import TokenIdentifier

if __name__ == '__main__':
    lexicInserter = LexicInserter()
    symtable = SymbolTable(6)
    programInternalForm = ProgramInternalForm()
    tokenIdentifier = TokenIdentifier(lexicInserter)

    scanner = Scanner(symtable, programInternalForm, tokenIdentifier)
    scanner.compute_results("p1.txt")
