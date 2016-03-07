#Variable Declaration 
#Integer and Float 
a=9
b=1.9

#string
c="Sunday"

#Printing values on screeen 
print(b)

#Getting the type of the variable 
t=type(c)         #store the type of the variable in t 
print(t)          #Print the type of c
print (type(c))   #Print the type of c


#Arithmetic Operators 
two=1+1
zero=1-1
sixteen=4*4
eight=sixteen/two

#Changing the type of a variable 
int(1.6) #result: 1  int(): to convert to integer
str(1) #result: '1'  #str()- to convert to string

#Lists : Object that represents sequence of values 

l=[] #Create an empty list of name l, (l is an object of list class) 
l.append("Monday") # Use append() method to add string "Monday" to list l 
l.append(1) # Adding 1 to l, You can add different types of values in python here--> string,integer
print(l) 
#Result: ['Monday', 1]
type(l) #Result: <type 'list'> 

#Creating filled lists 
l=["Monday","Tuesday","Wednesday"]
p=[1,2,3]


#List Index : from 0 to n-1
l[0]
#result: 'Monday'

#length of lists
len(l) #this gives the number of elements in list l

#List slicing 
l=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]

l[3:5]
#Result: 'Thursday','Friday'
#The first one is included but the last one is excluded














