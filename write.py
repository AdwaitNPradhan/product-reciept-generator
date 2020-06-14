import os
import csv
from datetime import datetime

grandTotal = 0
tempTotal = 0
rows = 0

name = []
price = []
quantity = []
link = []
total = []
rowFor = []


def ParseData(data:dict):
    global rows
    global grandTotal
    global tempTotal
    global name
    global price
    global quantity
    global total
    global link
    rows += 1
    name.append(data['name'])
    price.append(data['price'])
    link.append(data['link'])
    quantity.append(data['quantity'])
    tempTotal = round(int(data['price'])) * int(data['quantity'])
    total.append(tempTotal)
    grandTotal += tempTotal
    pass


def WritetoCSV(path:str):
    date = datetime.now().strftime("%d/%m/%y")
    time = datetime.now().strftime("%H:%M")
    heading = ['Date:',str(date),'Time:',str(time),]
    rowinit = ['Index','Name','Price','Quantity','Total','Link',]

    with open(path + '/Amazon Estimation list.csv','a',newline='') as f:
        writer = csv.writer(f,delimiter = ',')
        writer.writerow(heading)
        writer.writerow(rowinit)
        for row in range(rows):
            writeData = [str(row + 1), name[row], str(price[row]), str(quantity[row]), str(total[row]), link[row]]
            writer.writerow(writeData)
        grandData = ['Grand Total:', str(grandTotal)]
        writer.writerow(grandData)
    
    f.close() 
    pass


def Total():
    return grandTotal


