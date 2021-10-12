# num=int(input("enetr binary number"))
# sum=0
# i=0
# while num!=0:
#     rem=num%10
#     sum=sum+rem*pow(2,i)
#     num=int(num/10)
#     i=i+1
# print("decimal number:",sum)

Binary=[1,1,1,1,1,0,0]
index=0
sum=0
num=6
while index<len(Binary):
    mean_number=Binary[num]
    sum=(2**index*mean_number)
    num=num-1
    index+=1
    sum=sum+1
print(sum)
