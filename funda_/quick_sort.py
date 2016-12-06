'''
Quick Sort: Akond: Dec 05, 2016
'''

def performQuickSort(myList, low_, hig_):
  if low_ < hig_:
    pivot = performPart(myList, low_, hig_)
    performQuickSort(myList, low_, pivot - 1)
    performQuickSort(myList, pivot +1, hig_)
  return myList




def performPart(theList, l_, h_):
   done=False
   pivot = theList[l_]
   left = l_ + 1
   right = h_
   while not done:
     while ((left <= right) and (theList[left] <= pivot)):
        left = left + 1
     while ((left <= right) and (theList[right] >= pivot)):
        right = right - 1
     if left > right:
        done = True
     else:
        tmp_ = theList[left]
        theList[left] = theList[right]
        theList[right] = tmp_
   tmp_ = theList[left]
   theList[left] = theList[right]
   theList[right] = tmp_
   return right
