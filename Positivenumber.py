#take list of integers as input from user
a = []
n = int(input("Enter number of elements: "))
for i in range(n):
    ele = int(input())
    a.append(ele)
print("Your list is",a)
#extract only postive numbers from the list
b=[]

for i in a:
    if i>0:
        b.append(i)
print("The positive numbers in the list are:",b)
        