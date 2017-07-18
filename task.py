import csv
from prettytable import PrettyTable
import matplotlib.pyplot as plt

numList=[]
fruitList=[]
rottenList=[]
priceList=[]

def processNumber():
    fp=open("number.csv",'r')
    a=csv.reader(fp)

    for product in a:
        val=0
        for i in range(0,100):
            if(product[i]!=''):
                num=int(product[i])
            else:
                if val%2==0:
                    num=val
                else:
                    num=-1

            if num==val:
                numList.append(int(num))
            else:
                numList.append(int(-1))
            val=val+1
        break
    fp.close()

def processFruits():
    fp=open("fruits.csv","r")
    a=csv.reader(fp)
    for product in a:
        for i in range(0,100):
            if numList[i]==-1:
                fruitList.append("-1")
                continue
            if product[i]!='':
                fruitList.append(product[i])
            else:
                if numList==-1:
                    fruitList.append("-1")
                else:
                    shift=i-10
                    if shift<0:
                        num=10-i
                        shift=99-num
                    if product[shift]=='':
                        fruitname=fruitList[shift]
                    else:
                        fruitname=product[shift]
                    fruitList.append(fruitname)
        break
    fp.close()

def processrot():
    fp=open("rotten.csv","r")
    a=csv.reader(fp)
    for rot in a:
        for i in range(0,100):
            if rot[i]=='1':
                rottenList.append('t')
            elif rot[i]=='0':
                rottenList.append('f')
            else:
                rottenList.append(rot[i])
        break
    fp.close()

def processCost():
    fp=open("price.csv","r")
    a=csv.reader(fp)
    for cost in a:
        for i in range(0,100):
            if rottenList[i]=='t':
                priceList.append(round(float(0.00),2))
            else:
                if cost[i]=='':
                    priceList.append(round(float(10.00),2))
                else:
                    priceList.append(round(float(cost[i]),2))
        break
    fp.close()

def writeFile():
    fp=open("data.csv","a")
    a=csv.writer(fp)
    for i in range(0,100):
        itemList=[]
        num=int(numList[i])
        if num==-1:
            continue
        itemList.append(numList[i])
        itemList.append(fruitList[i])
        itemList.append(priceList[i])
        itemList.append(rottenList[i])
        a.writerow(itemList)
    fp.close()
def printData():
    x=PrettyTable(["ItemNumber","FruitName","Price","Rotten?"])
    fp=open("data.csv","r")
    a=csv.reader(fp)
    for product in a:
        x.add_row([product[0],product[1],product[2],product[3]])
    print(x)
    fp.close()

def plotData():
    x=[]
    ansList1=[]
    ansList2=[]
    y=[]
    for i in range(0,len(numList)):
        val=int(numList[i])
        if val!=-1:
            ansList1.append(numList[i])
            ansList2.append(priceList[i])
    plt.plot(ansList1,ansList2,"ro")
    plt.ylabel("PriceList")
    plt.xlabel("ItemId")
    plt.show()

processNumber()
processFruits()
processrot()
processCost()
writeFile()
printData()
plotData()
