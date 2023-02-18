#Problem Statement:
    Given input sentence that contains a list of words appended with an integer starting from 1.Sort the input sentence based on the appended integers and print the resultant sorted sentence
    by removing the appended integers.

#Source Code:
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

#Output
To2 Programming4 Welcome1 Python3
Welcome To Python Programming
