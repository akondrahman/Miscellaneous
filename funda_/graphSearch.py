'''
Author: Akond Nov 30, 2016
'''
def performBFS(theGraphParam, rootParam):
  outputBFS={}
  currentTraversedPath=[]
  nodeToTraverse = rootParam
  theQueue = [rootParam]
  outputBFS[rootParam] = ('NULL', 0, [])
  while (len(theQueue) > 0):
   #print "before:", theQueue
   nodeToTraverse = theQueue.pop(0)
   #print "after:", theQueue
   #currentTraversedPath.append(nodeToTraverse)
   if nodeToTraverse in theGraphParam:
     adjacencyList = theGraphParam[nodeToTraverse]
     for node_ in adjacencyList:
       if node_ not in theQueue:
         theQueue.append(node_)
         currentDistance = outputBFS[nodeToTraverse][1] + 1
         currPath = outputBFS[nodeToTraverse][2] + [nodeToTraverse]
         outputBFS[node_] = (nodeToTraverse, currentDistance, currPath)
  return outputBFS


theGraph={'s':['a', 'b', 'c'],
          'a':['d'],
          'b':['e'],
          'c':['f'],
          'd':['g'],
          'e':['g'],
          'g':[]
}
bfs_output = performBFS(theGraph, 's')
print bfs_output
