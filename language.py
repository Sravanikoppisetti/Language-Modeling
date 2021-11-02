"""
Language Modeling Project
Name:
Roll No:
"""

import language_tests as test

project = "Language" # don't edit this

### WEEK 1 ###

'''
loadBook(filename)
#1 [Check6-1]
Parameters: str
Returns: 2D list of strs
'''
def loadBook(filename):
    f= open(filename)
    data=f.read().splitlines()
    corpus=[]
    for i in data:
        if len(i)>0:
            #print("ss",i)
            corpus.append(i.split(' '))
    #print("c", corpus)
    return corpus


'''
getCorpusLength(corpus)
#2 [Check6-1]
Parameters: 2D list of strs
Returns: int
'''
def getCorpusLength(corpus):
    count=0
    for i in corpus:
        for j in i:
            count=count+1
    return count    


'''
buildVocabulary(corpus)
#3 [Check6-1]
Parameters: 2D list of strs
Returns: list of strs
'''
def buildVocabulary(corpus):
    unique_corpus=[]
    for i in corpus:
        for j in i:
            if j not in unique_corpus:
                unique_corpus.append(j)
    return unique_corpus


'''
countUnigrams(corpus)
#4 [Check6-1]
Parameters: 2D list of strs
Returns: dict mapping strs to ints
'''
def countUnigrams(corpus):
    count_corpus={}
    for corpus_list in corpus:
        for elements in corpus_list:
            if elements not in count_corpus:
                count_corpus[elements]=1
            else:
                count_corpus[elements]=count_corpus[elements]+1
    return count_corpus


'''
getStartWords(corpus)
#5 [Check6-1]
Parameters: 2D list of strs
Returns: list of strs
'''
def getStartWords(corpus):
    start_words_list=[]
    for corpus_list in corpus:
        if corpus_list[0] not in start_words_list:
            start_words_list.append(corpus_list[0])
    return start_words_list


'''
countStartWords(corpus)
#5 [Check6-1]
Parameters: 2D list of strs
Returns: dict mapping strs to ints
'''
def countStartWords(corpus):
    start_words={}
    for corpus_list in corpus:
        starting_word=corpus_list[0]
        if starting_word not in start_words:
            start_words[starting_word]=1
        else:
            start_words[starting_word]=start_words[starting_word]+1
    return start_words    


'''
countBigrams(corpus)
#6 [Check6-1]
Parameters: 2D list of strs
Returns: dict mapping strs to (dicts mapping strs to ints)
'''
def countBigrams(corpus):
    count_bigrams={}
    for i in range(len(corpus)):
        corpus_list=(corpus[i])
        for j in range(len(corpus_list)-1):
            word=corpus_list[j]
            if word not in count_bigrams:
                count_bigrams[word]={}
            if word in count_bigrams:
                next_word= corpus_list[j+1]
                if next_word not in count_bigrams[word]:
                    count_bigrams[word][next_word] = 0
                count_bigrams[word][next_word] += 1
    return(count_bigrams)

### WEEK 2 ###

'''
buildUniformProbs(unigrams)
#1 [Check6-2]
Parameters: list of strs
Returns: list of floats
'''
def buildUniformProbs(unigrams):
    uniform_probabilities=[]
    length=len(unigrams)
    for i in unigrams:
        prob=1/length
        uniform_probabilities.append(prob)
    return uniform_probabilities


'''
buildUnigramProbs(unigrams, unigramCounts, totalCount)
#2 [Check6-2]
Parameters: list of strs ; dict mapping strs to ints ; int
Returns: list of floats
'''
def buildUnigramProbs(unigrams, unigramCounts, totalCount):
    unigram_probs=[]
    for unique_word in unigrams:
        count_word=unigramCounts[unique_word]
        unigram_prob=(count_word/totalCount)
        unigram_probs.append(unigram_prob)
    return unigram_probs


'''
buildBigramProbs(unigramCounts, bigramCounts)
#3 [Check6-2]
Parameters: dict mapping strs to ints ; dict mapping strs to (dicts mapping strs to ints)
Returns: dict mapping strs to (dicts mapping strs to (lists of values))
'''
def buildBigramProbs(unigramCounts, bigramCounts):
    bigram_Probs={}
    for prevWord in bigramCounts:
        word=[]
        prob=[]
        for k,v in bigramCounts[prevWord].items():
            word.append(k)
            prob.append(v/unigramCounts[prevWord])
            temporary_dict={}
            temporary_dict["words"]=word
            temporary_dict["probs"]=prob
        bigram_Probs[prevWord]= temporary_dict
    return bigram_Probs


'''
getTopWords(count, words, probs, ignoreList)
#4 [Check6-2]
Parameters: int ; list of strs ; list of floats ; list of strs
Returns: dict mapping strs to floats
'''
def getTopWords(count, words, probs, ignoreList):
    wordProb= { } 
    Topwords = { } 
    for i in range(len(words)):
        if words[i] not in ignoreList:
           wordProb[words[i]] = probs[i] 
    sorted_list = sorted(wordProb, key=wordProb.get, reverse=True)
    for sort_words in sorted_list:
        if len(Topwords)<count:
           Topwords[sort_words]= wordProb[sort_words]
    return Topwords


'''
generateTextFromUnigrams(count, words, probs)
#5 [Check6-2]
Parameters: int ; list of strs ; list of floats
Returns: str
'''
from random import choices
import random
def generateTextFromUnigrams(count, words, probs):
    sentence=""
    for i in range(0,count):
        randomList = random.choices(words,weights=probs)
        #print("rr ", randomList)
        sentence= sentence + randomList[0]+" " 
    #print("ss",len(sentence))
    return sentence



