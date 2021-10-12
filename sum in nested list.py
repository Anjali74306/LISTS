list=[1,[1,2,3],3,[4,5,6]]
sum=0
i=0
while i<len(list):
    b=list[i]
    if type(b) is list:
        j=0
        while j<len(b):
            sum=sum+b[j]
        j+j+1
    else:
        sum=sum+list[i]
    i=i+i
print(sum)