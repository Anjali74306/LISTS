name=["m","o","m"]
p=[]
i=1
while i<=len(name):
    print(name[-i])
    p.append(name[-i])
    i=i+1
if p==name:
    print("yes")
else:
    print("no")

