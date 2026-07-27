#Tuples are immutuable in nature so we cannot do mutuability , we can't append or remove anything here  all other things  we can do here just like that we did in list eg looping , accessing elements , mim , max  
# we use brackets for Tuples 
tuple_1 = ('History', 'Math', 'Physics', 'CompSci')
tuple_2 = tuple_1
print(min(tuple_1))
print(tuple_2)

# tuple_1[0] = 'Art' # show error 
 #File "D:\Python_learning\Tuples.py", line 8, in <module>
    # tuple_1[0] = 'Art'
# TypeError: 'tuple' object does not support item assignment
# print(tuple_2)
# print(tuple_1) 


#  Two ways to Create an Empty tuple

tuple_list = () # 1st way 
tuple_list1 = tuple()#2nd way 
print(tuple_list)
print(tuple_list1)