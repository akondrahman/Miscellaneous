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


def googleProblemFour(dictP, strP):
  out_ =[]
  #from itertools import permutations
  #allCombs = [''.join(p) for p in permutations(strP)]
  #print allCombs
  for k_, v_ in dictP.iteritems():
    if k_ in strP:
       out_.append(k_)
  return out_

def googleProblemFive(websites):
   tmp_={}
   for website in websites:
    content = website[1]
    name = website[0]
    if content not in tmp_:
      tmp_[content] = [name]
    else:
      lol = tmp_[content]
      tmp_[content] = lol + [name]
   #print tmp_
   outut={}
   for k_, v_ in tmp_.iteritems():
    outut[v_[0]] = v_[1:]
   return outut
def makeithalf(array_, lo_, hi_):
   lo_ = 0
   hi_ = len(array_)
   m_ = (lo_ + hi_)/2
   if ((array_[m_] < array_[m_ + 1]) and (array_[m_] > array_[m_ - 1])):
     return array_[lo_:m_+1]
   elif (array_[m_] > array_[m_ - 1]):
     return array_[m_+1:hi_+1]
   elif ((array_[m_] < array_[m_ + 1])):
     return array_[lo_:m_]

def googleProblemSix(arrayParam):
  arrayToSearch = makeithalf(arrayParam, 0, len(arrayParam))
  min_, max_ = arrayToSearch[0], arrayToSearch[-1]
  return min_, max_
def googleProblemSeven(arrayP, k):
   for x in xrange(k):
    #print x
    ind= x + 1
    if x >=2:
        for y in xrange(len(arrayP)):
            iter_ = ind + y
            if iter_ < len(arrayP):
                tmp_ = arrayP[y:iter_]
                min_tmp = min(tmp_)
                print "Sub array:{}, min:{}".format(tmp_, min_tmp)

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

theDict={'fru':1, 'fruit':2}
theStr='fruit'
sol_ = googleProblemFour(theDict, theStr)
print "Output:", sol_
print "*"*100

websiteContent=[('www.a.com', '<html>a</html>'), ('www.b.com', '<html>b</html>'), ('www.c.com', '<html>c</html>'), ('www.d.com', '<html>a</html>'), ('www.e.com', '<html>a</html>')]
solution_ = googleProblemFive(websiteContent)
print "Webistes:\n",solution_
print "*"*100

theArray=[2, 3, 4, 5, 6, 7, 10, 9, 8, 7]
min_, max_ = googleProblemSix(theArray)
print "Min:{}, and max:{}".format(min_, max_)
print "*"*100

googleProblemSeven(theArray, 4)
print "*"*100
