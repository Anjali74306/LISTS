# a=[]
# size=int(input("how many element you want"))
# for i in range(size):
#     var=int(input("enter number"))
#     a.append(var)
#     sum=0
# for i in range(size):
#     sum=sum+a[i]
# print("sum of list elements",sum) 

a=[]
size=int(input("how many element you want"))
i=0
sum=0
while i<size:
    var=int(input("enetr the number"))
    a.append(var)
    sum=sum+var
    i+=1
print(a,sum)

