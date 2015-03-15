import Symbol

class Assembler(object):
    """Assembler, has symbols"""
    def __init__(self):
        self.__m_Symbols = list()

    #string description
    def __str__(self):
        rep = ""
        for symbol in self.__m_Symbols:
            rep += "Symbol name: {0} | value: {1}\n".format(symbol.getName, symbol.getValue)
        return rep

    def populateSymbols(self):
        self.__m_Symbols.append(Symbol.Symbol('SP', 0))
        self.__m_Symbols.append(Symbol.Symbol('LCL', 1))
        self.__m_Symbols.append(Symbol.Symbol('ARG', 2))
        self.__m_Symbols.append(Symbol.Symbol('THIS', 3))
        self.__m_Symbols.append(Symbol.Symbol('THAT', 4))
        self.__m_Symbols.append(Symbol.Symbol('R0', 0))
        self.__m_Symbols.append(Symbol.Symbol('R1', 1))
        self.__m_Symbols.append(Symbol.Symbol('R2', 2))
        self.__m_Symbols.append(Symbol.Symbol('R3', 3))
        self.__m_Symbols.append(Symbol.Symbol('R4', 4))
        self.__m_Symbols.append(Symbol.Symbol('R5', 5))
        self.__m_Symbols.append(Symbol.Symbol('R6', 6))
        self.__m_Symbols.append(Symbol.Symbol('R7', 7))
        self.__m_Symbols.append(Symbol.Symbol('R8', 8))
        self.__m_Symbols.append(Symbol.Symbol('R9', 9))
        self.__m_Symbols.append(Symbol.Symbol('R10', 10))
        self.__m_Symbols.append(Symbol.Symbol('R11', 11))
        self.__m_Symbols.append(Symbol.Symbol('R12', 12))
        self.__m_Symbols.append(Symbol.Symbol('R13', 13))
        self.__m_Symbols.append(Symbol.Symbol('R14', 14))
        self.__m_Symbols.append(Symbol.Symbol('R15', 15))
        self.__m_Symbols.append(Symbol.Symbol('SCREEN', 16384))
        self.__m_Symbols.append(Symbol.Symbol('KBD', 24576))

    def getSymbols(self):
        return self.__m_Symbols;