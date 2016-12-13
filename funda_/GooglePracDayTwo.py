'''
Akond, Dec 13
'''


def readFileByBlocks(fileName):
  file2open = open(fileName, 'rb')
  while True:
    block_ = file2open.read(65536)
    if not block_:
       break
    yield block_.count(',')


def getLocalMinimumElement(listParam, lParam, hParam):
  m_ = (lParam + hParam)/2
  if ((listParam[m_] < listParam[m_+1]) and (listParam[m_] < listParam[m_-1])):
    return listParam[m_]
  else:
    return getLocalMinimumElement(listParam, lParam, m_)
    return getLocalMinimumElement(listParam, m_ + 1, hParam)
def googleProblemOne(listParam):
   l_ = 0
   h_ = len(listParam)
   output  = getLocalMinimumElement(listParam, l_, h_)
   return output
arr_ = [9, 5, 1, 3, 4, 6, 5, 7]
answer_ = googleProblemOne(arr_)
print "Local minima is:", answer_
print "*"*100
