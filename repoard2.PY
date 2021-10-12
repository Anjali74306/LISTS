
# marks = [[78, 76, 94, 86, 88],
#     [91, 71, 98, 65, ],
#     [95, 45, 78, ],
#     [87, 67, 49, 68, 88]]
# i=0
# sum=0
# while i<len(marks):
#     a=0
#     while a<len(marks[i]):
#         sum=sum+(marks[i][a])
#         average=sum/len(marks[i])
#         a=a+1
#     i=i+1
# print(sum)
# print(average,"of sum")



marks = [
    [78, 76, 94, 86, 88],
    [91, 71, 98, 65, 76],
    [95, 45, 78, 52, 49]
    ]


i=0
while i<len(marks):
    j=0
    sum=0
    while j<len(marks[i]):
        sum=sum+marks[i][j]
        j+=1
    print(sum//len(marks[i]))
    i+=1