import csv
import json
import os

i=0
f = open('result.txt','w')
writer = csv.writer(f)

with open('hoos.csv', newline='') as csvfile:
    fieldnames =['host','Trigger']
    reader = csv.DictReader(csvfile,delimiter=';',fieldnames=fieldnames)
    for row in reader:
        i=i+1
        descriptions=""
        if "SERVICE" in row['Trigger'].upper():
            print("***************************")
            print(i)
            print(row['host'])

        #print(row['Trigger'])
        strJson = row['Trigger']
        if strJson == 'Trigger':
            continue
        cleanJson = (strJson[:-1])[:1]+'"'+(strJson[:-1])[1:]
        y=json.loads(cleanJson)
        #print(cleanJson)
        #print("***********************")
        for row2 in y['result']:
            #print(row2)
            if "SERVICE" in row2['description'].upper():
                descriptions =descriptions+ ", \""+ str(row2['description'])+ "\""
            #print("$$$$$$$$$$")
        #print("***********************")
        #print(y['result'][1])
        #z=json.loads(y['triggerid'])
        f.writelines(row['host']+" "+descriptions+"\n")

