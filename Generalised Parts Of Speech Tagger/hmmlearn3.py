import time
start_time = time.time()
import json, sys
import math
path = sys.argv[1]
f = open(path, encoding = 'UTF-8')
allSentences = f.read()
sentenceList = allSentences.splitlines()
wordList = [sentence.split(" ") for sentence in sentenceList]
templist = []
#tagCount will contain tags and count of tags
tagCount = {
            '_START_': len(wordList),
            '_END_': len(wordList)
        }
#wordGivenTag will contain a dictionary of tags and count of those tags appearing with words
wordGivenTag = {}
#contains transiion Probabilities
tagGivenTag = {
                    '_START_':{},
                    }

prevTag = ''
nextTag = ''
for sentence in wordList:
    prevTag = '_START_'
    for word in sentence:
        wordTag = word.split("/")#wordTag is a list of the word and the tag
        currTag = wordTag[-1]#Get the tag here
        if currTag in tagCount:
            tagCount[currTag] = tagCount[currTag] + 1
        else:
            tagCount[currTag] = 1

        observation = word[:word.rfind("/")]
        if observation in wordGivenTag:
            if currTag in wordGivenTag[observation]:#if the tag for a particular observation does'nt exist add word[:word.rfind("/")]] = 1;
                wordGivenTag[observation][currTag] = wordGivenTag[observation][currTag] + 1
            else:
                wordGivenTag[observation][currTag] = 1
        else:
             wordGivenTag[observation] = dict()
             wordGivenTag[observation][currTag] = 1   

        if prevTag in tagGivenTag:
            if currTag in tagGivenTag[prevTag]:
                tagGivenTag[prevTag][currTag] += 1
            else:
                tagGivenTag[prevTag][currTag] = 1                   
        else:
            tagGivenTag[prevTag] = dict()
            tagGivenTag[prevTag][currTag] = 1
        prevTag = currTag
        
    if prevTag in tagGivenTag:
        if '_END_' in tagGivenTag[prevTag]:
            tagGivenTag[prevTag]['_END_'] += 1
        else:
            tagGivenTag[prevTag]['_END_'] = 1                   
    else:
        tagGivenTag[prevTag] = dict()
        tagGivenTag[prevTag]['_END_'] = 1
    
def Smoothing(tagGivenTag, tagCount):#, wordGivenTag):
    smoothFact = 2#2
    leng =4*len(tagCount) -4#+ 2 #4*logtC+2
    
    for currTag in tagCount:
        tagCount[currTag] += leng
        if currTag == '_END_':
            continue
        for nextTag in tagCount:
            if nextTag == '_START_':# newAddition
                continue#newAddition
            if nextTag in tagGivenTag[currTag]:
                tagGivenTag[currTag][nextTag] += smoothFact
            else:
                tagGivenTag[currTag][nextTag] = smoothFact


Smoothing(tagGivenTag, tagCount)#, wordGivenTag) 

logFactor = 2*len(tagCount)
for currTag in tagGivenTag:
    for nextTag in tagGivenTag[currTag]:
        tagGivenTag[currTag][nextTag] = (math.log(tagGivenTag[currTag][nextTag]) + logFactor) - math.log(tagCount[currTag])

for word in wordGivenTag:
    for tag in wordGivenTag[word]:
        wordGivenTag[word][tag] = (math.log(wordGivenTag[word][tag])+ logFactor) - math.log(tagCount[tag])

writeFilePath = 'hmmmodel.txt'
writeFile = open(writeFilePath, mode = 'w', encoding = 'UTF-8')
writeFile.write(json.dumps(tagCount))
writeFile.write("\n")
writeFile.write(json.dumps(wordGivenTag))
writeFile.write("\n")
writeFile.write(json.dumps(tagGivenTag))
f.close();
print("--- %s seconds ---" % (time.time() - start_time))

