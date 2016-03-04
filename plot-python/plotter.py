# -*- coding: utf-8 -*-
"""
Created on Fri Oct 23 17:34:03 2015

@author: akond
"""



def compareViaBoxPlot(posGroupParam, zeroGroupParam, negGroupParam, fileNameParam):
  import plotly.plotly as py
  import plotly.graph_objs as go
  from plotly.graph_objs import  Layout, YAxis, Figure, Margin, Font  
  #from plotly.graph_objs import Bar, Marker, Data, Layout, XAxis, YAxis, Figure, Margin, Font    

  posGroup = go.Box(
    y=posGroupParam, 
    name='Corr. >= 0.50'
  )
  zeroGroup = go.Box(
    y=zeroGroupParam, 
    name='Corr. within 0.0 & 0.499'    
  )
  negGroup = go.Box(
    y=negGroupParam, 
    name='Corr. < 0.0'        
  )  
  
  layoutToUse = Layout(
            title='Distribution of Three Groups: ' + fileNameParam,
            titlefont=Font(
                    family='Times New Roman',
                    size=18,
                    color='#000000'
            ),
            yaxis=YAxis(
                showgrid=True,
                showline=True,    
                title='Values',
                #range=[0, 35],
                autorange=True,        
                titlefont=Font(
                    family='Times New Roman',
                    size=12,
                    color='#000000'
                )
            ),
            width=800,
            height=600,
            margin=Margin(
                l=140,
                r=40,
                b=50,
                t=80
            ),
  )  
  
  dataToPlot = [posGroup, zeroGroup, negGroup]
  #plot_url = py.plot(dataToPlot, filename=fileNameParam)    
  figToPlot = Figure(data=dataToPlot, layout=layoutToUse)
  fileNameParam = "plots/" + fileNameParam + ".png"
  py.image.save_as(figToPlot, fileNameParam)  
  # crazy shit .... 
  #py.plot(figToPlot, filename = fileNameParam) 

  
def plotCorrelations(fileNameP, listP):
    import plotly.plotly as py
    #import plotly
    from plotly.graph_objs import Bar, Marker, Data, Layout, XAxis, YAxis, Figure, Margin, Font
    #import plotly.graph_objs as gObjLib
    ### authentication stuff .... 
    #py = plotly.plotly(username='akond', key='9ebth53cdo')
    #barSize = 5
    fileTrace=[listP[0], listP[1], listP[2]]
    projectTrace=[listP[3], listP[4], listP[5]]
    stateTrace=[listP[6], listP[7], listP[8]]
    namespaceTrace=[listP[9], listP[10], listP[11]]    

    fileCorrTrace = Bar(
            x=['Corr. >= 0.50', 'Corr. within 0.0 & 0.499',  'Corr. < 0.0'],
            #x=[ 'Idle', 'System', 'Code', 'Debug', 'Build'],           
            y=fileTrace,
            name='FileInterleaving'
    )
    
    projCorrTrace = Bar(
            x=['Corr. >= 0.50', 'Corr. within 0.0 & 0.499',  'Corr. < 0.0'],
            #x=[ 'Idle', 'System', 'Code', 'Debug', 'Build'],           
            y=projectTrace,
            name='ProjetInterleaving'
    )        

    nspaceCorrTrace = Bar(
            x=['Corr. >= 0.50', 'Corr. within 0.0 & 0.499',  'Corr. < 0.0'],
            #x=[ 'Idle', 'System', 'Code', 'Debug', 'Build'],
            y=namespaceTrace,
            name='NamespaceInterleaving'
    )
       

    stateTrace = Bar(
            x=['Corr. >= 0.50', 'Corr. within 0.0 & 0.499',  'Corr. < 0.0'],
            #x=[ 'Idle', 'System', 'Code', 'Debug', 'Build'],          
            y=stateTrace,
            name='StateInterleaving'
    )

    #fileCorrTrace['marker'] = Marker(color='blue', size=barSize)
    #projCorrTrace['marker'] = Marker(color='green', size=barSize)
    #nspaceCorrTrace['marker'] = Marker(color='yellow', size=barSize)
    #stateTrace['marker'] = Marker(color='red', size=barSize)    
    fileCorrTrace['marker'] = Marker(color='blue')
    projCorrTrace['marker'] = Marker(color='green')
    nspaceCorrTrace['marker'] = Marker(color='yellow')
    stateTrace['marker'] = Marker(color='red')        
    dataToPlot = Data([fileCorrTrace, projCorrTrace, nspaceCorrTrace, stateTrace])

    layoutToUse = Layout(
            title='Distribution of Correlation for 339 Datasets : ' + fileNameP ,
            titlefont=Font(
                    family='Times New Roman',
                    size=18,
                    color='#000000'
            ),
            barmode='group', 
            xaxis=XAxis(
                showgrid=True,
                showline=True,
                title='Interleaving Correlations',
                titlefont=Font(
                    family='Times New Roman',
                    size=12,
                    color='#000000'
                ), 
                tickwidth=1.5
            ),
            yaxis=YAxis(
                showgrid=True,
                showline=True,    
                title='Count',
                #range=[0, 35],
                autorange=True,        
                titlefont=Font(
                    family='Times New Roman',
                    size=12,
                    color='#000000'
                )
            ),
            width=800,
            height=600,
            margin=Margin(
                l=140,
                r=40,
                b=50,
                t=80
            ),
    )
    fileToSave = 'plots/' + fileNameP + '.png'
    figToPlot = Figure(data=dataToPlot, layout=layoutToUse)
    py.image.save_as(figToPlot, fileToSave)
    # crazy shit .... 
    #py.plot(figToPlot, filename = fileToSave)
    
