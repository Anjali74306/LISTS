# num=[30,56,98,76,22,87]
# i=0
# min=0
# while i<len(num):
#     a=
#     if num[i]<min:
#         min=num[i]
#     i=i+1
numbers=[7,10,40,50,30,70]
i=0
max=0
while i<len(numbers):
    if numbers[i]>max:
        max=numbers[i]
    i=i+1
# print(max)
second_max = 0
i=0
while i<len(numbers):
    if numbers[i]>second_max:
        if numbers[i]!=max:
            second_max=numbers[i]
    i=i+1
print(second_max)



