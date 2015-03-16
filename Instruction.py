class Instruction(object):
    """Instruction key value"""
    def __init__(self, name, value):
        self.__m_name = name
        self.__m_value = value
    
    def __str__(self):
        rep = "Instruction name: {0} | value: {1}".format(getName, getValue)
        return rep
    
    @property
    def getValue(self):
        return self.__m_value
    @property
    def getName(self):
        return self.__m_name
