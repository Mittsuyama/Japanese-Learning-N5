#practice
import codecs
import random

def Change(List, x, y) :
    Temp = List[x]
    List[x] = List[y]
    List[y] = Temp

data = open('words.txt', encoding = 'utf-8').read()

i = j = 2
n = 0
Len = len(data)
Words = []
Prons = []
Meanings = []

#for k in range(0, 20):
#    print(data[k])

while i < Len:
    while data[j] != '\n' : j += 1
    Words.append(data[i : j])
    while data[j] == '\n': j+= 1 
    i = j
    
    while data[j] != '\n' : j += 1
    Prons.append(data[i : j])
    while data[j] == '\n': j+= 1
    i = j
    
    while j < Len and data[j] != '\n' : j += 1
    Meanings.append(data[i : j])
    while j < Len and data[j] == '\n': j+= 1
    i = j
    n += 1

Ord = range(0, n - 1)
for i in range(1, 500) :
    x = random.randint(0, n - 1)
    y = random.randint(0, n - 1)
    Change(Words, x, y)
    Change(Prons, x, y)
    Change(Meanings, x, y)


Out = open("practice.txt", 'w')
for w in range(0, 49) :
    Out.write(Words[w] + '\n')

Out.write('\n\n')
for k in range(0, 49) :
    Out.write(Words[k] + ' ' + Prons[k] + ' ' + Meanings[k] + '\n')