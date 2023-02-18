s=input()
l=s.split()
for i in range(len(l)):
    for j in range(i+1,len(l)):
        m=l[i][-1]
        n=l[j][-1]
        if n<m:
            l[i],l[j]=l[j],l[i]
k=[]
for i in range(len(l)):
    k.append(l[i][:-1])
b=" ".join(k)
print(b)