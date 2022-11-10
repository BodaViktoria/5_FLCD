from FiniteAutomata import FiniteAutomata
from LexicInserter import LexicInserter
from ProgramInternalForm import ProgramInternalForm
from Scanner import Scanner
from SymbolTable import SymbolTable
from TokenIdentifier import TokenIdentifier

if __name__ == '__main__':
    lexicInserter = LexicInserter()
    symtable = SymbolTable(6)
    programInternalForm = ProgramInternalForm()
    finite_automata_for_identifiers = FiniteAutomata("identifiers_fa.txt")
    finite_automata_for_integer_constants = FiniteAutomata("integer_constant_fa.txt")
    tokenIdentifier = TokenIdentifier(lexicInserter, finite_automata_for_identifiers,
                                      finite_automata_for_integer_constants)

    scanner = Scanner(symtable, programInternalForm, tokenIdentifier)
    scanner.compute_results("p1err.txt")
    print('\n')

    fa = FiniteAutomata("fa.txt")
    print(fa,'\n')
    sequence1 = "101"
    if fa.is_sequence_accepted(sequence1):
        print("Sequence " + str(sequence1) + " accepted")
    else:
        print("Sequence " + str(sequence1) + " not accepted")

    sequence1 = "1010"
    if fa.is_sequence_accepted(sequence1):
        print("Sequence " + str(sequence1) + " accepted")
    else:
        print("Sequence " + str(sequence1) + " not accepted")

    sequence1 = "10"
    if fa.is_sequence_accepted(sequence1):
        print("Sequence " + str(sequence1) + " accepted")
    else:
        print("Sequence " + str(sequence1) + " not accepted")

    sequence1 = "11"
    if fa.is_sequence_accepted(sequence1):
        print("Sequence " + str(sequence1) + " accepted")
    else:
        print("Sequence " + str(sequence1) + " not accepted")

    sequence1 = "10111"
    if fa.is_sequence_accepted(sequence1):
        print("Sequence " + str(sequence1) + " accepted")
    else:
        print("Sequence " + str(sequence1) + " not accepted")
