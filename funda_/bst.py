'''
Binary Search Tree: Dec 03, 2016:Saturday
'''

class nodeInTree:
  def __init__(self, leftP, rightP, valueP):
    self.left = leftP
    self.right = rightP
    self.value = valueP
    self.count = 1
  def printSelf(self):
   print "Node value is:", self.value

class binaryTree:
   def __init__(self):
     self.root= None
   def createBinaryTree(self, arrayP, lowIndexP, highIndexP):
      newNode = None
      if lowIndexP<= highIndexP:
        middle = (lowIndexP + highIndexP)/2
        newNode = nodeInTree(None, None, arrayP[middle])
        newNode.left =  self.createBinaryTree(arrayP, lowIndexP, middle - 1 )
        newNode.right =  self.createBinaryTree(arrayP, middle+1, highIndexP)
      return newNode
   def searchBinaryTree(self, elemP, rootP):
      nodeToRet = None
      if rootP != None:
        if rootP.value==elemP:
          nodeToRet = rootP
        elif elemP < self.root.value:
          nodeToRet = self.searchBinaryTree(elemP, rootP.left)
        elif elemP > self.root.value:
          nodeToRet = self.searchBinaryTree(elemP, rootP.right)
      return nodeToRet
'''
Execution
'''
arrayToCreate = [3,5,7,15,16,24,57]
sorted(arrayToCreate)
bst = binaryTree()
bst.root = bst.createBinaryTree(arrayToCreate,0,len(arrayToCreate)-1)
bst.root.printSelf()
print "*"*50
nodeToLook = bst.searchBinaryTree(24, bst.root)
nodeToLook.printSelf()
