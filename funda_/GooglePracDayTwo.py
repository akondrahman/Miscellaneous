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



def googleProblemTwo(strParam):
 asciiofA=97
 dict2ret={}
 for ind_ in xrange(len(strParam)):
   literal = strParam[ind_]
   if literal not in dict2ret:
    ascii_ = int(literal) + asciiofA
    #print ascii_
    dict2ret[literal]=  chr(ascii_)
   fwd_ = ind_ + 1
   if fwd_ < len(strParam):
    nextLiteral=strParam[fwd_]
    combined = literal + nextLiteral
    theInt = int(combined)
    if ((theInt < 26) and (combined not in dict2ret)):
      ascii_ = int(combined) + asciiofA
      dict2ret[combined]=  chr(ascii_)
 return dict2ret


def googleProblemThree(a):
   output = [0]* len(a)
   for index_ in xrange(len(a)):
    elem = a[index_]
    tmp_ = [x_ for x_ in a if x_!=elem]
    elem2insert = sum(tmp_)
    output[index_] = elem2insert
   return output
arr_ = [9, 5, 1, 3, 4, 6, 5, 7]
answer_ = googleProblemOne(arr_)
print "Local minima is:", answer_
print "*"*100

numberStr='1239451567'
solve = googleProblemTwo(numberStr)
print solve
print "*"*100



aOfInt=[5, 3, 1, 10]
solution = googleProblemThree(aOfInt)
print solution
print "*"*100