def plotAllStates(fileNameP, dictP):
    import plotly.plotly as py
    from plotly.graph_objs import Bar, Marker, Data, Layout, XAxis, YAxis, Figure, Margin, Font
    #import plotly.graph_objs as gObjLib
    #####
    dirToSave="plotsesscat/"
    #barSize = 6
    listForNormalTrace = []
    listForHeavyTrace = []
    listForSuperHeavyTrace = []
    allCatList = ['None', 'Idle', 'System', 'Code', 'Debug', 'Build', 'Navi']
    for it_ in allCatList:
       #print "ZZZZZZZ", dictP[it_] 
       listForNormalTrace.append(dictP[it_][0])  
       listForHeavyTrace.append(dictP[it_][1]) 
       listForSuperHeavyTrace.append(dictP[it_][2])           
        

    
    #print "length - Normal ... ", listForNormalTrace
    #print "length - Heavy ... ", listForHeavyTrace
    #print "length - SuperHeavy ... ", listForSuperHeavyTrace    
    normalTrace = Bar(
            x=['None', 'Idle', 'System', 'Code', 'Debug', 'Build', 'Navi'],
            #x=[ 'Idle', 'System', 'Code', 'Debug', 'Build'],           
            y=listForNormalTrace,
            name='Normal'
    )
        

    heavyTrace = Bar(
            x=['None', 'Idle', 'System', 'Code', 'Debug', 'Build', 'Navi'],
            #x=[ 'Idle', 'System', 'Code', 'Debug', 'Build'],
            y=listForHeavyTrace,
            name='Heavy'
    )
       

    superHeavyTrace = Bar(
            x=['None', 'Idle', 'System', 'Code', 'Debug', 'Build', 'Navi'],
            #x=[ 'Idle', 'System', 'Code', 'Debug', 'Build'],          
            y=listForSuperHeavyTrace,
            name='Super Heavy'
    )


    normalTrace['marker'] = Marker(color='green')
    heavyTrace['marker'] = Marker(color='yellow')
    superHeavyTrace['marker'] = Marker(color='red')    
    dataToPlot = Data([normalTrace, heavyTrace, superHeavyTrace])

    layoutToUse = Layout(
            title='Distribution of Different Session Categories',
            titlefont=Font(
                    family='Times New Roman',
                    size=22,
                    color='#000000'
            ),
            barmode='group', 
            xaxis=XAxis(
                showgrid=True,
                showline=True,
                title='Types of Sessions',
                titlefont=Font(
                    family='Times New Roman',
                    size=18,
                    color='#000000'
                ), 
                tickwidth=1.5
            ),
            yaxis=YAxis(
                showgrid=True,
                showline=True,    
                title='Count',
                #range=[0, 35],
                autorange=True,        
                titlefont=Font(
                    family='Times New Roman',
                    size=18,
                    color='#000000'
                )
            ),
            width=800,
            height=600,
            margin=Margin(
                l=140,
                r=40,
                b=50,
                t=80
            ),
    )
    fileToSave = dirToSave +  fileNameP + '.png'
    figToPlot = Figure(data=dataToPlot, layout=layoutToUse)
    #plot_url = py.plot(figToPlot, filename=fileToSave)
    py.image.save_as(figToPlot, fileToSave)    
