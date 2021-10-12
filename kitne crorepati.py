# kitna = [3000, 600000, 324990909, 90990900, 30000, 5600000, 690909090, 31010101, 532010, 510, 4100]
# i=0
# person=0
# person_1=0
# count=0
# while i<len(kitna):
#     if kitna[i]<100000:
#         count=count+1
#     elif kitna [i]>100000 and kitna [i]<10000000:
#         person=person+1
#     else:
#         person_1=person_1+1
#     i=i+1
# print("carorpati",person_1)
# print("lakhpati",person)
# print("dilwale",count)


kitna = [3000, 600000, 324990909, 90990900, 30000, 5600000, 690909090, 31010101, 532010, 510, 4100]
i=0
person=0
person_1=0
count=0
while i<len(kitna):
    if kitna[i]<100000:
        count=count+1
    elif kitna [i]>100000 and kitna [i]<10000000:
        person=person+1
    else:
        person_1=person_1+1
    i=i+1
print(person,"lakhpati")
print(person_1,"carorpati")
print(count,"dilwale")

