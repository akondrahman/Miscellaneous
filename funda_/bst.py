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
   def insertIntoBinaryTree(self, rootP, elemP):
       if rootP!=None:
         if elemP == rootP.value:
           rootP.count = rootP.count + 1
       elif rootP.value < elemP:
          nodeToInsert = nodeInTree(None, None, elemP)
          nodeToInsert =  self.insertIntoBinaryTree(rootP.left, elemP)
       elif rootP.value > elemP:
          nodeToInsert = nodeInTree(None, None, elemP)
          nodeToInsert = self.insertIntoBinaryTree(rootP.right, elemP)
       return nodeToInsert
'''
Execution
'''
arrayToCreate = [3,15,16,24,57,7]
sorted(arrayToCreate)
bst = binaryTree()
bst.root = bst.createBinaryTree(arrayToCreate,0,len(arrayToCreate)-1)
bst.root.printSelf()
print "*"*50
nodeToLook = bst.searchBinaryTree(24, bst.root)
nodeToLook.printSelf()
elemToInsert = 100
bst.insertIntoBinaryTree(bst.root, elemToInsert)
print "*"50 
