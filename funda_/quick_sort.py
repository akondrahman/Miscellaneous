'''
Quick Sort: Akond: Dec 05, 2016
'''

def performQuickSort(myList, low_, hig_):
  if low_ < hig_:
    pivot = performPart(myList, low_, hig_)
    performQuickSort(myList, low_, pivot - 1)
    performQuickSort(myList, pivot +1, hig_)
  return myList 
