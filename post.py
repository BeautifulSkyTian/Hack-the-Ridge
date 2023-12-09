


import time

def ssc(x):
        return int(x[0])-(time.time()//86400-int(x[1]))
def sst(x):
        return int(x[0])
def sdt(x):
        return int(x[1])*-1
import csv



csvfile=0
writer=0

# date,title,text,alias
fieldnames = ['stars','date', 'title','text']

def savePost(data,writer):
        writer.writerow({
                         'stars': data[0],
                         'date': data[1],
                         'title': data[2],
                         'text': data[3]})
