a=int(input())
for i in range(a):
    x=list(map(int,input().split()))
    c=0
    l,s=0,0
    if x[1]-x[0]>5:
        x[0]=x[1]-5
    for i in range(x[0],x[1]):
        b=i+1
        while b<=x[1]:
            a=i&b
            if a>c:
                #l,s=i,b
                c=a
            b+=1
    print(c)
