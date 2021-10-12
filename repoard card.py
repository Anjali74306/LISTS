# marks = [[78, 76, 94, 86, 88],
#     [91, 71, 98, 65, 76],
#     [95, 45, 78, 52, 49]]
# index=0
# sum=0
# while index<len(marks):
#     a=0
#     while a<len(marks[index]):
#         sum=sum+marks[index][a]
#         a=a+1
#     index=index+1
# print(sum)  

# marks = [[78, 76, 94, 86, 88],
#     [91, 71, 98, 65, ],
#     [95, 45, 78, ]]
# i=0
# sum=0
# while i<len(marks):
#     a=0
#     while a<len(marks[i]):
#         sum=sum+marks[i][a]
#         a=a+1
#     i=i+1
# print(sum)



marks = [[78, 76, 94, 86, 88],
    [91, 71, 98, 65, ],
    [95, 45, 78, ],
    [87, 67, 49, 68, 88]]
i=0
sum=0
while i<len(marks):
    j=0
    while j<len(marks[i]):
        sum=sum+marks[i][j]
        j=j+1
    i=i+1
print(sum)


 
    







