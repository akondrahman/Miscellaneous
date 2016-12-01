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

def performDFS(graphParam, rootParam):
  stackToTrack = []
  outputDFS = []
  nodeToTraverse=''
  popFlag=False
  stackToTrack.append(rootParam)
  while(len(stackToTrack) > 0):
   print "lol:", stackToTrack
   nodeToTraverse = stackToTrack[len(stackToTrack)-1]
   if (nodeToTraverse in graphParam):
     adj_nodes = graphParam[nodeToTraverse]
     if ((nodeToTraverse not in outputDFS) and (len(adj_nodes) > 0 )):
       for adj_node in adj_nodes:
          if ((adj_node not in stackToTrack) and (len(adj_node) > 0) and (adj_node not in outputDFS)):
            stackToTrack.append(adj_node)
          else:
            popFlag = True
     else:
            popFlag = True
   else:
            popFlag = True
   if popFlag:
     outputDFS.append( stackToTrack.pop())
     popFlag=False
  #print "elem:", elemToPop
  return outputDFS



theGraph={'s':['a', 'b', 'c'],
          'a':['d'],
          'b':['e'],
          'c':['f'],
          'd':['g'],
          'e':['g'],
          'g':[]
}
bfs_output = performBFS(theGraph, 's')
#print bfs_output
dfs_output = performDFS(theGraph, 's')
print dfs_output
