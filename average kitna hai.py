# Write a code that works for any list, it shows the two averages as the output. One is the average of even numbers 
# and the other is the average of odd numbers from the given list.
elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
i=0
sum=0
sum1=0
count=0
count_2=0
while i<len(elements):
    if elements [i]%2==0:
        sum+=elements[i]
        count+=1
    else:
        sum1+=elements[i]
        count_2+=1
    i=i+1
print("even number sum",sum)
avg=sum/count
print("avg",avg)

print("odd number sum",sum1)
avg=sum1/count_2
print("avg",avg)

# print(count,sum//len(elements[i])


