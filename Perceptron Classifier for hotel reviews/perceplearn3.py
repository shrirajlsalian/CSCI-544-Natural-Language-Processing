import time
start_time = time.time()
import json, sys, string

def openFile(path):
    #path = sys.argv[1]
    f = open(path, encoding = 'UTF-8')
    allSentences = f.read()
    sentenceList = allSentences.splitlines()
    stripPunctuation3(sentenceList)
    return sentenceList

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
    stopList1 = [ "a", "about", "above", "after", "again", "against", "all", "am", "an", "and", "any", "are", "as", "at", "be", "because", "been", "before", "being", "below", "between", "both", "but", "by", "could", "did", "do", "does", "doing", "down", "during", "each", "few", "for", "from", "further", "had", "has", "have", "having", "he", "he'd", "he'll", "he's", "her", "here", "here's", "hers", "herself", "him", "himself", "his", "how", "how's", "i", "i'd", "i'll", "i'm", "i've", "if", "in", "into", "is", "it", "it's", "its", "itself", "let's", "me", "more", "most", "my", "myself", "nor", "of", "on", "once", "only", "or", "other", "ought", "our", "ours", "ourselves", "out", "over", "own", "same", "she", "she'd", "she'll", "she's", "should", "so", "some", "such", "than", "that", "that's", "the", "their", "theirs", "them", "themselves", "then", "there", "there's", "these", "they", "they'd", "they'll", "they're", "they've", "this", "those", "through", "to", "too", "under", "until", "up", "very", "was", "we", "we'd", "we'll", "we're", "we've", "were", "what", "what's", "when", "when's", "where", "where's", "which", "while", "who", "who's", "whom", "why", "why's", "with", "would", "you", "you'd", "you'll", "you're", "you've", "your", "yours", "yourself", "yourselves" ];
    stopList = ['could', 'least', 'mine', 'see', 'put', 'nevertheless', 'whereby', 'sometime', 'through', 'neither', 'every', 'thence', 'beyond', 'even', 'yourselves', 'on', 'only', 'many', 'hers', 'fify', 'seemed', 'whither', 'thickv', 'below', 'too', 'formerly', 'anyone', 'much', 'nine', 'should', 'but', 'some', 'towards', 'other', 'with', 'ourselves', 'else', 'anyway', 'everyone', 'detail', 'fill', 'herein', 'it', 'serious', 'thereupon', 'last', 'couldnt', 'thru', 'among', 'everywhere', 'their', 'de', 'seems', 'beside', 'between', 'if', 'toward', 'are', 'several', 'whoever', 'he', 'three', 'nor', 'bill', 'then', 'very', 'full', 'top', 'never', 'became', 'cant', 'without', 'these', 'since', 'etc', 'off', 'me', 'whereafter', 'somehow', 'somewhere', 'anyhow', 'out', 'own', 'after', 'ltd', 'into', 'she', 'no', 'whence', 'at', 'wherein', 'might', 'get', 'around', 'during', 'already', 'we', 'per', 'same', 'whereupon', 'become', 'front', 'hence', 'again', 'amoungst', 'of', 'while', 'yet', 'because', 'side', 'across', 'anywhere', 'something', 'eg', 'amount', 'enough', 'the', 'was', 'find', 'were', 'nothing', 'give', 'sometimes', 'how', 'more', 'thereby', 'empty', 'before', 'bottom', 'show', 'for', 'about', 'however', 'done', 'from', 'once', 'our', 'you', 'one', 'take', 'fifteen', 'itself', 'this', 'moreover', 'thin', 'both', 'amongst', 'sincere', 'cry', 'made', 'will', 'latter', 'by', 'hereupon', 'in', 'behind', 'whose', 'co', 'whether', 'con', 'ie', 'up', 'why', 'elsewhere', 'above', 'until', 'otherwise', 'that', 'namely', 'noone', 'four', 'therein', 'beforehand', 'ever', 'therefore', 'her', 'which', 'than', 'do', 'may', 'yours', 'less', 'though', 'against', 'first', 'a', 'there', 'system', 'been', 'and', 'to', 'whenever', 'is', 'back', 'eleven', 'they', 'any', 'twenty', 'being', 'us', 'whole', 'throughout', 'often', 'now', 'perhaps', 'sixty', 'herself', 'twelve', 'third', 'move', 'those', 'ours', 'not', 'mill', 'former', 'what', 'himself', 'describe', 'seem', 'still', 'all', 'together', 'seeming', 'indeed', 'found', 'had', 'keep', 'its', 'next', 'his', 'whom', 'most', 'hasnt', 'further', 'over', 'mostly', 'so', 'becomes', 'others', 'forty', 'few', 'hereafter', 'un', 'under', 'meanwhile', 'please', 'go', 'call', 'within', 'has', 'five', 'as', 'although', 'besides', 'down', 'alone', 'also', 'name', 'have', 'six', 'someone', 'fire', 'becoming', 'along', 'nobody', 'hereby', 'always', 'well', 'anything', 'when', 'two', 'upon', 'afterwards', 'them', 'be', 'inc', 'am', 'can', 'my', 'whereas', 'latterly', 'rather', 'either', 'must', 'almost', 'interest', 'thus', 'everything', 'wherever', 'part', 'none', 'ten', 'an', 'thereafter', 'would', 'nowhere', 'eight', 'another', 'cannot', 'onto', 'your', 'hundred', 'whatever']
    #print(sentWords[0][3:])
    for i in range(0, len(sentWords)):
        sentWords[i] = [word for word in sentWords[i] if word.lower() not in stopList ]#and not word.isdigit()]

