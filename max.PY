# numbers = [50, 40, 23, 70, 56, 12, 5, 10, 7]
# max=0
# for i in numbers:
#     if i > max :
#         max=i
# print(max)

numbers=[40,23,55,12,5,10,7]
i=0
max=0
while i<len(numbers):
    if numbers[i]>max:
        max=numbers[i]
    i=i+1
print(max)
second_max = 0
i=0
while i<len(numbers):
    if numbers[i]>second_max:
        if numbers[i]!=max:
            second_max=numbers[i]
    i=i+1
print(second_max)




                                                                                             

