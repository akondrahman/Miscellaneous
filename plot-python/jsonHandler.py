# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 14:22:42 2015

@author: akond
"""



def createDictFromJSONFile(jsonFileParam):
 from ijson import items
 jsonFile = open(jsonFileParam)
 

 objects = items(jsonFile, 'Sessions.item')
 sessionDictionary={}
 for obj in objects: 
  #print "{}-->{}-->{}".format(obj['SessionID'], obj['Path'], obj['EventType'])
  tmpSessID =  obj['SessionID'] 
  tmpSessPath = obj['Path']
  tmpSessEvent = obj['EventType']
  tmpSessStartTick = obj['E_StartTicks']
  tmpSessEndTick = obj['E_EndTicks']
  tmpSessState = obj['State']  
  #sessIDList.append(int(obj['SessionID']))
  if not tmpSessID in sessionDictionary:
        sessionDictionary[tmpSessID] = [(tmpSessPath, tmpSessEvent, tmpSessState, tmpSessStartTick, tmpSessEndTick)]
  else:
        sessionDictionary[tmpSessID].append((tmpSessPath, tmpSessEvent, tmpSessState, tmpSessStartTick, tmpSessEndTick))  
 #print sessionDictionary
 return sessionDictionary   



def giveStateInfoFromDict(valParam, stateIdentifierParam): 
  stateCnt = 0
  listRange = len(valParam)
  for cnt in range(0, listRange):
    if valParam[cnt][2]==stateIdentifierParam:
      stateCnt = stateCnt + 1  
  return stateCnt
  


def giveDurationOfState(valParam, stateIdentifierParam):
  durationToRet = 0   
  # unitVal = 1 for seconds, 60 for minutes, 3600 for hours
  unitVal = 1
  listRange = len(valParam)
  for cnt in range(0, listRange):
    if valParam[cnt][2]==stateIdentifierParam:
      startTick = valParam[cnt][3]
      endTick = valParam[cnt][4]
      if endTick > startTick:
        calcDuration = lambda startP, endP: (float(endP) - float(startP))/float(10000000*unitVal)   
        durationToRet = durationToRet + calcDuration(startTick, endTick)
  return durationToRet      
  
  
def codeCntFromDict(valParam, fieldParam, stateP):   
  eventCnt = 0
  listRange = len(valParam)
  for cnt in range(0, listRange):
    if (valParam[cnt][1]==fieldParam) and (valParam[cnt][2]==stateP):
      eventCnt = eventCnt + 1  
  return eventCnt    



def codeDurationFromDict(valParam, fieldParam, stateP):
  durationToRet = 0   
  # unitVal = 1 for seconds, 60 for minutes, 3600 for hours
  unitVal = 1
  listRange = len(valParam)
  for cnt in range(0, listRange):
    if (valParam[cnt][1]==fieldParam) and (valParam[cnt][2]==stateP):
      startTick = valParam[cnt][3]
      endTick = valParam[cnt][4]
      if endTick > startTick:
        calcDuration = lambda startP, endP: (float(endP) - float(startP))/float(10000000*unitVal)   
        durationToRet = durationToRet + calcDuration(startTick, endTick)
  return durationToRet  
  