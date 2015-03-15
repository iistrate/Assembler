class Symbol(object):
    """Symbols"""
    def __init__(self, name, value):
        self.__m_name = name
        self.__m_value = value
    
    def __str__(self):
        rep = "Symbol name: {0} Symbol value: {1}".format(getName, getValue)
        return rep

    @property
    def getValue(self):
        return self.__m_value
    @property
    def getName(self):
        return self.__m_name
