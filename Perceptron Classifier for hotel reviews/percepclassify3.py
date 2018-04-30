import string, time, json, sys
start_time = time.time()
from sklearn.metrics import f1_score

def openFile(path):
    #path = 'C:\\Users\\shrir\\Documents\\USC Courses\\CSCI 544\\Coding 2\\coding-2-data-corpus\\dev-text.txt'#sys.argv[1]
    f = open(path, encoding = 'UTF-8')
    allSentences = f.read()
    sentenceList = allSentences.splitlines()
    return sentenceList

def readWrittenfile(pathRead):
    print("Hey Amba!")
    #pathRead = 'C:\\Users\\shrir\\Documents\\USC Courses\\CSCI 544\\Coding 3\\averagedmodel.txt'
    Parameters = [json.loads(x) for x in open(pathRead, mode = 'r', encoding = 'UTF-8').read().splitlines()]
    print("Hey Amba Bol!")
    weights = {}
    #print(Parameters[1])
    weights['TrueFake'] = Parameters[0]
    weights['PosNeg'] = Parameters[1]
    return weights

def stripPunctuation3(sentenceList):
    mypunct = string.punctuation
    mypunct = mypunct.replace("\'","")
    punctl = list(mypunct)
    for k in range(0, len(sentenceList)):
        sentence = sentenceList[k]
        #print(sentence)
        for i in range(0, len(sentence)):
            if sentence[i] in punctl:
                sentence = sentence[:i] + ' ' + sentence[i+1:]
        sentenceList[k] = sentence  

def removeStopWords(sentWords):
    #stopList = [ "a", "about", "above", "after", "again", "against", "all", "am", "an", "and", "any", "are", "as", "at", "be", "because", "been", "before", "being", "below", "between", "both", "but", "by", "could", "did", "do", "does", "doing", "down", "during", "each", "few", "for", "from", "further", "had", "has", "have", "having", "he", "he'd", "he'll", "he's", "her", "here", "here's", "hers", "herself", "him", "himself", "his", "how", "how's", "i", "i'd", "i'll", "i'm", "i've", "if", "in", "into", "is", "it", "it's", "its", "itself", "let's", "me", "more", "most", "my", "myself", "nor", "of", "on", "once", "only", "or", "other", "ought", "our", "ours", "ourselves", "out", "over", "own", "same", "she", "she'd", "she'll", "she's", "should", "so", "some", "such", "than", "that", "that's", "the", "their", "theirs", "them", "themselves", "then", "there", "there's", "these", "they", "they'd", "they'll", "they're", "they've", "this", "those", "through", "to", "too", "under", "until", "up", "very", "was", "we", "we'd", "we'll", "we're", "we've", "were", "what", "what's", "when", "when's", "where", "where's", "which", "while", "who", "who's", "whom", "why", "why's", "with", "would", "you", "you'd", "you'll", "you're", "you've", "your", "yours", "yourself", "yourselves" ];
    stopList = ['could', 'least', 'mine', 'see', 'put', 'nevertheless', 'whereby', 'sometime', 'through', 'neither', 'every', 'thence', 'beyond', 'even', 'yourselves', 'on', 'only', 'many', 'hers', 'fify', 'seemed', 'whither', 'thickv', 'below', 'too', 'formerly', 'anyone', 'much', 'nine', 'should', 'but', 'some', 'towards', 'other', 'with', 'ourselves', 'else', 'anyway', 'everyone', 'detail', 'fill', 'herein', 'it', 'serious', 'thereupon', 'last', 'couldnt', 'thru', 'among', 'everywhere', 'their', 'de', 'seems', 'beside', 'between', 'if', 'toward', 'are', 'several', 'whoever', 'he', 'three', 'nor', 'bill', 'then', 'very', 'full', 'top', 'never', 'became', 'cant', 'without', 'these', 'since', 'etc', 'off', 'me', 'whereafter', 'somehow', 'somewhere', 'anyhow', 'out', 'own', 'after', 'ltd', 'into', 'she', 'no', 'whence', 'at', 'wherein', 'might', 'get', 'around', 'during', 'already', 'we', 'per', 'same', 'whereupon', 'become', 'front', 'hence', 'again', 'amoungst', 'of', 'while', 'yet', 'because', 'side', 'across', 'anywhere', 'something', 'eg', 'amount', 'enough', 'the', 'was', 'find', 'were', 'nothing', 'give', 'sometimes', 'how', 'more', 'thereby', 'empty', 'before', 'bottom', 'show', 'for', 'about', 'however', 'done', 'from', 'once', 'our', 'you', 'one', 'take', 'fifteen', 'itself', 'this', 'moreover', 'thin', 'both', 'amongst', 'sincere', 'cry', 'made', 'will', 'latter', 'by', 'hereupon', 'in', 'behind', 'whose', 'co', 'whether', 'con', 'ie', 'up', 'why', 'elsewhere', 'above', 'until', 'otherwise', 'that', 'namely', 'noone', 'four', 'therein', 'beforehand', 'ever', 'therefore', 'her', 'which', 'than', 'do', 'may', 'yours', 'less', 'though', 'against', 'first', 'a', 'there', 'system', 'been', 'and', 'to', 'whenever', 'is', 'back', 'eleven', 'they', 'any', 'twenty', 'being', 'us', 'whole', 'throughout', 'often', 'now', 'perhaps', 'sixty', 'herself', 'twelve', 'third', 'move', 'those', 'ours', 'not', 'mill', 'former', 'what', 'himself', 'describe', 'seem', 'still', 'all', 'together', 'seeming', 'indeed', 'found', 'had', 'keep', 'its', 'next', 'his', 'whom', 'most', 'hasnt', 'further', 'over', 'mostly', 'so', 'becomes', 'others', 'forty', 'few', 'hereafter', 'un', 'under', 'meanwhile', 'please', 'go', 'call', 'within', 'has', 'five', 'as', 'although', 'besides', 'down', 'alone', 'also', 'name', 'have', 'six', 'someone', 'fire', 'becoming', 'along', 'nobody', 'hereby', 'always', 'well', 'anything', 'when', 'two', 'upon', 'afterwards', 'them', 'be', 'inc', 'am', 'can', 'my', 'whereas', 'latterly', 'rather', 'either', 'must', 'almost', 'interest', 'thus', 'everything', 'wherever', 'part', 'none', 'ten', 'an', 'thereafter', 'would', 'nowhere', 'eight', 'another', 'cannot', 'onto', 'your', 'hundred', 'whatever']
    for i in range(0, len(sentWords)):
        sentWords[i] = [word for word in sentWords[i] if word.lower() not in stopList ]#and not word.isdigit()]

