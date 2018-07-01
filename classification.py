#coding:utf-8
import os
import os.path
import codecs       
import io,sys
from janome.tokenizer import Tokenizer
from janome.analyzer import Analyzer
from janome.tokenfilter import POSKeepFilter

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')


directory = os.listdir("./topic-news")
tempList = []
for file in directory:
    f = codecs.open("./topic-news/{}".format(file),'r', 'utf-8', errors='ignore')
    lines = f.readlines()
    rmList = [w.strip() for w in lines]
    tempList.append(rmList)

#Make Stopwords
file = codecs.open("stopwords.txt","r","utf-8")
lines = file.read()
stopwords = lines.split("\n")
stoplist = ['ため','せい','それら','ならでは','あれこれ','ごと','とおり','それ','これ','これら',"ころ",'よう','こと','もの','の','さまざま','ほか','ん','さ','大','中','小',
            '高','今後','費', '.', '℃',"われわれ",'百','たち','千','万','億','円','等','用','月','日','年','その他','化','比','力',"自分",'的','当社','所','後','前',"1","2","3","4","5","6","7","8","9"]
for sw in stoplist:
    stopwords.append(sw)


articlesList = []


for list in tempList:    
    del list[0:2]
    if '' in list:
        tempArr = []
        list.remove('')
        for l in list:
            if l != "":
                tempArr.append(l)
        list = tempArr
        articlesList.append("".join(list))
    else:
        articlesList.append("".join(list))

t = Tokenizer()
tokenArr = []
finalArr = []
nounString = ""
labelStr = "__label__nine , "
processedSent = ""



for  article in articlesList:
    #Tokenization
    
    tokens = t.tokenize(article)
    nounString = ""
    processedSent = ""
    tokenArr = []
    for token in tokens:
        if token.part_of_speech[:2] == "名詞":
            tokenArr.append(token.base_form)            
        tokenArr = [w for w in tokenArr if not w in stopwords]
        nounString = " ".join(tokenArr)
        processedSent = labelStr + nounString
    finalArr.append(processedSent)

trainArr = finalArr[:617]
testArr = finalArr[617:]
trainString = "\n".join(trainArr)
testString = "\n".join(testArr)

with open("nineTrain.txt", "w", encoding='utf-8') as text_file:
    text_file.write(trainString)

with open("nineTest.txt", "w", encoding='utf-8') as text_file:
    text_file.write(testString) 
