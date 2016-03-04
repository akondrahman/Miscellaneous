
"""
Created on Tue Nov 24 19:32:03 2015

@author: akond
"""

def performWilcoxonRankSumTest(vectorX, vectorY):
  from scipy import stats
  res = stats.ranksums(vectorX, vectorY)
  return res     
  
  
  
