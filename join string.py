# num=["a","n","j","a","l","i"],["s","i","n","g","h"]
# a=num[0]+num[1]
# b=a
# print(b)
# s=""
# s=s.join(b)
# print(s)


name=[['a','n','j','a','l','i'],['s','i','n''g','h']]
for i in range (len(name)):
    if type (name[i]) is list:
        for j in range(len(name[i])):
            print(name[i][j],end='')
    else:
        print(name[i])      
    



    