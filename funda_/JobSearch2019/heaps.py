'''
Akond Rahman 
Dec 02, 2018 
Heap Practice 
'''

import heapq 

if __name__=='__main__':
   ls = [21, 1, 45, 78, 3, 5]
   heapq.heapify(ls)  ## returns None 
   print ls 
   heapq.heappush(ls, 99) 
   print ls 
   heapq.heappop(ls)
   print ls 
   heapq.heapreplace(ls, 7)
   print ls 