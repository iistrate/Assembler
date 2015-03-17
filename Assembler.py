import Instruction

class Assembler(object):
    """Assembler, has symbols"""
    #constructor
    def __init__(self, commands, fileName):
        #object lists
        self.__m_Symbols = list()
        self.__m_Comps = list()
        self.__m_Dests = list()
        self.__m_Jumps = list()
        #end objects

        self.__m_rom = 0
        self.__m_ram = 16
        
        #filename renamed
        self.__m_FileName = fileName.split('.')[0] + '.hack'

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

    #part of pass 1
    def addUserLabels(self):
        for line in self.__m_rawCommands:
            if (self.isLabel(line)):
                #cut out first and last ()
                name = line[1:-1]
                #append label and rom to label table
                self.__m_Symbols.append((Instruction.Instruction(name, self.__m_rom)))
            else:
                self.__m_rom += 1
    #essentially pass 1
    def addUserSymbols(self):
        self.addUserLabels()
        #user defined symbols (check on address start and increment)
        for line in self.__m_rawCommands:
            name = line[1:];
            if self.isA(line) and (not name.isdigit()) and (not self.isNameInTable(name, self.__m_Symbols)):
                #test if symbol is added at the right address
                #print("symbol is {0}, address is {1}".format(name, self.__m_ram))
                #end test
                self.__m_Symbols.append(Instruction.Instruction(name, self.__m_ram))
                self.__m_ram += 1 
                       

    #translate the raw commands into binary aka pass2
    def translate(self):
        for line in self.__m_rawCommands:
            #if A instruction
            if (self.isA(line)):
                #everything after @
                value = line[1:]
                #integer values
                if (value.isdigit()):
                    #translate into binary and add a 0 at beginning
                    self.__m_translated.append(self.__m_preA + self.toBinary(line[1:]))
                #variable integer value
                else:
                    name = value
                    #get integer value from symbol table
                    value = self.getValueByName(name, self.__m_Symbols)
                    self.__m_translated.append(self.__m_preA + self.toBinary(value))
                self.__m_rom += 1
            #if C instruction
            else:
                if (not self.isLabel(line)):
                    if ';' or '=' in line:
                        translated = self.translateC(line)
                        a = translated[0]
                        comp = translated[1]
                        dest = translated[2]
                        jump = translated[3]              
                        self.__m_translated.append('{0}{1}{2}{3}{4}'.format(self.__m_preC, a, comp, dest, jump))
                        self.__m_rom += 1
        return self.__m_translated
    
    #check if line represents a label
    def isLabel(self, line):
        if line[0] == '(' and line[-1] == ')':
            return True
        return False

    #check if line is an A instruction
    def isA(self, line):
        if '@' in line:
            return True
        return False
    
    #if line is a C instruction
    def translateC(self, line):
        a = comp = dest = jump = ''
        #get jump portion and comp
        if ';' in line:
            #get index where the jmp begins
            index = line.find(';')
            #get jump type
            jumpName = line[index+1:]
            #see if there's an M in comp part
            if 'M' in line[:index]: a = '1'
            #get binary representation
            jump = self.getValueByName(jumpName, self.__m_Jumps)
            compName = line[:index]
            comp = self.getValueByName(compName, self.__m_Comps)
        elif '=' in line:
            #get index where dest begins
            index = line.find('=')
            #get destination type
            destName = line[0:index]
            compName = line[index+1:]
            #see if there's an M in comp part
            if 'M' in line[index:]: a = '1'
            #get binary representation
            comp = self.getValueByName(compName, self.__m_Comps)
            dest = self.getValueByName(destName, self.__m_Dests)

        if not comp: comp = '000000'
        if not dest: dest = '000'
        if not jump: jump = '000'
        if not a: a = '0'

        return (a, comp, dest, jump)

    def getValueByName(self, name, list):
        #find value by name from table 
        for item in list:
            if item.getName == name:
                return item.getValue
    
    def isNameInTable(self, name, list):
        #find if name in table
        for item in list:
            if item.getName == name:
                return True
        return False

    #output translated commands to file
    def outputFile(self):
        output = open(self.__m_FileName, 'w')
        for line in self.__m_translated:
            output.writelines('{0}\n'.format(line))
        output.close()

    #
    # Helpers, and Tables construction
    #

    #get 15 digit binary
    @staticmethod
    def toBinary(integer):
        prepend = ''
        binary = "{0:b}".format(int(integer))
        #if the length of binary < 15 prepend 0's
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
    
    #go ahead and populate symbol table with known values
    def populateSymbols(self):
        #symbols we know of
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
        self.__m_Comps.append(Instruction.Instruction('0', '101010'))
        self.__m_Comps.append(Instruction.Instruction('1', '111111'))
        self.__m_Comps.append(Instruction.Instruction('-1', '111010'))
        self.__m_Comps.append(Instruction.Instruction('D', '001100'))
        self.__m_Comps.append(Instruction.Instruction('A', '110000'))
        self.__m_Comps.append(Instruction.Instruction('M', '110000'))
        self.__m_Comps.append(Instruction.Instruction('!D', '001101'))
        self.__m_Comps.append(Instruction.Instruction('!A', '110001'))
        self.__m_Comps.append(Instruction.Instruction('!M', '110001'))
        self.__m_Comps.append(Instruction.Instruction('-D', '001111'))
        self.__m_Comps.append(Instruction.Instruction('-A', '110011'))
        self.__m_Comps.append(Instruction.Instruction('-M', '110011'))
        self.__m_Comps.append(Instruction.Instruction('D+1', '011111'))
        self.__m_Comps.append(Instruction.Instruction('A+1', '110111'))
        self.__m_Comps.append(Instruction.Instruction('M+1', '110111'))
        self.__m_Comps.append(Instruction.Instruction('D-1', '001110'))
        self.__m_Comps.append(Instruction.Instruction('A-1', '110010'))
        self.__m_Comps.append(Instruction.Instruction('M-1', '110010'))
        self.__m_Comps.append(Instruction.Instruction('D+A', '000010'))
        self.__m_Comps.append(Instruction.Instruction('D+M', '000010'))
        self.__m_Comps.append(Instruction.Instruction('D-A', '010011'))
        self.__m_Comps.append(Instruction.Instruction('D-M', '010011'))
        self.__m_Comps.append(Instruction.Instruction('A-D', '000111'))
        self.__m_Comps.append(Instruction.Instruction('M-D', '000111'))
        self.__m_Comps.append(Instruction.Instruction('D&A', '000000'))
        self.__m_Comps.append(Instruction.Instruction('D&M', '000000'))
        self.__m_Comps.append(Instruction.Instruction('D|A', '010101'))
        self.__m_Comps.append(Instruction.Instruction('D|M', '010101'))

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