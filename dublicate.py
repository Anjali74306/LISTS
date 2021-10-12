number=[19,17,34,67,67,19,17,6,5,90,6,5,89,43,11,43,1]
# [34,90,89,11,1]
i=0
a=[]
while i<len(number):
    j=0
    count=0
    while j<len(number):
        if number[i]==number[j]:
            count=count+1
            if count==2:
                if number[i] not in  a:
                    a.append(number[i])
        j=j+1
    i=i+1
print(a)               

