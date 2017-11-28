a=int(input())
for i in range(a):
    x=list(map(int,input().split()))
    c=0
    for i in range(x[0],x[1]):
        b=i+1
        while b<=x[1]:
            a=i&b
            if a>c:
                c=a
            b+=1
    print(c)
