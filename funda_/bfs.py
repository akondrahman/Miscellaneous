# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 12:14:44 2015

@author: akond
"""
theGraph = {
  'A': set(['B', 'C']),
  'B': set(['A', 'D', 'E']),
  'C': set(['A','F']),
  'D': set(['B']),
  'E': set(['B', 'F']), 
  'F': set(['C', 'E'])
} 
def doDFS(graphParam, startP, visited=None):
  if visited is None:
    visited = set() 
  visited.add(startP)  
  for nextVertex in graphParam[startP] - visited:
    doDFS(graphParam, nextVertex, visited)
  return visited    

def findDFSPath(graph, start,goal, path=None):
  if path==None:
    path = [start]
  if start == goal:
    yield path 
  for nextV in graph[start] - set(path):
    yield findDFSPath(graph, nextV, goal, path + [next]) 
def doBFS(graphParam, startV):
 visited, que = set(), [startV]
 while que:
   v_=que.pop(0)
   if v_ not in visited:
    visited.add(v_)
    que.extend(graphParam[v_] - visited)
 return visited   
 
      
def doBFSPath(graphParam, startV, goalV):
  que = [(startV, [startV])]
  while que:
    (vertex, path) = que.pop(0)
    for next_ in graphParam[vertex] - set(path):
      if next_ == goalV:
        yield path + [next]
      else:
        que.append((next_, path + [next_]))  
        
######### testing area ############
print "the graph", theGraph
print "DFS list: ", doDFS(theGraph, 'C')    
print "DFS path ...", list(findDFSPath(theGraph, 'C', 'F'))
print "BFS list: ", doBFS(theGraph, 'A') 
print "BFS Path ... ", list(doBFSPath(theGraph, 'A', 'F'))