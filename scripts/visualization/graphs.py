'''
Module for collecting graph related functions.
'''

import matplotlib.pyplot as plt

def scatterMatrix(dataFrame, labelColumn):
    ''''
    Makes a so-called matrix scatter using data from dataFrame. 
    Uses the labelColumn as label and plots each category with different 
    colors/markers. 
    
    Category aware compared to pandas function. 
    
    Assumes labels are integers 0, L-1, where L is the number of unique labels
    inferred from the dataFrame[labelColumn].
    
    Assumes labelColumn is the last column to be included in scatter, preceeding 
    columns must be numeric. 
    
    Supports only first 5 numeric columns.
    '''
    N = list(dataFrame.columns).index(labelColumn) - 1
    fig, axs = plt.subplots(N,N)

    colors = ['C0','C1','C2','C4','C5']
    markers = ['x','o','+','-','.']
    
    #Number of labels
    L = len(dataFrame.loc[:,labelColumn].unique())
    
    
    #Do scatter on non diagonal axes
    for i in range(N):
        for j in range(N):
            if i == j: ## skip diagonals
                continue
            for label in range(L):
                #grab data 
                x, y = dataFrame.query(f'{labelColumn} == {label}').iloc[:,[i,j]].values.T
                #do acutal plot 
                axs[i,j].plot(x, y, marker = markers[label], color=colors[label], ls="None", alpha=0.5)

    #Do histograms on diagonal.
    for i in range(N):
        for label in range(L):
            x = dataFrame.query(f'{labelColumn} == {label}').iloc[:,i].values.T
            axs[i,i].hist(x,bins='auto', alpha=0.5, color=colors[label])
        
    return fig, axs