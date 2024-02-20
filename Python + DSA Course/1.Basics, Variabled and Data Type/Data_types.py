# How to check a data type of a variable and how to convert them. 
x= 55 
print(x)
print(x, type(x))
y= 66.7
print(y,type(y))
name= "Vrunda"
print(name, type(name))
bol= True
print(bol, type(bol))

marks= [34,66,55,12,990]
print(marks, type(marks))

marks_1= (34,66,55,12,990)
print(marks_1, type(marks_1))

dict_1 = {"Vrunda":75, "Charmi": 88 }
print(dict_1, type(dict_1))


x= "55"
y="10"
print(x+y)
# Returns: 5510
x= int(x)
y= int(y)
print(x+y)
# Returns: 65

a= "100.5"
print(int(a)) #throws an error
print(float(a)) # this works. 