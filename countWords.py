"""
   Count Word Frequency
   CSCI 203 project
   Spring 2017
   Student name(s): Corey Scamman
                    Justin LaCapra
"""
import operator
from collections import OrderedDict
from operator import itemgetter


def plotData(sorted_dic, string):

    import matplotlib.pyplot as plt; plt.rcdefaults()
    import numpy as np
    import matplotlib.pyplot as plt
     
    obj = (list(sorted_dic.keys()))
    objects = (obj[0:20]) 
    y_pos = np.arange(len(objects))
    pref = list(sorted_dic.values())
    counted = pref[0:20]
     
    plt.barh(y_pos, counted, align='center', alpha= .5)
    plt.yticks(y_pos, objects)
    plt.ylabel('Frequency')
    plt.title('Top 20 Used Words for ' + string )
     
    plt.show()
    
def countWords(filename):
    '''
    takes in a txt file filename and returns the number of unique
    words and also shows the 10 ten most used words and their count
    '''
    file = open(filename, 'r')
    text1 = file.read()
    text2 = text1.split() #text2 is list of words of SOU speech
    stopwords = open('stopwords.txt', 'r')
    stopwords1 = stopwords.read()
    stopwords2 = stopwords1.split()  #stopwords2 is list of stop words

    #Eliminates all punctuation and turns all text into lowercase
    for i in range(len(text2)):             
        text2[i] = text2[i].strip('-,.:;!?')
        text2[i] = text2[i].lower()

    #Eliminates the stop words from text2
    noStopWordList = []                     
    for i in text2:
        if i not in stopwords2 and len(i)>2:
            noStopWordList += [i]
    uniqueWords = 0
    dic = {}

    #Tallies the frequency of each unique word
    for i in range(len(noStopWordList)):    
        if noStopWordList[i] in noStopWordList:
            if(noStopWordList[i] in dic):
                dic[noStopWordList[i]] += 1
            else:
                dic[noStopWordList[i]] = 1
                uniqueWords += 1
    sorted_dic = sorted(dic.items(), key=lambda x:x[1],reverse=True)
    print('Running analysis for ' + filename)
    print('')
    print('Unique words count: ' + str(uniqueWords))
    print('Top 10 most used words and their count')
    x = 1
    y = 20
    for i in range(y):
        print(x,sorted_dic[x-1])
        x += 1
        
    plotData(OrderedDict(sorted_dic), filename)


file = (input('Please enter the name of the text file you would like to analyze\n'))
countWords(file)


        

