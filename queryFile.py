import os

## Test arguments
pathToDocs = 'C:\Users\IBM_ADMIN\Documents\GitHub\Python\OPIM 311\Case3\UNGCCOPs'
doc = 'eBayUNGCRr4final.txt'
pathToQueryFile = 'C:\Users\IBM_ADMIN\Documents\GitHub\Python\OPIM 311\Case3\concepts\greenhouse_gases.txt'    
pathToConceptFiles = 'C:\Users\IBM_ADMIN\Documents\GitHub\Python\OPIM 311\Case3\concepts'

## Opens file, reads it, returns contents as string
def getDaFile(pathToDocs, doc):
    filenamePath = pathToDocs + '/' + doc
    daFile = open(filenamePath,'r')
    contents = daFile.read()
    daFile.close()
    return contents
#getDaFile(pathToDocs, doc)

## Obtains list of filenames, obtains list of words in queryfile, creates/writes 
## output file, then counts occurrences of queryfile words in files

def report(pathToDocs, pathToConceptFiles,lowercase):
## part 1 --- list of filenames under pathToDocs##
    dirList = os.listdir(pathToDocs)
    print dirList

## list of filenames in pathToConceptFiles##
    dirConceptList = os.listdir(pathToConceptFiles)
    print dirConceptList
      
## create output file and write headers ##
    myFile = open('output.txt','w')
    myFile.write('File_Name' + ',' + 'File_Length' + ',')
    for queryFileName in dirConceptList:
        myFile.write(queryFileName + ',')
    myFile.write('\n')
    
## processing it all##
    queryCounter = 0
    for queryFile in dirConceptList:
        pathToQueryFile = pathToConceptFiles + '/' + queryFile
        (filepath, queryFileName) = os.path.split(pathToQueryFile) 
        wordList = getDaFile(pathToConceptFiles, queryFileName).split()
        print wordList
        fileCounter = 0
        for filename in dirList:
            
            print filename
            fileString = getDaFile(pathToDocs, filename)
            if lowercase == True:
                loweredString = fileString.lower()
                loweredList = loweredString.split()
                #print loweredList
                daWordCount = 0
                for word in loweredList:
                    for item in wordList:
                        if word == item:
                            daWordCount = daWordCount + 1
            elif lowercase == "":
                loweredString = fileString.lower()
                loweredList = loweredString.split()
                daWordCount = 0
                for word in loweredList:
                    for item in wordList:
                        if word == item:
                            daWordCount = daWordCount + 1
            else:
                fileList = fileString.split()
                daWordCount = 0
                for word in fileList:
                    for item in wordList:
                        if word == item:
                            daWordCount = daWordCount + 1
            print daWordCount
            
## writing to output file ##
            if queryCounter == 0:
                myFile.write(filename + ',' + str(len(fileString)) + ',' + str(daWordCount))
                myFile.write('\n')
            elif queryCounter == 1:
                if fileCounter == 0:
                    myFile.close()
                    myFile = open('output.txt','a')
                    myFile.write(','','',' + str(daWordCount))
                else:
                    myFile.write(','','',' + str(daWordCount))
                myFile.write('\n')
            elif queryCounter == 2:
                if fileCounter == 0:
                    myFile.close()
                    myFile = open('output.txt','a')
                    myFile.write(','','','',' + str(daWordCount))
                else:
                    myFile.write(','','','',' + str(daWordCount))
                myFile.write('\n')
            fileCounter = fileCounter + 1        
        queryCounter = queryCounter + 1

#report(pathToDocs, pathToConceptFiles, True)