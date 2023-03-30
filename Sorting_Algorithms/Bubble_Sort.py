n=int(input("Enter size of array:"))
print("Enter array elements:")
l=map(int,input().split())
for i in range(n):
    for j in range(i+1,n):
        if l[i]>l[j]:
            l[i],l[j]=l[j],l[i]
print("Array elements after sorting:")
for i in l:
    print(i,end=" ")