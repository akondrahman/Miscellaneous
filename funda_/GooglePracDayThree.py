'''
Akond, Dec 14, Day 3
'''

def GoogleProbOne(arrayP):
  for i_ in xrange(len(arrayP)):
    for j_ in xrange(len(arrayP)):
      if j_ > i_:
        subArray = arrayP[i_: j_+1]
        sumOfSub=sum(subArray)
        if ((sumOfSub>=i_) and (sumOfSub<=j_)):
           print "Eligible sub-array:",subArray


def GoogleProbTwo(arrayP):
   for x_ in xrange(len(arrayP)):
    fHalf = arrayP[0:x_+1]
    lHalf = arrayP[x_+1:]
    if (sum(fHalf)==sum(lHalf)):
        print "The index is:", x_

def GoogleProbThree(idAndWeight):
 out_=[]
 for ind_ in xrange(len(idAndWeight)):
  out_.append(idAndWeight[ind_][1])
 return out_

def isPalin(s_):
    if s_ == s_[::-1]:
        return True

def GoogleProbFour(s_):
   tmp_=''
   for idy, item_ in enumerate(s_):
     for idx, item_ in enumerate(s_):
        lol_ = s_[idy:idx+1]
        if ((len(lol_) > len(tmp_)) and (isPalin(lol_))):
            tmp_=lol_
   return tmp_
def GoogleProbFive(matParam):
  fla_ = False
  firstRow = matParam[0]
  nCols= len(firstRow)
  for ind_ in xrange(nCols):
    curr_ = firstRow[ind_]
    #print curr_
    for next_ in xrange(1, len(matParam), 1):
        #print next_
        nextCol = ind_ + next_
        if nextCol < nCols:
          nextElem = matParam[next_][nextCol]
          if nextElem==curr_:
            fla_=True
  return fla_

arra_=[5, 1, 3, 4, 7, 6, 1, 2]
GoogleProbOne(arra_)
print '*'*100
idweight=[[4, 20], [2, 30], [3, 40], [4, 50]]
wieght = GoogleProbThree(idweight)
print "Weights:", wieght
print '*'*100
stringForPalin='gggaaa'
outPalin= GoogleProbFour(stringForPalin)
print "Palindrome output", outPalin
print '*'*100
theMat=[[6, 7, 8, 9, 2], [4, 6, 7, 8, 9], [1, 4, 6, 7, 8], [0, 1, 4, 6, 7]]
theFlag=GoogleProbFive(theMat)
print "Is timponze?", theFlag
