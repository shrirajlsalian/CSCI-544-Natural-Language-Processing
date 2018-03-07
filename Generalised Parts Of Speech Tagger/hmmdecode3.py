import time
start_time = time.time()
import json, sys
pathRead = 'hmmmodel.txt'
Parameters = [json.loads(x) for x in open(pathRead, mode = 'r', encoding = 'UTF-8').read().split('\n')]
tagCount = Parameters[0]
wordGivenTag = Parameters[1]
tagGivenTag = Parameters[2]

def ViterbiAlgo(tagCount, wordGivenTag, tagGivenTag):
     pathTest = sys.argv[1]
     f = open(pathTest, encoding = 'UTF-8')
     allSentencesTest = f.read()
     sentencesListTest = allSentencesTest.splitlines()
     taggedSents = []
     for sentence in sentencesListTest:
         wordList = sentence.split()
         firstWord = wordList[0]
         Viterbi = []#Viterbi is a 3D  Dictionary containing word as the state, all tags for each state
#Calculate Viterbi for first word
         Viterbi.append({})
         States ={}
         if firstWord in wordGivenTag.keys():
             States = wordGivenTag[firstWord]
         else:
             States = tagCount
         for tag in States.keys():
             if tag == '_START_':
                 continue
             if firstWord in wordGivenTag.keys():
                 emissionProb = wordGivenTag[firstWord][tag]
             else:
                 emissionProb = 1
             Viterbi[0][tag]={}
             Viterbi[0][tag]['probability'] = tagGivenTag['_START_'][tag] * emissionProb                                               
             Viterbi[0][tag]['backpointer'] = '_START_'
        
         #Start from word 1
         for i in range(1,len(wordList)):
             word = wordList[i]
             Viterbi.append({})
             if word in wordGivenTag.keys():
                 States = wordGivenTag[word]
             else:
                 States = tagCount
             for currTag in States.keys():
                 if currTag == '_START_' or currTag == '_END_':
                     continue
                 if word in wordGivenTag.keys():
                     emissionProb = wordGivenTag[word][currTag]
                 else:
                     emissionProb = 1
                 maxProb ={'prob':0,'backpointer':''}
                 #print("Previous Keys ", Viterbi[i-1].keys())#['probability'])
                 #print("len of Viterbi", len(Viterbi[i-1]))
                 for prevTag in Viterbi[i-1].keys():#CHeck This
                     if prevTag == '_START_' or prevTag == '_END_':
                         continue
                     tempProb = Viterbi[i-1][prevTag]['probability'] * \
                                tagGivenTag[prevTag][currTag] * \
                                emissionProb
                     if(tempProb>maxProb['prob']):
                         maxProb['prob'] = tempProb
                         maxProb['backpointer'] = prevTag#Viterbi[i-1][prevTag]['backpointer']

                 Viterbi[i][currTag] = {}
                 Viterbi[i][currTag]['probability'] = maxProb['prob']
                 Viterbi[i][currTag]['backpointer'] = maxProb['backpointer']
                 
                 #print("currTag given to", i, " is", Viterbi[i][currTag])
             #print(c,"\n")
         #Do for End
         States = Viterbi[-1].keys()
         n = len(wordList)
         Viterbi.append({})
         maxProb ={'prob':0,'backpointer':''}
         for tag in States:
             if tag == '_END_':
                 continue
             tempProb = Viterbi[n-1][tag]['probability'] * \
                                tagGivenTag[tag]['_END_'] 
             if(tempProb>maxProb['prob']):
                 maxProb['prob'] = tempProb
                 maxProb['backpointer'] = tag
         Viterbi[-1]['_END_']={}
         Viterbi[-1]['_END_']['probability'] = maxProb['prob']
         Viterbi[-1]['_END_']['backpointer'] = maxProb['backpointer'] 
         taggedSents.append(tagSentence(Viterbi, wordList))

     print(len(taggedSents))
     writeFile(taggedSents)

def tagSentence(Viterbi, wordList):
    state = len(wordList)
    #print(Viterbi[state]['_END_'])
    tag = '_END_'
    iList = ""
    i = len(wordList)-1
    while i >= 0:
        #print(Viterbi[state][tag])
        iList = wordList[i]+"/"+Viterbi[state][tag]['backpointer']+" " + iList
        tag = Viterbi[state][tag]['backpointer']
        state -= 1
        i-=1
    return iList
  
def writeFile(taggedSents):
    writeFilePath = 'hmmoutput.txt'
    writeFile = open(writeFilePath, mode = 'w', encoding = 'UTF-8')
    for sentence in taggedSents:
        writeFile.write(sentence)
        writeFile.write("\n")
    
ViterbiAlgo(tagCount, wordGivenTag, tagGivenTag)
