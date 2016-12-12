'''
Dec 07, 2016:Akond:Dynamic Programming
'''

def coinProblem(theSumToMake, theCoins):
  lol= len(theCoins) + 1
  min_ = [9999999]* lol
  for ind_ in xrange(theSumToMake):
    if ind_==0:
        min_[ind_] = 0
    else:
      for j_ in xrange(len(theCoins)):
        if((theCoins[j_] <= ind_) and ( min_[ind_ - theCoins[j_]] < min_[ind_])):
          min_[ind_]  = min_[ind_ - theCoins[j_]] + 1

  return min_[theCoins]




sumToMake=24
coins=[1, 5, 25]
output_ = coinProblem(sumToMake, coins)
print output_
