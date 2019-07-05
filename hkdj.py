h=int(input())
g1=1
g2=1
count=0
if (h=='0') :
    print("0")
while (count<h) :
    print(g1, end=' ')
    g3=g1+g2
    g1=g2
    g2=g3
    count+=1
