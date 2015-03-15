import Symbol, Instruction

class Assembler(object):
    """Assembler, has symbols"""
    def __init__(self):
        self.__m_Symbols = list()
        self.__m_Instructions = list()
        #go ahead and populate symbol table
        self.populateSymbols()
        #go ahead and populate instruction table
        self.populateInstructions()

    #string description
    def __str__(self):
        rep = ""
        rep += "Symbols: \n"
        for symbol in self.__m_Symbols:
            rep += "Symbol name: {0} | value: {1}\n".format(symbol.getName, symbol.getValue)
        rep += "Instructions: \n"
        for instruction in self.__m_Instructions:
            rep += "Instruction name: {0} | value: {1}\n".format(instruction.getName, instruction.getValue)
        return rep
    
    #go ahead and populate symbol table
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
        return self.__m_Symbols

    #go ahead and populate instruction table
    def populateInstructions(self):
        self.__m_Instructions.append(Instruction.Instruction('0', '0101010'))
        self.__m_Instructions.append(Instruction.Instruction('1', '0111111'))
        self.__m_Instructions.append(Instruction.Instruction('-1', '0111010'))
        self.__m_Instructions.append(Instruction.Instruction('D', '0001100'))
        self.__m_Instructions.append(Instruction.Instruction('A', '0110000'))
        self.__m_Instructions.append(Instruction.Instruction('M', '1110000'))
        self.__m_Instructions.append(Instruction.Instruction('!D', '0001101'))
        self.__m_Instructions.append(Instruction.Instruction('!A', '0110001'))
        self.__m_Instructions.append(Instruction.Instruction('!M', '1110001'))
        self.__m_Instructions.append(Instruction.Instruction('-D', '0001111'))
        self.__m_Instructions.append(Instruction.Instruction('-A', '0110011'))
        self.__m_Instructions.append(Instruction.Instruction('-M', '1110011'))
        self.__m_Instructions.append(Instruction.Instruction('D+1', '0011111'))
        self.__m_Instructions.append(Instruction.Instruction('A+1', '0110111'))
        self.__m_Instructions.append(Instruction.Instruction('M+1', '1110111'))
        self.__m_Instructions.append(Instruction.Instruction('D-1', '0001110'))
        self.__m_Instructions.append(Instruction.Instruction('A-1', '0110010'))
        self.__m_Instructions.append(Instruction.Instruction('M-1', '1110010'))
        self.__m_Instructions.append(Instruction.Instruction('D+A', '0000010'))
        self.__m_Instructions.append(Instruction.Instruction('D+M', '1000010'))
        self.__m_Instructions.append(Instruction.Instruction('D-A', '0010011'))
        self.__m_Instructions.append(Instruction.Instruction('D-M', '1010011'))
        self.__m_Instructions.append(Instruction.Instruction('A-D', '0000111'))
        self.__m_Instructions.append(Instruction.Instruction('M-D', '1000111'))
        self.__m_Instructions.append(Instruction.Instruction('D&A', '0000000'))
        self.__m_Instructions.append(Instruction.Instruction('D&M', '1000000'))
        self.__m_Instructions.append(Instruction.Instruction('D|A', '0010101'))
        self.__m_Instructions.append(Instruction.Instruction('D|M', '1010101'))



    def getInstructions(self):
        return self.__m_Instructions