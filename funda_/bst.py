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
         elif rootP.value > elemP:
          rootP.left =  self.insertIntoBinaryTree(rootP.left, elemP)
         elif rootP.value < elemP:
          rootP.right = self.insertIntoBinaryTree(rootP.right, elemP)
       else:
          nodeToInsert = nodeInTree(None, None, elemP)
          rootP = nodeToInsert
       return rootP



   def doInOrderPrint(self, root_):
     if root_!= None:
        root_.left = self.doInOrderPrint(root_.left)
        print str(root_.value) + ":"
        root_.right = self.doInOrderPrint(root_.right)
   def remove(self, root):
        node2remove = root
        if root == None:
            return None
        if root.right ==None:
            root = root.left
        elif root.left == None:
            root = root.right
        else:
            parent = root
            node2remove = root.left
            while node2remove.right != None:
                parent = node2remove
                node2remove = node2remove.right
            root.value = node2remove.value
            if parent == root:
                parent.left = root.left
            else:
                parent.right = root.right
        return root
   def removeElem(self, rootP_, elemP):
    if rootP_!= None:
        if elemP < rootP_.value:
            rootP_.left = self.removeElem(rootP_.left, elemP)
        elif elemP > rootP_.value:
            rootP_.right = self.removeElem(rootP_.right, elemP)
        else:
            rootP_ = self.remove(rootP_)
    return rootP_
'''
Execution
'''
elem_ = 100
arrayToCreate = [3,15,16,24,57,7]
arrayToCreate = sorted(arrayToCreate)
bst = binaryTree()
bst.root = bst.createBinaryTree(arrayToCreate,0,len(arrayToCreate)-1)
bst.root.printSelf()
print "*"*50
nodeToLook = bst.searchBinaryTree(24, bst.root)
nodeToLook.printSelf()
print "*"*50
checkRoot = bst.insertIntoBinaryTree(bst.root, elem_)
checkRoot.printSelf()
print "*"*50
bst.doInOrderPrint(bst.root)
print "*"*50 + "Before" + "*"*50
bst.removeElem(bst.root, elem_)
bst.doInOrderPrint(bst.root)
print "*"*50 + "After" + "*"*50
