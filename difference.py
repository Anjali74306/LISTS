# list=[1,2,3,4,6,8]
# list2=[1,2,3,4,9,10]
# i=0
# k=[]
# while i<len(list):
#     p=list[i]
#     if p not in list2:
#         k.append(p)
#     i=i+1
# print(k)

list1 = [1,2,3,4,5,6]
list2 = [2,3,1,0,6,7]
i=0
k=[]
while i<len(list1):
    p=list1[i]
    if p not in list2:
        k.append(p)
    i=i+1
print(k)

