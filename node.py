import uuid

class Node(object):
    def __init__(self, value, color):
        self.setValue(value)
        self.setColor(color)
        self.__uuid = uuid.uuid1()
        self.__leftNode = None
        self.__rightNode = None
        self.__parentNode = None

    def setLeftNode(self, node):
        if (node != None and type(node).__name__ != 'Node'):
            raise Exception('value should be a Node: {}'.format(node))
        self.__leftNode = node

    def setRightNode(self, node):
        if (node != None and type(node).__name__ != 'Node'):
           raise Exception('value should be a Node: {}'.format(node))        
        self.__rightNode = node

    def getLeftNode(self):
        return self.__leftNode

    def getRightNode(self):
        return self.__rightNode

    def setValue(self, value):
        if (type(value).__name__ != 'int'):
            raise Exception('value should be an integer: {}'.format(value))
        self.__value = value

    def getValue(self):
        return self.__value

    def setColor(self, color):
        if (type(color).__name__ != 'Color'):
            raise Exception('color should be a Color: {}'.format(color))
        self.__color = color

    def getColor(self):
        return self.__color

    def setParentNode(self, node):
        if (node != None and type(node).__name__ != 'Node'):
            raise Exception('value should be a Node: {}'.format(node))        
        self.__parentNode = node

    def getParentNode(self):
        return self.__parentNode
    
    def getUUID(self):
        return self.__uuid