def compareFileExtViaBoxPlots(dictParam, fileNameParam, extList):
  import plotly.plotly as py
  import plotly.graph_objs as go
  from plotly.graph_objs import  Layout, YAxis, Figure, Margin, Font  
  #from plotly.graph_objs import Bar, Marker, Data, Layout, XAxis, YAxis, Figure, Margin, Font    
  dataToPlot = []
  for it_ in extList:
    trace_ = go.Box(
      y= dictParam[it_]  , 
      name=it_
    )
    dataToPlot.append(trace_)        
        
  
  layoutToUse = Layout(
            title='Distribution of File Types : ' + fileNameParam,
            titlefont=Font(
                    family='Times New Roman',
                    size=18,
                    color='#000000'
            ),
            yaxis=YAxis(
                showgrid=True,
                showline=True,    
                title='Values',
                #range=[0, 35],
                autorange=True,        
                titlefont=Font(
                    family='Times New Roman',
                    size=12,
                    color='#000000'
                )
            ),
            width=800,
            height=600,
            margin=Margin(
                l=140,
                r=40,
                b=50,
                t=80
            ),
  )  
  

  #plot_url = py.plot(dataToPlot, filename=fileNameParam)    
  figToPlot = Figure(data=dataToPlot, layout=layoutToUse)
  fileNameParam = "plot-session-info/" + fileNameParam + ".png"
  py.image.save_as(figToPlot, fileNameParam)  
  # crazy shit .... 
  #py.plot(figToPlot, filename = fileNameParam)   
def plotSharpVSOthers(dictParam, fileNameParam, extOfInterest="cSharpCount"):
  import plotly.plotly as py
  import plotly.graph_objs as go
  from plotly.graph_objs import  Layout, YAxis, Figure, Margin, Font      
  cSharpList = dictParam[extOfInterest]
  otherList = [ 100.0 - float(x) for x in cSharpList  ]
  cSharpTrace_ = go.Box(
      y= cSharpList  , 
      name="C# Files"
    )
  otherTrace_ = go.Box(
      y= otherList  , 
      name="Other Files"
    ) 
  dataToPlot = [ cSharpTrace_, otherTrace_  ]
  layoutToUse = Layout(
            title='Distribution of File Types : ' + fileNameParam,
            titlefont=Font(
                    family='Times New Roman',
                    size=18,
                    color='#000000'
            ),
            yaxis=YAxis(
                showgrid=True,
                showline=True,    
                title='Values',
                #range=[0, 35],
                autorange=True,        
                titlefont=Font(
                    family='Times New Roman',
                    size=12,
                    color='#000000'
                )
            ),
            width=800,
            height=600,
            margin=Margin(
                l=140,
                r=40,
                b=50,
                t=80
            ),
  )  
  

  #plot_url = py.plot(dataToPlot, filename=fileNameParam)    
  figToPlot = Figure(data=dataToPlot, layout=layoutToUse)
  fileNameParam = "plot-session-info/" + fileNameParam + ".png"
  py.image.save_as(figToPlot, fileNameParam)    
  
