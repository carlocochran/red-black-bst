#!/usr/local/bin/python3

# Self-balancing Binary Search Tree
# author: Carlo Cochran <carlo.cochran at gmail.com>
# Red-Black Tree algorithm from https://www.cs.auckland.ac.nz/software/AlgAnim/red_black.html

from color import Color
from node import Node

class BST:
    def __init__(self, value):
        if (type(value).__name__ != 'int'):
            raise Exception('value should be an integer: {}'.format(value))
        # root node is always black
        self.__root = Node(value, Color.BLACK)

    def getRootNode(self):
        return self.__root

    def addNode(self, value, currentNode=None):
        if (type(value).__name__ != 'int'):
            raise Exception('value should be an integer: {}'.format(value))

        if (currentNode == None):
            currentNode = self.__root

        if (currentNode.getValue() >= value):
            if (currentNode.getLeftNode() == None):
                newNode = self.__createNewNode(value)
                currentNode.setLeftNode(newNode)
                newNode.setParentNode(currentNode)
                self.__rebalance(newNode)
                return newNode
            else:
                return self.addNode(value, currentNode.getLeftNode())
        else:
            if (currentNode.getRightNode() == None):
                newNode = self.__createNewNode(value)
                currentNode.setRightNode(newNode)
                newNode.setParentNode(currentNode)
                self.__rebalance(newNode)
                return newNode
            else:
                return self.addNode(value, currentNode.getRightNode())

    def __rebalance(self, x):
        if (self.__isEqual(x, self.__root) or x.getParentNode().getColor() == Color.BLACK):
            return
        else:
            if (self.__isEqual(x.getParentNode(), x.getParentNode().getParentNode().getLeftNode())):
                y = x.getParentNode().getParentNode().getRightNode()
                if (y != None and y.getColor() == Color.RED):
                    x.getParentNode().setColor(Color.BLACK)
                    y.setColor(Color.BLACK)
                    x.getParentNode().getParentNode().setColor(Color.RED)
                    self.__rebalance(x.getParentNode().getParentNode())
                else:
                    if self.__isEqual(x, x.getParentNode().getRightNode()):
                        x = x.getParentNode()
                        self.__rotateLeft(x)
                    x.getParentNode().setColor(Color.BLACK)
                    x.getParentNode().getParentNode().setColor(Color.RED)
                    self.__rotateRight(x.getParentNode().getParentNode())
                    self.__rebalance(x)
            else:
                y = x.getParentNode().getParentNode().getLeftNode()
                if (y != None and y.getColor() == Color.RED):
                    x.getParentNode().setColor(Color.BLACK)
                    y.setColor(Color.BLACK)
                    x.getParentNode().getParentNode().setColor(Color.RED)
                    self.__rebalance(x.getParentNode().getParentNode())
                else:
                    if self.__isEqual(x, x.getParentNode().getLeftNode()):
                        x = x.getParentNode()
                        self.__rotateRight(x)
                    x.getParentNode().setColor(Color.BLACK)
                    x.getParentNode().getParentNode().setColor(Color.RED)
                    self.__rotateLeft(x.getParentNode().getParentNode())
                    self.__rebalance(x)

        self.__root.setColor(Color.BLACK)    

    def __createNewNode(self, value):
        # new node is always red
        return Node(value, Color.RED)

    def __rotateLeft(self, pivot_node):
        new_parent_node = pivot_node.getRightNode()
        pivot_node.setRightNode(new_parent_node.getLeftNode())
        subtree_node  = new_parent_node.getLeftNode()
        if subtree_node != None:
            subtree_node.setParentNode(pivot_node)
            pivot_node.setRightNode(subtree_node)

        pivot_node_parent = pivot_node.getParentNode()
        new_parent_node.setParentNode(pivot_node_parent)
        if pivot_node_parent == None:
            self.__root = new_parent_node
        elif self.__isEqual(pivot_node, pivot_node.getParentNode().getLeftNode()):
            pivot_node_parent.setLeftNode(new_parent_node)
        else:
            pivot_node_parent.setRightNode(new_parent_node)
        
        new_parent_node.setLeftNode(pivot_node)
        pivot_node.setParentNode(new_parent_node)

    def __rotateRight(self, pivot_node):
        new_parent_node = pivot_node.getLeftNode()
        pivot_node.setLeftNode(new_parent_node.getRightNode())
        subtree_node  = new_parent_node.getRightNode()
        if subtree_node != None:
            subtree_node.setParentNode(pivot_node)
            pivot_node.setLeftNode(subtree_node)

        pivot_node_parent = pivot_node.getParentNode()
        new_parent_node.setParentNode(pivot_node_parent)
        if pivot_node_parent == None:
            self.__root = new_parent_node
        elif self.__isEqual(pivot_node, pivot_node.getParentNode().getRightNode()):
            pivot_node_parent.setRightNode(new_parent_node)
        else:
            pivot_node_parent.setLeftNode(new_parent_node)
        
        new_parent_node.setRightNode(pivot_node)
        pivot_node.setParentNode(new_parent_node)

    def __isEqual(self, node1, node2):
        return node1 != None and node2 != None and node1.getUUID() == node2.getUUID()        

    def printInOrder(self):
        return self.__inOrder(self.__root)

    def __inOrder(self, currentNode):
        if (currentNode == None):
            return

        self.__inOrder(currentNode.getLeftNode())
        print (currentNode.getValue(), end =" ")
        print (currentNode.getColor().name)
        self.__inOrder(currentNode.getRightNode())

    def printPreOrder(self):
        return self.__preOrder(self.__root)

    def __preOrder(self, currentNode):
        if (currentNode == None):
            return

        print (currentNode.getValue(), end =" ")
        print (currentNode.getColor().name)
        self.__preOrder(currentNode.getLeftNode())
        self.__preOrder(currentNode.getRightNode())

    def printPostOrder(self):
        return self.__postOrder(self.__root)

    def __postOrder(self, currentNode):
        if (currentNode == None):
            return

        self.__postOrder(currentNode.getLeftNode())
        self.__postOrder(currentNode.getRightNode())        
        print (currentNode.getValue(), end =" ")
        print (currentNode.getColor().name)
