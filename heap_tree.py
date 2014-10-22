
class TreeNode(object):

    def setParent(self,newParent):
        self._parent = newParent
    def getParent(self):
        return self._parent
    parent = property(fget = getParent,
                      fset = setParent)
    
    def setLeftSon(self,newLeftSon):
        self._leftSon = newLeftSon
    def getLeftSon(self):
        return self._leftSon
    leftSon = property(fget = getLeftSon,
                       fset = setLeftSon)

    def setRightSon(self,newRightSon):
        self._rightSon = newRightSon
    def getRightSon(self):
        return self._rightSon
    rightSon = property(fget = getRightSon,
                        fset = setRightSon)

    def setValue(self,newVal):
        self._value = newVal
    def getValue(self):
        return self._value
    value = property(fget = getValue,
                     fset = setValue)

    def __init__(self,value):
        pass
        self.setLeftSon(None)
        self.setRightSon(None)
        self.setParent(None)
        self.setValue(value)
        

class Tree(object):
    def setRoot(self,value):
        self._root = value
    def getRoot(self):
        return self._root
    root = property(fget = lambda self: self.getRoot(),
                    fset = lambda self, value: self.setRoot(value))

    def __init__(self):
        pass
        self._root = None

    def _cartesianInsert(self,thisNode,lastInserted):
        if (thisNode.getValue() <= lastInserted.getValue() and
             lastInserted.getRightSon() is None):
            pass # This is the nice, vanilla case
            lastInserted.setRightSon(thisNode)
            thisNode.setParent(lastInserted)
            return
        if (thisNode.getValue() > lastInserted.getValue()):
            pass # We go up through parents, and insert where adequate
            if lastInserted.getParent() == None:
                pass # In this case, we just inserted the root
                self.root = thisNode
                thisNode.setLeftSon(lastInserted)
                lastInserted.setParent(thisNode)
                return
            parentHeader = lastInserted.getParent()
            while parentHeader is not None:
                if (thisNode.getValue() <= parentHeader.getValue()):
                    thisNode.setLeftSon(parentHeader.getRightSon())
                    parentHeader.setRightSon(thisNode)
                    thisNode.setParent(parentHeader)
                    thisNode.getLeftSon().setParent(thisNode)
                    return
                parentHeader = parentHeader.getParent()
            if parentHeader is None:
                thisNode.setLeftSon(self.root)
                self.root.setParent(thisNode)
                self.root = thisNode
        return
            

    def createCartesianTree(self,A):
        lastInserted = None
        for a in A:
            #print 'a is '+str(a) +' - '+str(self.inorderTraversal())
            thisNode = TreeNode(a)
            if self.root is None:
                self.root = thisNode
                lastInserted = thisNode
                continue
            self._cartesianInsert(thisNode,lastInserted)
            lastInserted = thisNode


    def _inorderTraversal(self,node,addHere):
        if node.getLeftSon() is not None:
            self._inorderTraversal(node.getLeftSon(),addHere)
        addHere.append(node.getValue())
        if node.getRightSon() is not None:
            self._inorderTraversal(node.getRightSon(),addHere)
        return addHere

    def inorderTraversal(self):
        if self.root is None:
            return list()
        result = self._inorderTraversal(self.root,list())
        return result


"""
After the class itself, I'm adding some testing to brag
"""
print "TESTING..."
from random import randrange
tester = None
trav = None
for i in range(10):
    tree = Tree()
    tester = [randrange(1000) for _ in range(100)]
    tree.createCartesianTree(tester)
    trav = tree.inorderTraversal()
    if trav != tester:
        print 'ERROR! '+str(tester)
        break
    trav = None
if trav is None:
    print 'Results are satisfactory.'