def compareFileExtViaBarPlots(dictParam, fileNameParam, listParam):
  import plotly.plotly as py
  import plotly.graph_objs as go
  from plotly.graph_objs import  Layout, YAxis, Figure, Margin, Font    
  import numpy as np
  xList=[]
  yList=[]
  for it_ in listParam:  
   xList.append(it_)  
   yList.append( np.mean(dictParam[it_])) 
   
  dataToPlot = [
      go.Bar(
        x=xList  ,
        y=yList
      )
  ]
  layoutToUse = Layout(
            title='Distribution of File Types (Average) : ' + fileNameParam,
            titlefont=Font(
                    family='Times New Roman',
                    size=18,
                    color='#000000'
            ),
            yaxis=YAxis(
                showgrid=True,
                showline=True,    
                title='Values',
                #range=[0, 35],
                autorange=True,        
                titlefont=Font(
                    family='Times New Roman',
                    size=12,
                    color='#000000'
                )
            ),
            width=800,
            height=600,
            margin=Margin(
                l=140,
                r=40,
                b=50,
                t=80
            ),
  )  
  

  #plot_url = py.plot(dataToPlot, filename=fileNameParam)    
  figToPlot = Figure(data=dataToPlot, layout=layoutToUse)
  fileNameParam = "plot-session-info/" + fileNameParam + ".png"
  py.image.save_as(figToPlot, fileNameParam)     
def plotDistForThreeGroups(group1, group2, group3, fileNameParam):
  import plotly.plotly as py
  import plotly.graph_objs as go
  from plotly.graph_objs import  Layout, YAxis, Figure, Margin, Font  
  #from plotly.graph_objs import Bar, Marker, Data, Layout, XAxis, YAxis, Figure, Margin, Font    
  dataToPlot = []
  g1Trace_ = go.Box(
      y= group1  , 
      name="Corr >=0.50"
    )  
  g2Trace_ = go.Box(
      y= group2  , 
      name="Corr >=0.0 AND Corr <=0.499"
    )  
  g3Trace_ = go.Box(
      y= group3  , 
      name="Corr < 0.0"
    )          
  dataToPlot = [g1Trace_, g2Trace_, g3Trace_]
  layoutToUse = Layout(
            title='Distribution of : ' + fileNameParam,
            titlefont=Font(
                    family='Times New Roman',
                    size=18,
                    color='#000000'
            ),
            yaxis=YAxis(
                showgrid=True,
                showline=True,    
                title='Values',
                #range=[0, 35],
                autorange=True,        
                titlefont=Font(
                    family='Times New Roman',
                    size=12,
                    color='#000000'
                )
            ),
            width=800,
            height=600,
            margin=Margin(
                l=140,
                r=40,
                b=50,
                t=80
            ),
  )  
  

  #plot_url = py.plot(dataToPlot, filename=fileNameParam)    
  figToPlot = Figure(data=dataToPlot, layout=layoutToUse)
  fileNameParam = "plot-session-info/"  + fileNameParam + ".png"
  py.image.save_as(figToPlot, fileNameParam)  

def plotTwoGroups( group1Param, group2Param, yAxisParam, titleParam, fileNameParam):
  import plotly.plotly as py
  import plotly.graph_objs as go
  from plotly.graph_objs import  Layout, YAxis, Figure, Margin, Font      

  group1Trace_ = go.Box(
      y= group1Param  , 
      name="High Productivity Sessions"
    )
  group2Trace_ = go.Box(
      y= group2Param  , 
      name="Low Productivity Sessions"
    ) 
  dataToPlot = [ group1Trace_, group2Trace_  ]
  layoutToUse = Layout(
            title='Summary of 84030 Sessions  : ' + titleParam,
            titlefont=Font(
                    family='Times New Roman',
                    size=18,
                    color='#000000'
            ),
            yaxis=YAxis(
                showgrid=True,
                showline=True,    
                title=yAxisParam,
                #range=[0, 35],
                autorange=True,        
                titlefont=Font(
                    family='Times New Roman',
                    size=12,
                    color='#000000'
                )
            ),
            width=800,
            height=600,
            margin=Margin(
                l=140,
                r=40,
                b=50,
                t=80
            ),
  )  

  figToPlot = Figure(data=dataToPlot, layout=layoutToUse)
  fileNameParam = "plot-session-info/" + fileNameParam + ".png"
  py.image.save_as(figToPlot, fileNameParam)   
  return "DONE!"