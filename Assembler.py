
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
        except:
            print("Error, no such file")
    #close file
    asmFile.close()

if __name__ == '__main__': 
    main()