def getFeatures(sentWords):#converting to lower case here
    features = []
    for wordList in sorted(sentWords):
        sentFeatures = {}
        for word in sorted(wordList[3:]):
            word = word.lower()
            if word not in sentFeatures:
                sentFeatures[word] = 1
            else:
                sentFeatures[word] += 1
        features.append(sentFeatures)
    return features

def calcActivation(feature, weights):
    activation  = 0
    #print(feature)
    #print(weights['Vanilla'])
    for word in sorted(feature):
        if word in weights['Vanilla']:
            activation += feature[word] * weights['Vanilla'][word]
        else:
            weights['Vanilla'][word] = 0
            weights['Average'][word] = 0
            activation += 0
    return activation + weights['Vanilla']['_bias_']

def updateVanillaWeights(feature, weights, label):
    #print(weights)
    for word in feature:
        #if word == '_bias_':
            #continue
        #No need to check here because your'e already doing it while generating the features
        weights[word] += label*feature[word]
   #bias needs to be updated, the above runs when only the word is present in weights
    weights['_bias_'] += label;     
        
def updateAverageWeights(feature, weights, label, avgCounter):
    for word in feature:
        #No need to check here because your'e already doing it while generating the features]
        #if word == '_bias_':
            #continue
        weights[word] += label*feature[word]*avgCounter
   #bias needs to be updated, the above runs when only the word is present in weights
    weights['_bias_'] += label*avgCounter

def calcAvgPerceptron(weightsVan, weightsAvg, counter):
    #use 
    #print(len(weightsVan))
    #print(len(weightsVan))
    #above two lines to check if valid or not
    for word in weightsAvg:
        weightsAvg[word] = weightsVan[word] - (weightsAvg[word]/counter)
    #weightsAvg['_bias_'] = weightsVan['_bias_']- (weightsAvg['_bias_']/counter)
    #No need to do this since you're already doing it in in the for loop
    #if feature used bias needs to be sseparately updated, if weights is used separate bias not required
    #Handle key not found error???
    
def trainPerceptron(sentFeatures, sentWords):
    weights = {'TrueFake':{'Vanilla':{'_bias_':0}, 'Average':{'_bias_':0}},
               'PosNeg':{'Vanilla':{'_bias_':0}, 'Average':{'_bias_':0}}}
    classificn = {'True':1, 'Fake':-1, 'Pos':1, 'Neg':-1}
    label = {'TrueFake':1, 'PosNeg':1}
    avgCounter = 1
    iterations = 20
    z = 0
    stopIterations = False
    #------------------Make a function to check if weights have converged also check if time is less than 2 minutes-------------------------------
    while(z<iterations):# or stopIterations != True):
        #print(len(sentFeatures))
        for i in range(0, len(sentFeatures)):
            
            label['TrueFake'] =  classificn[sentWords[i][1]]
            label['PosNeg'] = classificn[sentWords[i][2]]
            #print(sentFeatures[i])
            
            activation = calcActivation(sentFeatures[i], weights['TrueFake'])
            #print(label['TrueFake']*activation)
            if label['TrueFake']*activation <= 0:
                updateVanillaWeights(sentFeatures[i], weights['TrueFake']['Vanilla'], label['TrueFake'])
                updateAverageWeights(sentFeatures[i], weights['TrueFake']['Average'], label['TrueFake'], avgCounter)
                
            activation = calcActivation(sentFeatures[i], weights['PosNeg'])
            if label['PosNeg']*activation <= 0:
                updateVanillaWeights(sentFeatures[i], weights['PosNeg']['Vanilla'], label['PosNeg'])
                updateAverageWeights(sentFeatures[i], weights['PosNeg']['Average'], label['PosNeg'], avgCounter)
            
            #print(weights['TrueFake']['Vanilla'])
            #print(weights['PosNeg']['Vanilla'])
            
            avgCounter += 1
            #if avgCounter == 4:
                #break
        #print(z)
        
        z += 1
   
    calcAvgPerceptron(weights['TrueFake']['Vanilla'], weights['TrueFake']['Average'], avgCounter)
    calcAvgPerceptron(weights['PosNeg']['Vanilla'], weights['PosNeg']['Average'], avgCounter)
    
    writeToFile(weights)

def writeToFileS(weights, writeFilePath):
    pass

def writeToFile(weights):
    writeFilePath = 'vanillamodel.txt'
    writeFile = open(writeFilePath, mode = 'w', encoding = 'UTF-8')
    #print(len(weights['TrueFake']['Vanilla']), len(weights['PosNeg']['Vanilla']))
    writeFile.write(json.dumps(weights['TrueFake']['Vanilla']))
    writeFile.write("\n")
    writeFile.write(json.dumps(weights['PosNeg']['Vanilla']))
    writeFile.write("\n")
    
    writeFilePath = 'averagedmodel.txt'
    writeFile = open(writeFilePath, mode = 'w', encoding = 'UTF-8')
    #print(len(weights['TrueFake']['Average']), len(weights['PosNeg']['Average']))
    writeFile.write(json.dumps(weights['TrueFake']['Average']))
    writeFile.write("\n")
    writeFile.write(json.dumps(weights['PosNeg']['Average']))
    writeFile.write("\n")
    
path = sys.argv[1]#'C:\\Users\\shrir\\Documents\\USC Courses\\CSCI 544\\Coding 3\\coding-2-data-corpus\\train-labeled.txt'  
sentenceList = openFile(path)
sentWords = [sentence.split() for sentence in sentenceList]
removeStopWords(sentWords)
sentFeatures = getFeatures(sentWords)
trainPerceptron(sentFeatures, sentWords)
print("Hey Amba!")
#print(time.time() - start_time)