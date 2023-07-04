import random
import string
s1=string.ascii_letters
s2="0123456789"
s3="@#$%/._^*"
s4=s1+s2+s3
print("Welcome To Python Random Password Generator Application")
l=int(input("Enter the length of password to be generated:"))
ps="".join(random.choice(s4) for i in range(l))
print("Your password is:",ps)
