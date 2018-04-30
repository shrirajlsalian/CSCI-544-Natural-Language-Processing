import time, math
#start_time = time.time()
import json, sys, string

def openFile():
    path = sys.argv[1]
    f = open(path, encoding = 'UTF-8')
    allSentences = f.read()
    sentenceList = allSentences.splitlines()
    #print(sentenceList[22])
    stripPunctuation3(sentenceList)
    #print(sentenceList[22])
    return sentenceList


def stripPunctuation3(sentenceList):
    mypunct = string.punctuation
    mypunct = mypunct.replace("\'","")
    print(mypunct)
    punctl = list(mypunct)
    for k in range(0, len(sentenceList)):
        sentence = sentenceList[k]
        for i in range(0, len(sentence)):
            if sentence[i] in punctl:
                sentence = sentence[:i] + ' ' + sentence[i+1:]
        sentenceList[k] = sentence       

#-----------------Remove Stop Words-----------------------
def removeStopWords(sentWords):
    stopList1 = [ "a", "about", "above", "after", "again", "against", "all", "am", "an", "and", "any",
                "are", "as", "at", "be", "because", "been", "before", "being", "below", "between",
                "both", "but", "by", "could", "did", "do", "does", "doing", "down", "during", "each",
                "few", "for", "from", "further", "had", "has", "have", "having", "he", "he'd",
                "he'll", "he's", "her", "here", "here's", "hers", "herself", "him", "himself", "his",
                "how", "how's", "i", "i'd", "i'll", "i'm", "i've", "if", "in", "into", "is", "it", 
                "it's", "its", "itself", "let's", "me", "more", "most", "my", "myself", "nor", "of",
                "on", "once", "only", "or", "other", "ought", "our", "ours", "ourselves", "out", 
                "over", "own", "same", "she", "she'd", "she'll", "she's", "should", "so", "some",
                "such", "than", "that", "that's", "the", "their", "theirs", "them", "themselves",
                "then", "there", "there's", "these", "they", "they'd", "they'll", "they're",
                "they've", "this", "those", "through", "to", "too", "under", "until", "up",
                "very", "was", "we", "we'd", "we'll", "we're", "we've", "were", "what",
                "what's", "when", "when's", "where", "where's", "which", "while", "who",
                "who's", "whom", "why", "why's", "with", "would", "you", "you'd", "you'll",
                "you're", "you've", "your", "yours", "yourself", "yourselves"]
    stopList = ['her', 'during', 'than', 'or', 'an', 'after', 'him', 'in', "you'll", 'who', 'why', 'make', 'up', 'two', 'whom', 'itself', 'some', 'nor', 'his', 'under', 'which', "you've", 'each', 'many', 'ours', 'when', "where's", 'for', 'herself', 'from', 'below', 'himself', 'though', 'before', 'ourselves', 'yourselves', 'your', 'myself', 'are', 'if', 'having', 'too', 'against', 'me', 'further', 'both', 'that', 'have', 'over', 'asked', 'our', 'had', 'same', "there's", "how's", 'away', 'you', 'hers', "what's", 'yours', 'with', 'and', 'only', "you'd", 'between', 'here', 'we', 'theirs', 'is', 'do', "i'm", 'being', 'them', 'said', 'all', "i'd", 'through', 'above', 'also', 'to', 'now', 'on', 'such', "they'd", 'because', 'they', 'down', "she'll", 'i', 'would', "let's", "why's", "we'd", 'could', 'this', "that's", 'of', 'there', 'next', "they'll", "it's", "who's", 'own', "they've", 'am', 'as', 'ought', 'those', "we're", "she'd", "we'll", "here's", 'while', 'few', 'any', 'has', "he'll", "i've", 'how', 'their', 'yourself', "you're", "she's", 'its', "they're", "i'll", 'where', 'until', 'the', "he'd", 'by', 'themselves', 'so', 'was', 'other', 'into', 'quite', 'these', 'out', "we've", 'did', "he's", 'be', 'a', 'about', 'my', 'high', 'old', 'once', 'then', 'again', 'what', 'been', 'were', 'should', 'does', 'every', 'very', 'doing', 'most', "when's", 'at', 'more', 'she', 'but', 'he', 'it', 'rooms']
    for i in range(0, len(sentWords)):
        sentWords[i] = [word for word in sentWords[i] if word.lower() not in stopList ]#and not word.isdigit()]
        #print(sentWords[i])#Getting '' here HANDLE THIS
#---------------------------------------------------------

def getCounts(sentWords):
    #sentWords = [sentence.split(" ") for sentence in sentenceList]#CHANGE HERE
    #------------------Data Structures------------------------
    totalCount = len(sentenceList)
    priorProb = {'True':0, 'Fake':0, 'Pos':0, 'Neg':0}
    condProb = {'True':{}, 'Fake':{}, 'Pos':{}, 'Neg':{}}
    countClass = {'True':0, 'Fake':0, 'Pos':0, 'Neg':0}
    unique = []
    #---------------------------------------------------------
    
    for wordList in sentWords:
        labelTF = wordList[1]
        labelPN = wordList[2]
        priorProb[labelTF] += 1
        priorProb[labelPN] += 1
        for word in wordList[3:]:
            word = word.lower()#Change Here
            if word in condProb[labelTF]:
                condProb[labelTF][word] += 1
            else:
                condProb[labelTF][word] = 1
            #-----------For PN-------------------------------
            if word in condProb[labelPN]:
                condProb[labelPN][word] += 1
            else:
                condProb[labelPN][word] = 1

            if word not in unique:
                unique.append(word)
                
        countClass[labelTF] += len(wordList[3:])
        countClass[labelPN] += len(wordList[3:])
    vocabSize = len(unique)
    calcProb(priorProb, condProb, countClass, vocabSize)
    return  priorProb, condProb, countClass, vocabSize

def calcProb(priorProb, condProb, countClass, vocabSize):
    for label in condProb:
        for word in condProb[label]:
            #condProb[label][word] = condProb[label][word] / countClass[label]
            #Fr Smoothing use
            condProb[label][word] = (condProb[label][word] + 1.0) / (countClass[label] + vocabSize)
            #Taking Log probabilities
            condProb[label][word] = math.log(condProb[label][word])
    for label in priorProb:
        priorProb[label] = math.log(priorProb[label]/totalCount)
        

def writeToFile(priorProb, condProb, countClass, vocabSize):
    writeFilePath = 'nbmodel.txt'
    writeFile = open(writeFilePath, mode = 'w', encoding = 'UTF-8')
    writeFile.write(json.dumps(priorProb))
    writeFile.write("\n")
    writeFile.write(json.dumps(condProb))
    writeFile.write("\n")
    writeFile.write(json.dumps(countClass))
    writeFile.write("\n")
    writeFile.write(str(vocabSize))
    

sentenceList = openFile()
totalCount = len(sentenceList)
sentWords = [sentence.split() for sentence in sentenceList]#CHANGE HERE
removeStopWords(sentWords)
#print(sentWords[16])
priorProb, condProb, countClass, vocabSize = getCounts(sentWords)
writeToFile(priorProb, condProb, countClass, vocabSize)
print("Hey Amba!")
#print(time.time() - start_time)#comment this