import copy

from Node import Node, NodeHelper


class Parser:
    def __init__(self, grammar):
        self.__grammar = grammar
        self.__productions = self.rearrangeProductions()
        self.__first = self.first()
        self.__follow = self.follow()
        self.__parseTable = self.parseTable()
        self.__input_stack = None
        self.__work_stack = None
        self.__sequence = []
        self.__parserOutputString = []

    @property
    def parserOutputString(self):
        return self.__parserOutputString

    def getNumberOfProduction(self, nonTerminal, prod):
        i = 1
        for p in self.__productions:
            for pp in self.__productions[p]:
                if pp == prod and nonTerminal == p:
                    return i
                i += 1

    def getProductionBasedOnNumber(self, number):
        i = 1
        for p in self.__productions:
            for pp in self.__productions[p]:
                if i == number:
                    return pp
                i += 1
        return None

    def returnProductionWhichIsGeneratingTheTerminal(self, nonterminal, terminal):
        for prod in self.__productions[nonterminal]:
            for elem in prod:
                if terminal in elem:
                    return prod
        for prod in self.__productions[nonterminal]:
            for elem in prod:
                if elem in self.__grammar.get_nonterminals:
                    if '"' + terminal + '"' in self.__first[elem]:
                        return prod

    def returnEpsilonProductionOfNonterminal(self, nonTerminal):
        for prod in self.__productions[nonTerminal]:
            for elem in prod:
                if '"epsilon"' in elem:
                    return prod

    def rearrangeProductions(self):
        productions = self.__grammar.get_productions
        productionsRearranged = dict()
        for nonTerminal in self.__grammar.get_nonterminals:
            productionsRearranged[nonTerminal] = []
        productionsRearranged['simple_declaration'] = [['type', '" "', 'identifier']]
        for nonTerminal in productions:
            if nonTerminal != 'simple_declaration':
                for productionPart in productions[nonTerminal]:
                    current_production_part = []
                    while productionPart.find(' ') != -1:
                        index_space = productionPart.find(' ')
                        current_production_part.append(productionPart[0:index_space])
                        productionPart = productionPart[index_space + 1:len(productionPart)]
                    current_production_part.append(productionPart[0:len(productionPart)])
                    productionsRearranged[nonTerminal].append(current_production_part)
        return productionsRearranged

    def first(self):
        current_first = dict()
        for terminal in self.__grammar.get_terminals:
            current_first[terminal] = [terminal]
        nextSymbolToLookInto = dict()
        for nonTerminal in self.__grammar.get_nonterminals:
            current_first[nonTerminal] = []
            nextSymbolToLookInto[nonTerminal] = []
        # current_first[' '] = [' ']
        for nonTerminal in self.__grammar.get_nonterminals:
            for prod in self.__productions[nonTerminal]:
                if prod[0].strip('"') in self.__grammar.get_terminals:
                    current_first[nonTerminal].append(prod[0])
        for nonTerminal in self.__grammar.get_nonterminals:
            for prodToLookInto in self.__productions[nonTerminal]:
                if prodToLookInto[0].strip('"') not in self.__grammar.get_terminals \
                        and prodToLookInto[0] != nonTerminal \
                        and prodToLookInto[0] not in nextSymbolToLookInto[nonTerminal]:
                    nextSymbolToLookInto[nonTerminal].append(prodToLookInto[0])
        next_first = copy.deepcopy(current_first)

        while True:
            for nonTerminal in self.__grammar.get_nonterminals:
                for nextSymbol in nextSymbolToLookInto[nonTerminal]:
                    for prod in self.__productions[nextSymbol]:
                        if prod[0].strip('"') in self.__grammar.get_terminals and prod[0] not in next_first[
                            nonTerminal]:
                            next_first[nonTerminal].append(prod[0])
            nextSymbolsToLookIntoFirst = dict()
            for nonTerminal in self.__grammar.get_nonterminals:
                nextSymbolsToLookIntoFirst[nonTerminal] = []
            for nonTerminal in self.__grammar.get_nonterminals:
                for eachNext in nextSymbolToLookInto[nonTerminal]:
                    for prodToLookInto in self.__productions[eachNext]:
                        if prodToLookInto[0].strip('"') not in self.__grammar.get_terminals \
                                and prodToLookInto[0] != nonTerminal \
                                and prodToLookInto[0] not in nextSymbolsToLookIntoFirst[nonTerminal]:
                            nextSymbolsToLookIntoFirst[nonTerminal].append(prodToLookInto[0])
            nextSymbolToLookInto = nextSymbolsToLookIntoFirst
            if current_first == next_first:
                break
            else:
                current_first = copy.deepcopy(next_first)
        return next_first

    def follow(self):
        current_follow = dict()
        for nonTerminal in self.__grammar.get_nonterminals:
            current_follow[nonTerminal] = []
        current_follow[self.__grammar.get_starting_symbol] = ['"epsilon"']
        next_follow = copy.deepcopy(current_follow)
        while True:
            for nonTerminal in self.__grammar.get_nonterminals:
                for production in self.__productions:
                    for p in self.__productions[production]:
                        if nonTerminal in p:
                            if p.index(nonTerminal) + 1 != len(p):
                                if p[p.index(nonTerminal) + 1].find('"') != -1:
                                    for element in self.__first[
                                        p[p.index(nonTerminal) + 1][1:len(p[p.index(nonTerminal) + 1]) - 1]]:
                                        if element == '"epsilon"':
                                            for smth in current_follow[production]:
                                                if smth not in next_follow[nonTerminal]:
                                                    next_follow[nonTerminal].append(smth)
                                        else:
                                            for smth in current_follow[nonTerminal]:
                                                if smth not in next_follow[nonTerminal]:
                                                    next_follow[nonTerminal].append(smth)
                                            for smth in self.__first[
                                                p[p.index(nonTerminal) + 1][1:len(p[p.index(nonTerminal) + 1]) - 1]]:
                                                if smth not in next_follow[nonTerminal]:
                                                    next_follow[nonTerminal].append(smth)
                                else:
                                    for element in self.__first[p[p.index(nonTerminal) + 1]]:
                                        if element == '"epsilon"':
                                            for smth in current_follow[production]:
                                                if smth not in next_follow[nonTerminal]:
                                                    next_follow[nonTerminal].append(smth)
                                        else:
                                            for smth in current_follow[nonTerminal]:
                                                if smth not in next_follow[nonTerminal]:
                                                    next_follow[nonTerminal].append(smth)
                                            for smth in self.__first[p[p.index(nonTerminal) + 1]]:
                                                if smth not in next_follow[nonTerminal]:
                                                    next_follow[nonTerminal].append(smth)
                            else:
                                for smth in current_follow[production]:
                                    if smth not in next_follow[nonTerminal]:
                                        next_follow[nonTerminal].append(smth)
            if current_follow == next_follow:
                break
            else:
                current_follow = copy.deepcopy(next_follow)
        return next_follow

    def parseTable(self):
        parseTable = dict()
        for terminal in self.__grammar.get_terminals:
            if terminal != 'epsilon':
                for nonTerminal in self.__grammar.get_nonterminals:
                    parseTable[(nonTerminal, terminal)] = []
                for terminal2 in self.__grammar.get_terminals:
                    if terminal2 != 'epsilon':
                        if terminal2.strip('"') == terminal.strip('"'):
                            parseTable[(terminal2, terminal)] = ['pop']
                        else:
                            parseTable[(terminal2, terminal)] = []
                parseTable[('$', terminal)] = []
                parseTable[(terminal, '$')] = []
        for nonTerminal in self.__grammar.get_nonterminals:
            parseTable[(nonTerminal, '$')] = []
        parseTable[('$', '$')] = ['acc']
        for nonTerminal in self.__grammar.get_nonterminals:
            for terminal in self.__grammar.get_terminals:
                if terminal != 'epsilon':
                    if ('"' + terminal + '"') not in self.__first[nonTerminal]:
                        parseTable[(nonTerminal, terminal)] = ['err']
                    else:
                        parseTable[(nonTerminal, terminal)] = (
                            self.returnProductionWhichIsGeneratingTheTerminal(nonTerminal, terminal),
                            self.getNumberOfProduction(nonTerminal,
                                                       self.returnProductionWhichIsGeneratingTheTerminal(nonTerminal,
                                                                                                         terminal)))
                else:
                    if ('"' + terminal + '"') in self.__first[nonTerminal]:
                        for elem in self.__follow[nonTerminal]:
                            if elem != '"epsilon"':
                                parseTable[(nonTerminal, elem.strip('"'))] = (
                                    self.returnEpsilonProductionOfNonterminal(nonTerminal),
                                    self.getNumberOfProduction(nonTerminal,
                                                               self.returnEpsilonProductionOfNonterminal(nonTerminal)))
                            if elem == '"epsilon"':
                                parseTable[(nonTerminal, '$')] = (
                                    self.returnEpsilonProductionOfNonterminal(nonTerminal),
                                    self.getNumberOfProduction(nonTerminal,
                                                               self.returnEpsilonProductionOfNonterminal(nonTerminal)))
        for i in parseTable:
            if len(parseTable[i]) == 0:
                parseTable[i] = ['err']
        return parseTable

    def parseSequence(self, word):
        self.__input_stack = word
        self.__input_stack.append('$')
        self.__input_stack.reverse()
        self.__work_stack = ['$', self.__grammar.get_starting_symbol]
        self.__sequence = []

        while True:
            self.__parserOutputString.append(copy.deepcopy("input stack:\n" + str(self.__input_stack)))
            self.__parserOutputString.append(copy.deepcopy("work stack:\n" + str(self.__work_stack)))
            self.__parserOutputString.append(copy.deepcopy("production string:\n" + str(self.__sequence)))
            self.__parserOutputString.append('\n')

            if self.__work_stack[-1].strip('"') == ' ':
                self.__work_stack.pop(-1)
                continue

            seq = self.__parseTable[(self.__work_stack[-1].strip('"'), self.__input_stack[-1].strip('"'))]
            if seq == ['acc']:
                break
            elif seq == ['pop']:
                self.__input_stack.pop(-1)
                self.__work_stack.pop(-1)
            elif seq == ['err']:
                self.__parserOutputString.append("ERROR AT SYMBOL: " + self.__input_stack[-1].strip('"'))
                return False, None
            elif ['"epsilon"'] in seq:
                self.__work_stack.pop(-1)
                self.__sequence.append(seq[1])
            else:
                self.__work_stack.pop(-1)
                for i in range(len(seq[0])):
                    self.__work_stack.append(seq[0][len(seq[0]) - i - 1].strip('"'))
                self.__sequence.append(seq[1])

        self.__parserOutputString.append(copy.deepcopy("input stack:\n" + str(self.__input_stack)))
        self.__parserOutputString.append(copy.deepcopy("work stack:\n" + str(self.__work_stack)))
        self.__parserOutputString.append(copy.deepcopy("production string:\n" + str(self.__sequence)))
        self.__parserOutputString.append('\n')

        return True, self.__sequence

    def createParseTree(self, productionString):
        helperNodeList = []
        nodeStack = []
        productionIndex = 0
        nodeNumber = 0

        node = NodeHelper(self.__grammar.get_starting_symbol)
        node.sibling = 0
        nodeNumber += 1
        node.index = nodeNumber

        helperNodeList.append(node)
        nodeStack.append(node)

        maxLevel = -1
        nodesPerLevel = {}

        while productionIndex < len(productionString):
            currentNode = nodeStack[0]
            if currentNode.value.strip('"') in self.__grammar.get_terminals:
                nodeStack.remove(nodeStack[0])
                continue
            production = self.getProductionBasedOnNumber(productionString[productionIndex])
            nodesToAdd = []

            for i in range(0, len(production)):
                child = NodeHelper(production[i])
                child.father = currentNode
                child.level = currentNode.level + 1
                if child.level > maxLevel:
                    maxLevel = child.level

                if child.level in nodesPerLevel:
                    nodesPerLevel[child.level].append(child)
                else:
                    nodesPerLevel[child.level] = [child]

                helperNodeList.append(child)
                nodesToAdd.append(child)

            index = nodeStack.index(currentNode)
            del nodeStack[index]
            for i in range(index, index + len(nodesToAdd)):
                nodeStack.insert(i, nodesToAdd[i])

            productionIndex += 1

        currentLevel = 0
        currentIndex = 1

        while currentLevel <= maxLevel:
            for i in range(len(helperNodeList)):
                if helperNodeList[i].level == currentLevel:
                    helperNodeList[i].index = currentIndex
                    currentIndex += 1
            currentLevel += 1

        for level in nodesPerLevel:
            for i in range(len(nodesPerLevel[level])):
                if i == len(nodesPerLevel[level]) - 1:
                    nodesPerLevel[level][i].sibling = 0
                else:
                    if nodesPerLevel[level][i].father == nodesPerLevel[level][i + 1].father \
                            or nodesPerLevel[level][i].father.sibling == nodesPerLevel[level][i + 1].father.index:
                        nodesPerLevel[level][i].sibling = nodesPerLevel[level][i + 1].index
                    else:
                        nodesPerLevel[level][i].sibling = 0

        nodeList = []

        for helperNode in helperNodeList:
            node = Node(helperNode.value)
            node.sibling = helperNode.sibling
            node.index = helperNode.index
            if helperNode.father is not None:
                node.father = helperNode.father.index
            else:
                node.father = 0
            nodeList.append(node)

        return nodeList

    def testParsingTable(self):
        print(self.__parseTable[('S', 'a')])
        print(self.__parseTable[('a', 'a')])
        print(self.__parseTable[('D', '(')])
        print(self.__parseTable[('A', ')')])
        print(self.__parseTable[('C', '*')])
        print(self.__parseTable[('a', '*')])
        print(self.__parseTable[('$', '$')])

    def testFirst(self):
        print("FIRST:")
        print(self.__first['S'])
        print(self.__first['A'])
        print(self.__first['B'])
        print(self.__first['C'])
        print(self.__first['D'])
        print(self.__first['a'])

    def testFollow(self):
        print("FOLLOW:")
        print(self.__follow['S'])
        print(self.__follow['A'])
        print(self.__follow['B'])
        print(self.__follow['C'])
        print(self.__follow['D'])
