 # "count of odd numbers .... count of even numbers ....
#  count of all the numbers .... sum of odd numbers .... sum of even numbers .... sum of all the numbers ...
#  . average of odd numbers .... average of even numbers .... average of all the numbers ka ...."
elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
i=0
count_even=0
count1_odd=0
sum_even=0
sum1_odd=0
while i<len(elements):
    if elements[i]%2==0:
        sum_even=sum_even+elements[i]
        count_even+=1
    else:
        sum1_odd=sum1_odd+elements[i]
        count1_odd+=1
    i+=1
print("even number: ",count_even)
print("odd number:",count1_odd)
print("sum of even number:",sum_even)
print("average of even numbers:",sum1_odd)
print("sum of odd number:---",sum_even//count_even)
print("average of odd numbers:---",sum1_odd//count1_odd)



