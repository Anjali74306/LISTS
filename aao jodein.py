elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
i=0
even_sum=0
odd_sum=0
while i<len(elements):
    if elements [i]%2==0:
        even_sum+=elements[i]
    else:
        odd_sum+=elements[i]
    i=i+1
print("even number sum",even_sum)
print("odd number sum",odd_sum)   

    
    



