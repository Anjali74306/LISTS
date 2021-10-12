num=[5,4,2,7,8,9,45,67,21,31,1,55,78,4,34,63,91,]
i=0
a=[]
b=[]
while i<len(num):
    count=0
    k=2
    while k<num[i]:
        if num[i]%k==0:
            count=count+1
        k=k+1
    if count==0:
        print(num[i],"prime")
        a.append(num[i])
    else:
        print(num[i],"not prime")
        b.append(num[i])
    i=i+1
print(a)
print(b)    


