import random
p=int(input("Give me a number "))
b=0
c=1
j=0
while p <= 0:
    print("Wrong number-Try again!")
    p=int(input("Give me a number "))
while j < p:
    s=b+c
    b=c
    c=s
    j+=1
s1=0
for i in range(0,20):
  a=random.randrange(1,b)
  if pow(a,b,b)==a:
      s1+=1
if s1==20:
    print("O",p,"oros tis akolouthias fibonacci einai o",b,"kai einai prwtos arithmos")
else:
    print("O",p,"oros tis akolouthias fibonacci einai o",b,"kai den einai prwtos arithmos")
