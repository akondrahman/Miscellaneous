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
