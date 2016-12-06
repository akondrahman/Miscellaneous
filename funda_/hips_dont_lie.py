'''
Akond, Heaps, Dec 06, 2016
'''

def heapify(arr_, n, i):
  left = 2 * (i+1)
  right = 2 * (i+2)
  largest = i
  if ((left < n) and (arr_[i] < arr_[left])):
    largest = left
  if ((right < n) and (arr_[largest] < arr_[right])):
    largest = right
  if (largest!=i):
      arr_[i], arr_[largest] = arr_[largest], arr_[i]
      heapify(arr_, n, largest)

def heapSort(arrayParam):
   len_ = len(arrayParam)
   for i range(len_, -1, -1):
     heapify(arrayParam, len_, i)
   for i range(len_-1, 0, -1):
     arrayParam[0], arrayParam[i] = arrayParam[i], arrayParam[0]
     heapify(arrayParam, i, 0)

array2sort=[100, 10, 2, 97, 1, 5, 44, 50]
heapSort(array2sort)
