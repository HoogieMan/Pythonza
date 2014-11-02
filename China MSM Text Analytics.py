import re

##to do: create for loop to loop through directory of MSM articles##


##accesses file, prepares it for reading, and removes punctuation##
daFile = "C:\Users\IBM_ADMIN\Documents\Github\Python\Joe Analytics\evolutionofbeauty.txt"
textfile = open(daFile, "r")
daString = textfile.read()
daList = re.split('\W+',daString)

##zips two lists together to create a dictionary of the full text file##
seq1 = range(0,len(daList))
seq2 = daList
wordDict = dict(zip(seq2, seq1))

##accesses the keywordFile, which has words of interest (WOI) which we'll scan##
keywordFilePos = "C:\Users\IBM_ADMIN\Documents\Github\Python\Joe Analytics\\positive dictionary.txt"
keywordFileNeg = "C:\Users\IBM_ADMIN\Documents\Github\Python\Joe Analytics\\negative dictionary.txt"
textKeywordsPos = open(keywordFilePos, "r")
textKeywordsNeg = open(keywordFileNeg, "r")
keywordStringPos = textKeywordsPos.read()
keywordStringNeg = textKeywordsNeg.read()
keywordListPos = re.split('\W+',keywordStringPos)
keywordListNeg = re.split('\W+',keywordStringNeg)

## counts the number of times each word in the POSITIVE list occurs in article##
for item in keywordListPos:
    count = 0
    for word in daList:
        if item == word.lower():
            count+=1
    print "The word '" + item + "' occurs " + str(count) + " times."
            #print wordDict[word]

## counts the number of times each word in the NEGATIVE list occurs in article##
for item in keywordListNeg:
    count = 0
    for word in daList:
        if item == word.lower():
            count+=1
    print "The word '" + item + "' occurs " + str(count) + " times."
    
##