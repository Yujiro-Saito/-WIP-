#coding:utf-8
import os
import os.path
import codecs
import io,sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

directory = os.listdir("./dokujo-tsushin")
tempList = []
for file in directory:
    f = codecs.open("./dokujo-tsushin/{}".format(file),'r', 'utf-8', errors='ignore')
    lines = f.readlines()
    rmList = [w.strip() for w in lines]
    tempList.append(rmList)


articlesList = []


for list in tempList:    

    if '' in list:
        tempArr = []
        list.remove('')
        for l in list:
            if l != "":
                tempArr.append(l)
        list = tempArr      
        articlesList.append(list)
    else:
        articlesList.append(list)
        
    
    

    
print(articlesList[0])


