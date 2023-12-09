



hot = []

from post import *


with open('new.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        hot.append(row)
        print(row)

mode=1
def change(type):
    mode=type
    if mode==1:
        hot.sort(key=ssc)
    elif mode==2:    
        hot.sort(key=sdt)
    elif mode==3:
        hot.sort(key=sst)



csvfile = open('new.csv', 'w', newline='')
writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#for x in hot:
   #savePost(x,writer)


# stars,date,topic,text
def makePost(data):
    data[1]=time.time()//86400
    hot.append(data)
    if mode==1:
        hot.sort(key=ssc)
    elif mode==2:    
        hot.sort(key=sdt)
    elif mode==3:
        hot.sort(key=sst)

def getPost(index):
        return hot[index]

def updatePost(stars,index):
    hot[index][0]=str(int(hot[index][0])+stars)
    if mode==1:
        hot.sort(key=ssc)
    elif mode==2:    
        hot.sort(key=sdt)
    elif mode==3:
        hot.sort(key=sst)
     