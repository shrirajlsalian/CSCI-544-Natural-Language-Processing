import math, string
#start_time = time.time()
import json, sys

def openFile():
    path = sys.argv[1]
    f = open(path, encoding = 'UTF-8')
    allSentences = f.read()
    sentenceList = allSentences.splitlines()
    return sentenceList

def readWrittenfile():
    pathRead = 'nbmodel.txt'
    Parameters = [json.loads(x) for x in open(pathRead, mode = 'r', encoding = 'UTF-8').read().split('\n')]
    priorProb = Parameters[0]
    condProb = Parameters[1]
    countClass = Parameters[2]
    vocabSize = Parameters[3]
    return priorProb, condProb, countClass, vocabSize
    
#-------------------Strip Punctuation---------------------
#-------------------Convert to lowercase------------------
 
def stripPunctuation3(sentenceList):
    mypunct = string.punctuation
    mypunct = mypunct.replace("\'","")
    punctl = list(mypunct)
    for k in range(0, len(sentenceList)):
        sentence = sentenceList[k]
        for i in range(0, len(sentence)):
            if sentence[i] in punctl:
                sentence = sentence[:i] + ' ' + sentence[i+1:]
        sentenceList[k] = sentence  
                
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
        
def sentenceClassify(priorProb, condProb, countClass, vocabSize):
    print("Classify!")
    sentenceList = openFile()
    #print(sentenceList[10])
    stripPunctuation3(sentenceList)
    #print(sentenceList[10])
    sentWords = [sentence.split() for sentence in sentenceList]#CHANGE HERE
    removeStopWords(sentWords)
    Output = {}
    for wordList in sentWords:
        #wordList= sentWords[10]
        ID = wordList[0]
        Output[ID] = []
        labelTF, labelPN = naiveBayesClassify(wordList[1:], priorProb, condProb, countClass, vocabSize)
        Output[ID] = [labelTF, labelPN]
        #print(wordList)  
        #break
    writeFile(Output)

def naiveBayesClassify(wordList, priorProb, condProb, countClass, vocabSize):
    labelTF = ''
    labelPN = ''
    #print(priorProb)
    probability = {'True':0, 'Fake':0, 'Pos':0, 'Neg':0}
    for label in probability:
        probability[label] = priorProb[label]

    for word in wordList:
        word = word.lower() # change here
        if vocabCheck(word, condProb) == 0:#Word does not exist in corpus
            continue
        for label in probability:
            if word in condProb[label]:
                probability[label] += condProb[label][word]#probability[label] *= condProb[label][word]
            else:
                probability[label] += math.log(1.0/(countClass[label]+ vocabSize))#probability[label] *= 1/(countClass[label]+ vocabSize)
            
    if probability['True'] > probability['Fake']:
        labelTF = 'True'
    else:
        labelTF = 'Fake'
    
    if probability['Pos'] > probability['Neg']:#Accuracy and Fscore go up if only > is used, if >= is used accuracy and Fscore go down by 2 percent
        labelPN = 'Pos'
    else:
        labelPN = 'Neg'
        
    return labelTF, labelPN

def vocabCheck(word, condProb):
    c =0;
    for label in condProb:
        if word in condProb[label]:
            return 1
        c+=1
        if c==2:#No need to check twice
            return 0
    return 0

def writeFile(Output):#{ID:[TF, PN]}
    writeFilePath = 'nboutput.txt'
    writeFile = open(writeFilePath, mode = 'w', encoding = 'UTF-8')
    for ID in Output:
        temp = str(ID)+ " "+Output[ID][0]+" "+Output[ID][1]
        writeFile.write(temp+"\n")

def F1(file1, file2):
    observed = {"True":[], "Fake":[], "Pos":[], "Neg":[]}
    expected = {"True":[], "Fake":[], "Pos":[], "Neg":[]}
    f1 = open(file1, encoding = 'UTF-8')
    f2 = open(file2, encoding = 'UTF-8')

    allSentences1 = f1.read()
    sentenceList1 = allSentences1.splitlines()
    allSentences2 = f2.read()
    sentenceList2 = allSentences2.splitlines()
    for i in range(0, len(sentenceList1)):
        temp = sentenceList1[i].split()
        observed['True'].append(temp[1])
        observed['Pos'].append(temp[2])

        temp = sentenceList2[i].split()
        expected['True'].append(temp[1])
        expected['Pos'].append(temp[2])
    avg = 0
    for label in observed:
        if label == 'Neg':
            label = 'Pos'
        elif label == 'Fake':
            label = 'True'
        print(f1_score(expected[label], observed[label], average = 'macro'))
        avg += f1_score(expected[label], observed[label], average = 'macro')
    print(avg/4)
    
totalCount = 0
priorProb = {}
condProb = {}
sentenceList = openFile()
priorProb, condProb, countClass, vocabSize = readWrittenfile()
sentenceClassify(priorProb, condProb, countClass, vocabSize)
file1 = 'nboutput.txt'
file2 = 'C:\\Users\\shrir\\Documents\\USC Courses\\CSCI 544\\Coding 2\\coding-2-data-corpus\\dev-key.txt'
#F1(file1, file2)
print("Amma")