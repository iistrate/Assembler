class Parser(object):
    """File parser"""
    def __init__(self, file):
        self.__m_file = file
        self.__m_contents = []
        #parse file and load it into a list
        self.parseFile();

    def parseFile(self):
        for line in self.__m_file:
            #remove newlines
            line = line.strip()
            #filter out comments
            if ('/' not in line and line):
                self.__m_contents.append(line)
    @property
    def getContents(self):
        return self.__m_contents;