'''
generateTextFromBigrams(count, startWords, startWordProbs, bigramProbs)
#6 [Check6-2]
Parameters: int ; list of strs ; list of floats ; dict mapping strs to (dicts mapping strs to (lists of values))
Returns: str
'''
def generateTextFromBigrams(count, startWords, startWordProbs, bigramProbs):
    sentence=""
    z= random.choices(startWords,weights=startWordProbs)[0]
    sentence +=z 
    for i in range(count-1):
        if (z!="."):
                x=bigramProbs[z]['words']
                y=bigramProbs[z]['probs']
                z = random.choices(x,weights=y)[0]  
                sentence+=" " +z 
                #print("z",z)
                #print("sss", sentence)
        else:
            z= random.choices(startWords,weights=startWordProbs)[0]
            sentence += " " +z 
    return sentence

### WEEK 3 ###

ignore = [ ",", ".", "?", "'", '"', "-", "!", ":", ";", "by", "around", "over",
           "a", "on", "be", "in", "the", "is", "on", "and", "to", "of", "it",
           "as", "an", "but", "at", "if", "so", "was", "were", "for", "this",
           "that", "onto", "from", "not", "into" ]

'''
graphTop50Words(corpus)
#3 [Hw6]
Parameters: 2D list of strs
Returns: None
'''
def graphTop50Words(corpus):
    return


'''
graphTopStartWords(corpus)
#4 [Hw6]
Parameters: 2D list of strs
Returns: None
'''
def graphTopStartWords(corpus):
    return


'''
graphTopNextWords(corpus, word)
#5 [Hw6]
Parameters: 2D list of strs ; str
Returns: None
'''
def graphTopNextWords(corpus, word):
    return


'''
setupChartData(corpus1, corpus2, topWordCount)
#6 [Hw6]
Parameters: 2D list of strs ; 2D list of strs ; int
Returns: dict mapping strs to (lists of values)
'''
def setupChartData(corpus1, corpus2, topWordCount):
    return


'''
graphTopWordsSideBySide(corpus1, name1, corpus2, name2, numWords, title)
#6 [Hw6]
Parameters: 2D list of strs ; str ; 2D list of strs ; str ; int ; str
Returns: None
'''
def graphTopWordsSideBySide(corpus1, name1, corpus2, name2, numWords, title):
    return


'''
graphTopWordsInScatterplot(corpus1, corpus2, numWords, title)
#6 [Hw6]
Parameters: 2D list of strs ; 2D list of strs ; int ; str
Returns: None
'''
def graphTopWordsInScatterplot(corpus1, corpus2, numWords, title):
    return


### WEEK 3 PROVIDED CODE ###

"""
Expects a dictionary of words as keys with probabilities as values, and a title
Plots the words on the x axis, probabilities as the y axis and puts a title on top.
"""
def barPlot(dict, title):
    import matplotlib.pyplot as plt

    names = []
    values = []
    for k in dict:
        names.append(k)
        values.append(dict[k])

    plt.bar(names, values)

    plt.xticks(rotation='vertical')
    plt.title(title)

    plt.show()

"""
Expects 3 lists - one of x values, and two of values such that the index of a name
corresponds to a value at the same index in both lists. Category1 and Category2
are the labels for the different colors in the graph. For example, you may use
it to graph two categories of probabilities side by side to look at the differences.
"""
def sideBySideBarPlots(xValues, values1, values2, category1, category2, title):
    import matplotlib.pyplot as plt

    w = 0.35  # the width of the bars

    plt.bar(xValues, values1, width=-w, align='edge', label=category1)
    plt.bar(xValues, values2, width= w, align='edge', label=category2)

    plt.xticks(rotation="vertical")
    plt.legend()
    plt.title(title)

    plt.show()

"""
Expects two lists of probabilities and a list of labels (words) all the same length
and plots the probabilities of x and y, labels each point, and puts a title on top.
Note that this limits the graph to go from 0x0 to 0.02 x 0.02.
"""
def scatterPlot(xs, ys, labels, title):
    import matplotlib.pyplot as plt
    fig, ax = plt.subplots()

    plt.scatter(xs, ys)

    # make labels for the points
    for i in range(len(labels)):
        plt.annotate(labels[i], # this is the text
                    (xs[i], ys[i]), # this is the point to label
                    textcoords="offset points", # how to position the text
                    xytext=(0, 10), # distance from text to points (x,y)
                    ha='center') # horizontal alignment can be left, right or center

    plt.title(title)
    plt.xlim(0, 0.02)
    plt.ylim(0, 0.02)

    # a bit of advanced code to draw a y=x line
    ax.plot([0, 1], [0, 1], color='black', transform=ax.transAxes)

    plt.show()


### RUN CODE ###

# This code runs the test cases to check your work
if __name__ == "__main__":
    # print("\n" + "#"*15 + " WEEK 1 TESTS " +  "#" * 16 + "\n")
    # test.week1Tests()
    # print("\n" + "#"*15 + " WEEK 1 OUTPUT " + "#" * 15 + "\n")
    # test.runWeek1()
    #test.testCountBigrams()
    #test.testBuildUniformProbs()
    #test.testBuildBigramProbs()
    test.testGenerateTextFromBigrams()

    ## Uncomment these for Week 2 ##
"""
    print("\n" + "#"*15 + " WEEK 2 TESTS " +  "#" * 16 + "\n")
    test.week2Tests()
    print("\n" + "#"*15 + " WEEK 2 OUTPUT " + "#" * 15 + "\n")
    test.runWeek2()
"""

    ## Uncomment these for Week 3 ##
"""
    print("\n" + "#"*15 + " WEEK 3 OUTPUT " + "#" * 15 + "\n")
    test.runWeek3()
"""