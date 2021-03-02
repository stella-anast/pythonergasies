import random
i=input("Give me the number of the rows ")
i= int(i)
j=input("Give me the number of the columns ")
j=int(j)
while i<3:
 print("Wrong number of rows-Try again!")
 i=int(input("Give me the number of the rows "))
while j<3:
 print("Wrong number of columns-Try again!")
 j=int(input("Give me the number of the columns "))
count=[]
for x in range(100):
  list1=[]
  p=i*j #oi theseis tou pinaka
  if (p%2)==0: #gia tin stroggulopoisi pros ta panw
    p1=p//2
  else:
   p1=(p//2)+1
  for m in range(p): #gemizw tis mises theseis me s kai o
    if m > p1:
      list1.append("O")
    else:
      list1.append("S")
  random.shuffle(list1) #tuxaio anakatema listas
  list2=[]
  for k in range (j):
    list2.append([])
    for z in range (i):
         q=list1.pop(0)
         list2[k].append(q) #gemizw tin lista me ta stoixeia tis prwtis listas
  count.insert(x,0)
  for a in range (i):
    for b in range (j-2):
      if list2[b][a] == "S" and list2[b+1][a] == "O" and list2[b+2][a] == "S":
              count[x] += 1
  for a in range(i-2):
     for b in range(j):
        if list2[b][a] == "S" and list2[b][a+1] == "O" and list2[b][a+2] == "S":
            count[x] += 1
  for a in range (i-2):
    for b in range (j-2):
        if list2[b][a] == "S" and list2[b+1][a+1] == "O" and list2[b+2][a+2] == "S":
            count[x] += 1
sum=0
length=len(count)-1
for y in range(length):
  sum=+count[y]
avg=sum/len(count)
print("The average is: ",avg)
