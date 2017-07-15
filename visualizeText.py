'''
Corey Scamman 11 Professor Huggard
Justin LaCapra 8 Professor Meng
CS 203
Final Project
'''
import operator
from collections import OrderedDict
from operator import itemgetter
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt



def isTalkingPoint(string, filename):
    '''
    takes in  a string and a file and turns file into list
    and checks if string is in that file and returns true if so
    >>> isTalkingPoint('america', 'bush_2001.txt')
    True
    >>> isTalkingPoint('asdasdsw', 'bush_2001.txt')
    False
    '''
    file = open(filename, 'r')
    file1 = file.read()
    file2 = file1.split()
    for i in range(len(file2)):             
        file2[i] = file2[i].strip('-,.:;!?')
        file2[i] = file2[i].lower()
    if string in file2:
        return True
    else:
        return False
            

def valuePercentage(points, total):
    '''
    Takes in an integer and a file and call totalWords
    and returns a value which represents the percent
    of how much a topic was talked about in file
    >>> valuePercentage(121,2165)
    11
    '''
    
    percent = round(((2*points)/total)*100)
    return percent

def topicAnalysis(filename):
    '''
    takes in a file and checks how much the file talks about
    6 different topics
    >>> topicAnalysis('bush_2001.txt')
    Social Ills Percent: 7
    Domestic Policy Percent: 32
    Economics Percent: 31
    Technology Percent: 7
    Democracy Percent: 15
    Foreign Affairs Percent: 7
    '''
    #converts program into 
    file = open(filename, 'r')
    file1 = file.read()
    file2 = file1.split()
    stopwords = open('stopwords.txt', 'r')
    stopwords1 = stopwords.read()
    stopwords2 = stopwords1.split()
  
    #strips our original file of punctation, makes it lowercase
    #and eliminates all stopwords and stored in list noStopWordList
    for i in range(len(file2)):             
        file2[i] = file2[i].strip('-,.:;!?')
        file2[i] = file2[i].lower()
    noStopWordList = []                     
    for i in file2:
        if i not in stopwords2 and len(i)>2:
            noStopWordList += [i]

    #initializes point variables for the 6 topics
    socialPoints = 0
    domPoints = 0
    econPoints = 0
    techPoints = 0
    demoPoints = 0
    forePoints = 0
    totalWords = len(noStopWordList)
    
    #checks for a word in the 6 topic lists
    for i in range(len(noStopWordList)):
        if isTalkingPoint(noStopWordList[i],'Social Ills') == True:
            socialPoints += 2
        elif isTalkingPoint(noStopWordList[i],'Domestic Policy') == True:
            domPoints += 2
        elif isTalkingPoint(noStopWordList[i],'Economics') == True:
            econPoints += 2
        elif isTalkingPoint(noStopWordList[i],'Technology') == True:
            techPoints += 2
        elif isTalkingPoint(noStopWordList[i],'Democracy') == True:
            demoPoints += 2
        elif isTalkingPoint(noStopWordList[i],'Foreign Affairs') == True:
            forePoints += 2
        else:
            None
            
    #prints the data
    print('Social Ills Percent: ' + str(valuePercentage(socialPoints,totalWords)))
    print('Domestic Policy Percent: ' + str(valuePercentage(domPoints,totalWords)))
    print('Economics Percent: ' + str(valuePercentage(econPoints,totalWords)))
    print('Technology Percent: ' + str(valuePercentage(techPoints,totalWords)))
    print('Democracy Percent: ' + str(valuePercentage(demoPoints,totalWords)))
    print('Foreign Affairs Percent: ' + str(valuePercentage(forePoints,totalWords)))

def plotDataBush():
    '''
    Plots a bar graph of Bush's first and last SOU.
    Y axis is percentage. X axis are the topics
    '''
    # data to plot
    n_groups = 6
    means_FirstSpeech = (7, 32, 31, 7, 15, 7)
    means_FinalSpeech = (5, 27, 14, 5, 18, 18)
     
    # create plot
    fig, ax = plt.subplots()
    index = np.arange(n_groups)
    bar_width = 0.35
    
     
    rects1 = plt.bar(index, means_FirstSpeech, bar_width,
                     alpha=0.8,
                     color='r',
                     label='First Speech')
     
    rects2 = plt.bar(index + bar_width, means_FinalSpeech, bar_width,
                     alpha=0.8,
                     color='b',
                     label='Final Speech')
     
    plt.xlabel('Talking Points')
    plt.ylabel('SOU Percentage')
    plt.title('President Bush SOU Speech Analysis')
    plt.xticks(index + bar_width, ('Social Ills','Domestic Policy','Economics','Technology','Democracy','Foreign Affairs'))
    plt.legend()
     
    plt.tight_layout()
    plt.show()

def plotDataObama():
    '''
    Plots a bar graph of Bush's first and last SOU.
    Y axis is percentage. X axis are the topics
    '''
     
    # data to plot
    n_groups = 6
    means_FirstSpeech = (2, 36, 29, 5, 12, 7)
    means_FinalSpeech = (4, 23, 17, 6, 17, 11)
     
    # create plot
    fig, ax = plt.subplots()
    index = np.arange(n_groups)
    bar_width = 0.35
    
     
    rects1 = plt.bar(index, means_FirstSpeech, bar_width,
                     alpha=0.8,
                     color='r',
                     label='First Speech')
     
    rects2 = plt.bar(index + bar_width, means_FinalSpeech, bar_width,
                     alpha=0.8,
                     color='b',
                     label='Final Speech')
     
    plt.xlabel('Talking Points')
    plt.ylabel('SOU Percentage')
    plt.title('President Obama SOU Speech Analysis')
    plt.xticks(index + bar_width, ('Social Ills','Domestic Policy','Economics','Technology','Democracy','Foreign Affairs'))
    plt.legend()
     
    plt.tight_layout()
    plt.show()


def main():
    print('   Bush 2001 SOU')
    topicAnalysis('bush_2001.txt')
    print('')
    print('   Bush 2008 SOU')
    topicAnalysis('bush_2008.txt')
    print('')
    print('   Obama 2009 SOU')
    topicAnalysis('obama_2009.txt')
    print('')
    print('   Obama 2016 SOU')
    topicAnalysis('obama_2016.txt')
    plotDataBush()
    plotDataObama()
    
    
    
import doctest
doctest.testmod()
























    
    
   
        
    


            
    
