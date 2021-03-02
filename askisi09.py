import math
list=[]
def count(text, y):
    x=0
    for character in text:
      if character == y:
         p=ord(character) #metatrepw xaraktira se ascii
         if p%2!=0:  #tsekarw an einai monos
            x+=1
            list.append(p)
    return x
with open("test.txt") as file: #opou test.txt to arxeio sas
    text= file.read()
for y in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ": #gia kathe latiniko gramma
  b=count(text,y)
  k=set(list)
for y in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ":
   if (len(k)>0):
    perc = 100 *(count(text, y)/len(k))
    a=math.modf(perc)
    if (a[0]>0):
       print(y,":","*"*((int(a[1]))+1))
    else:
      print(y,":","*"*(int(a[1])))
