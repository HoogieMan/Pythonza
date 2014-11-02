import os
import sys
import re
import sqlite3

def replaceNewLines(aString):
    return re.sub(r'\n{1,}',r' ',aString)

def kwicn(daTerm, docStr, n):
    return kwicword(daTerm, replaceNewLines(docStr), n)

def kwicword(daTerm, daString, n):
    leftOfdaTerm = r'(((\b\w{1,}\b[^\w]{1,}){,' + str(n) + r'})'   
    rightOfdaTerm = r'((\b[^\w]{1,}\b\w{1,}\b){,' + str(n) + r'}))'
    #leftOfdaTerm = r'(((?:\S+\s+){,' + str(n) + r'}\b)'
    #rightOfdaTerm = r'(\b(?:\s+\S+){,' + str(n) + r'}))'
    toFind = leftOfdaTerm + daTerm + rightOfdaTerm
    return re.findall(toFind,daString,re.IGNORECASE)
    print(leftOfdaTerm)

def dbkwicn(daCurs,docID,daTerm,n):
    query = "SELECT doc from docs WHERE id='" + str(docID) + "'"
    result = daCurs.execute(query)
    row = daCurs.fetchone()
    return kwicn(daTerm, str(row), n)

def listOfFirms(daCurs):
    query = "SELECT distinct firm from docs"
    result = daCurs.execute(query)
    daRows = []
    for row in result:
        print(row)
        daStr=''
        daList=[]
        for item in list(range(len(row))):
            daStr += str(row[item]) + " "
            daList.append(row[item])
        print(daStr)
        daRows.append
    return daRows
    
def listOfRTypes(daCurs):
    query = "SELECT distinct reporttype from docs"
    result = daCurs.execute(query)
    daRows = []
    for row in result:
        print(row)
        daStr=''
        daList=[]
        for item in list(range(len(row))):
            daStr += str(row[item]) + " "
            daList.append(row[item])
        print(daStr)
        daRows.append
    return daRows

def listOfYears(daCurs):
    query = "SELECT distinct year from docs"
    result = daCurs.execute(query)
    daRows = []
    for row in result:
        print(row)
        daStr=''
        daList=[]
        for item in list(range(len(row))):
            daStr += str(row[item]) + " "
            daList.append(row[item])
        print(daStr)
        daRows.append
    return daRows

def getConceptList(conceptName):
    con = sqlite3.connect('ConceptVocabularies.sqlite')
    cur = con.cursor()
    query = "SELECT cterm from concept WHERE cname='" + str(conceptName) + "'"
    result = cur.execute(query)
    daRows = []
    for row in result:
        print(row)
        daStr=''
        daList=[]
        for item in list(range(len(row))):
            daStr += str(row[item]) + " "
            daList.append(row[item])
        print(daStr)
        daRows.append
    con.close()
    return daRows

def scoreDocConceptCountScore(doc,conceptName):
    termList = getConceptList(conceptName)
    # need something to make termList an actual list of words, and not the output
    # thing from getConceptList?
    daScore = 0
    for term in termList:
        print term
        zz = re.findall(r"\b" + term + r"\b", doc, re.IGNORECASE)
        daScore = daScore + len(zz)
    return daScore

def scoreDocGroup(firm,year,rtype,cName,daCurs):
    query = "SELECT doc from docs WHERE firm='" + str(firm) + "'AND year='" + str(year) + "'AND reporttype='" + str(rtype) +"'"
    results = daCurs.execute(query)
    totalScore = 0
    for eachDoc in results:
        indScore = scoreDocConceptCountScore(eachDoc,cName)
        totalScore = totalScore + indScore
    return totalScore

def timeScores(firm,years,rtype,cName,daCurs):
    scoreList = []
    print(type(scoreList))
    for year in years:
        yearlyScore = scoreDocGroup(firm,year,rtype,cName,daCurs)
        scoreList.append(str(yearlyScore))
    return scoreList

def timeScoresIndustryReport(cName,daCurs):
    yearList = listOfYears(daCurs)
    print(yearList)
    f = open('output.txt','w')
    f.write('Concept name:' + ',' + cName + '\n')
    f.write('For years:' + ',' + ',' + 
    f.write(',' + ',')
    for row in yearList:
        f.write(str(year) + ',')
    f.write('\n' + 'Firms' + ',' + 'Report types' + '\n')
    f.write(listOfFirms(daCurs) + ',' + listOfRTypes(daCurs) + ',' + timeScores(        
    f.close()
            
        
    
