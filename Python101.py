#Files 

#Opening a file 
#open(argument1,argument2)
#argument1: string : name of the file 
#argument2: string : Mode of working with the file : "r" means read mode 
#open() returns a file object, which doesn't contain the contents of the file 
a=open("AnimalData.csv","r") 

#Reading in files 
b=a.read()
#b is a string which contains the contents of a 
#print(b)

#We can see that each line is separated by a "\n"
#split() function is used to split a string using a delimiter,
#and gives list of strings as output
c=b.split("\n") #converts into list of string 
rows=c[1:6]


#Loops

#for row in rows:
    #print(row)

#0 index of rows is assigned to row then the statemtment is implemented
#i.e. print(row): thus 1st row is printed, then the row at index 1 is selected
# this is how for loop works, the "row" here is a temporary variable
#only the indented part is executed as the loop


#Making a list of lists, each element of the list is a list(which is a row
#of the dataset

final_list=[]

for row in c:
    split_list=row.split(',')
    final_list.append(split_list)
#print(final_list)
#print(final_list[1])

#Accessing elements in a list manual way
#We can use double brackets to specify the elements of the list of list
print(final_list[0][0]) #Read as : print first list's first element 

#Accessing elements using loop, making list of only the ids 
id=[]

for row in final_list:
    first=row[0]
    id.append(first)
print(id)




