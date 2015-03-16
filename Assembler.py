import Instruction

class Assembler(object):
    """Assembler, has symbols"""
    #constructor
    def __init__(self, commands):
        #object lists
        self.__m_Symbols = list()
        self.__m_Comps = list()
        self.__m_Dests = list()
        self.__m_Jumps = list()
        #end objects

        #holds raw commands
        self.__m_rawCommands = commands
        #final translated commands
        self.__m_translated = list()
        #if A instruction prepend 0; if C instruction prepend 111
        self.__m_preA = '0'
        self.__m_preC = '111'

        #calls
        #go ahead and populate symbol table
        self.populateSymbols()
        #go ahead and populate comp table
        self.populateComps()
        #go ahead and populate dests table
        self.populateDests()
        #go ahead and populate jump table
        self.populateJumps()

    #translate the raw commands into binary
    def translate(self):
        for line in self.__m_rawCommands:
            if (self.isA(line)):
                #translate into binary and add a 0 at beginning
                self.__m_translated.append(self.__m_preA + self.toBinary(line[1:]))
        return self.__m_translated
    
    #
    #   Checkers
    #

    #check if line represents a symbol
    def isSymbol(self, line):
        if (line[0] == '@') and (line[1:] in self.__m_Symbols):
            return True
        return False
    #check if line represents a label
    def isLabel(self, line):
        if line[0] == '(' and line[-1] == ')':
            return True
        return False
    #check if line is an A instruction
    def isA(self, line):
        if (line[0] == '@') and (not self.isSymbol(line)):
            return True
    
        
    #
    # Helpers, and Tables construction
    #

    #get 15 digit binary
    @staticmethod
    def toBinary(integer):
        prepend = ''
        binary = "{0:b}".format(int(integer))
        if (len(binary) != 15):
            size = 15 - len(binary)
        for i in range(size):
            prepend += '0'
        return prepend+binary

    #string description
    def __str__(self):
        rep = ""
        rep += "Symbols: \n"
        for symbol in self.__m_Symbols:
            rep += "Symbol name: {0} | value: {1}\n".format(symbol.getName, symbol.getValue)
        rep += "Comps: \n"
        for comp in self.__m_Comps:
            rep += "Comp name: {0} | value: {1}\n".format(comp.getName, comp.getValue)
        rep += "Destinations: \n"
        for dest in self.__m_Dests:
            rep += "Dest name: {0} | value: {1}\n".format(dest.getName, dest.getValue)
        rep += "Jumps: \n"
        for jump in self.__m_Jumps:
            rep += "Jump name: {0} | value: {1}\n".format(jump.getName, jump.getValue)
        return rep
    
    #go ahead and populate symbol table
    def populateSymbols(self):
        #labels
        self.__m_Symbols.append(Instruction.Instruction('SP', 0))
        self.__m_Symbols.append(Instruction.Instruction('LCL', 1))
        self.__m_Symbols.append(Instruction.Instruction('ARG', 2))
        self.__m_Symbols.append(Instruction.Instruction('THIS', 3))
        self.__m_Symbols.append(Instruction.Instruction('THAT', 4))
        self.__m_Symbols.append(Instruction.Instruction('R0', 0))
        self.__m_Symbols.append(Instruction.Instruction('R1', 1))
        self.__m_Symbols.append(Instruction.Instruction('R2', 2))
        self.__m_Symbols.append(Instruction.Instruction('R3', 3))
        self.__m_Symbols.append(Instruction.Instruction('R4', 4))
        self.__m_Symbols.append(Instruction.Instruction('R5', 5))
        self.__m_Symbols.append(Instruction.Instruction('R6', 6))
        self.__m_Symbols.append(Instruction.Instruction('R7', 7))
        self.__m_Symbols.append(Instruction.Instruction('R8', 8))
        self.__m_Symbols.append(Instruction.Instruction('R9', 9))
        self.__m_Symbols.append(Instruction.Instruction('R10', 10))
        self.__m_Symbols.append(Instruction.Instruction('R11', 11))
        self.__m_Symbols.append(Instruction.Instruction('R12', 12))
        self.__m_Symbols.append(Instruction.Instruction('R13', 13))
        self.__m_Symbols.append(Instruction.Instruction('R14', 14))
        self.__m_Symbols.append(Instruction.Instruction('R15', 15))
        self.__m_Symbols.append(Instruction.Instruction('SCREEN', 16384))
        self.__m_Symbols.append(Instruction.Instruction('KBD', 24576))

    #go ahead and populate instruction table
    def populateComps(self):
        #comp
        self.__m_Comps.append(Instruction.Instruction('0', '0101010'))
        self.__m_Comps.append(Instruction.Instruction('1', '0111111'))
        self.__m_Comps.append(Instruction.Instruction('-1', '0111010'))
        self.__m_Comps.append(Instruction.Instruction('D', '0001100'))
        self.__m_Comps.append(Instruction.Instruction('A', '0110000'))
        self.__m_Comps.append(Instruction.Instruction('M', '1110000'))
        self.__m_Comps.append(Instruction.Instruction('!D', '0001101'))
        self.__m_Comps.append(Instruction.Instruction('!A', '0110001'))
        self.__m_Comps.append(Instruction.Instruction('!M', '1110001'))
        self.__m_Comps.append(Instruction.Instruction('-D', '0001111'))
        self.__m_Comps.append(Instruction.Instruction('-A', '0110011'))
        self.__m_Comps.append(Instruction.Instruction('-M', '1110011'))
        self.__m_Comps.append(Instruction.Instruction('D+1', '0011111'))
        self.__m_Comps.append(Instruction.Instruction('A+1', '0110111'))
        self.__m_Comps.append(Instruction.Instruction('M+1', '1110111'))
        self.__m_Comps.append(Instruction.Instruction('D-1', '0001110'))
        self.__m_Comps.append(Instruction.Instruction('A-1', '0110010'))
        self.__m_Comps.append(Instruction.Instruction('M-1', '1110010'))
        self.__m_Comps.append(Instruction.Instruction('D+A', '0000010'))
        self.__m_Comps.append(Instruction.Instruction('D+M', '1000010'))
        self.__m_Comps.append(Instruction.Instruction('D-A', '0010011'))
        self.__m_Comps.append(Instruction.Instruction('D-M', '1010011'))
        self.__m_Comps.append(Instruction.Instruction('A-D', '0000111'))
        self.__m_Comps.append(Instruction.Instruction('M-D', '1000111'))
        self.__m_Comps.append(Instruction.Instruction('D&A', '0000000'))
        self.__m_Comps.append(Instruction.Instruction('D&M', '1000000'))
        self.__m_Comps.append(Instruction.Instruction('D|A', '0010101'))
        self.__m_Comps.append(Instruction.Instruction('D|M', '1010101'))

    #populate destinations
    def populateDests(self):
        #dest
        self.__m_Dests.append(Instruction.Instruction('null', '000'))
        self.__m_Dests.append(Instruction.Instruction('M', '001'))
        self.__m_Dests.append(Instruction.Instruction('D', '010'))
        self.__m_Dests.append(Instruction.Instruction('MD', '011'))
        self.__m_Dests.append(Instruction.Instruction('A', '100'))
        self.__m_Dests.append(Instruction.Instruction('AM', '101'))
        self.__m_Dests.append(Instruction.Instruction('AD', '110'))
        self.__m_Dests.append(Instruction.Instruction('AMD', '111'))

    #populate jumps
    def populateJumps(self):
        #jumps
        self.__m_Jumps.append(Instruction.Instruction('null', '000'))
        self.__m_Jumps.append(Instruction.Instruction('JGT', '001'))
        self.__m_Jumps.append(Instruction.Instruction('JEQ', '010'))
        self.__m_Jumps.append(Instruction.Instruction('JGE', '011'))
        self.__m_Jumps.append(Instruction.Instruction('JLT', '100'))
        self.__m_Jumps.append(Instruction.Instruction('JNE', '101'))
        self.__m_Jumps.append(Instruction.Instruction('JLE', '110'))
        self.__m_Jumps.append(Instruction.Instruction('JMP', '111'))

    def getSymbols(self):
        return self.__m_Symbols

    def getComps(self):
        return self.__m_Comps

    def getJumps(self):
        return self.__m_Jumps

    def getDests(self):
        return self.__m_Dests