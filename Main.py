import Parser, Assembler;
#read in .asm
#parse file
#output .hack

def main():
    askForFile = True;
    while (askForFile):
        try:
            fileName = input("Please enter file name to read: ")
            asmFile = open(fileName, 'r')
            askForFile = False
            FileParser = Parser.Parser(asmFile)
            #close file
            asmFile.close()

            #list of commands to be interpreted
            rawCommands = FileParser.getContents

            HackAssembler = Assembler.Assembler(rawCommands, fileName)
            HackAssembler.addUserSymbols()
            HackAssembler.translate()
            HackAssembler.outputFile()
        except:
            print("Error, no such file")

if __name__ == '__main__': 
    main()