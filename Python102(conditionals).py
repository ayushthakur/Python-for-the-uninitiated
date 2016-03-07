#To check conditions which give output as True or False
a=10
b=5
c=10
d=15

#equals to
p=(a==b)
print(p)

#greater than
q=(b>a)
print(q)

#less than equal to
r=(a<=c)
print(r)

#if statement is used to run a certain line of code only if certain conditions
#are met. Only indented set of lines are considered inside the if clause

if (a>b):
    print("the condition was met")

#for loops and if
#To check presence of a particular element in the list

cities=["Washington","Newyork","San Francisco","Las Vegas"]

for city in cities:
    if city=="Washington":
        a=11
print(a)

#To check the index of the element
index=0
counter=0

for city in cities:
    if city=="Las Vegas":
        index=counter
    counter+=1
print(index)


#Finding highest

ranks=[23,45,34,55,54,22,67,33,2,43,56]
highest=ranks[0]
for rank in ranks:
    if rank>highest:
        highest=rank
print(highest)