def getFeatures(sentWords):#converting to lower case here
    features = []
    for wordList in sorted(sentWords):
        sentFeatures = {}
        for word in sorted(wordList[1:]):
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
        if word in weights:
            activation += feature[word] * weights[word]
        else:
            continue
    return activation + weights['_bias_']

def percepClassify(feature, weights):
    labelTF = ''
    labelPN = ''
    
    activation = calcActivation(feature, weights['TrueFake'])
    if activation > 0:
        labelTF = 'True'
    else:
        labelTF = 'Fake'
        
    activation = calcActivation(feature, weights['PosNeg'])        
    if activation > 0:
        labelPN = 'Pos'
    else:
        labelPN = 'Neg'
    
    #Accuracy and Fscore go up if only > is used, if >= is used accuracy and Fscore go down by 2 percent
    return labelTF, labelPN
    
def sentenceClassify(sentWords, weights):
    Output = {}
    sentFeatures = getFeatures(sentWords)
    for i in range(len(sentWords)):
        #wordList= sentWords[10]
        ID = sentWords[i][0]
        Output[ID] = []
        labelTF, labelPN = percepClassify(sentFeatures[i], weights)
        Output[ID] = [labelTF, labelPN]
        #print(wordList)  
    writeFile(Output)   

def writeFile(Output):#{ID:[TF, PN]}
    writeFilePath = 'percepoutput.txt'
    writeFile = open(writeFilePath, mode = 'w', encoding = 'UTF-8')
    for ID in Output:
        temp = str(ID)+ " "+Output[ID][0]+" "+Output[ID][1]
        writeFile.write(temp+"\n")
        
def F1(file1, file2):
    observed = {"True":[], "Fake":[], "Pos":[], "Neg":[]}
    expected = {"True":[], "Fake":[], "Pos":[], "Neg":[]}
    f1 = open(file1, encoding = 'UTF-8')
    f2 = open(file2, encoding = 'UTF-8')
    #ID
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
    
print("Classify!")
path = sys.argv[2]#'C:\\Users\\shrir\\Documents\\USC Courses\\CSCI 544\\Coding 2\\coding-2-data-corpus\\dev-text.txt'#sys.argv[1]
sentenceList = openFile(path)
stripPunctuation3(sentenceList)
sentWords = [sentence.split() for sentence in sentenceList]#CHANGE HERE
removeStopWords(sentWords)

pathRead = sys.argv[1]#'C:\\Users\\shrir\\Documents\\USC Courses\\CSCI 544\\Coding 3\\vanillamodel.txt'#sys.argv[2]
weights = readWrittenfile(pathRead)
sentenceClassify(sentWords, weights)
"""
file1 = 'C:\\Users\\shrir\\Documents\\USC Courses\\CSCI 544\\Coding 2\\coding-2-data-corpus\\dev-key.txt'
file2 = 'percepoutput.txt'
F1(file1, file2)
"""
