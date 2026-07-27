
# Create a function we use def to create a function
def hello_func():
  # return 'Hello function' # treat return type as your data type so here it is return string 
   pass # pass is used when we do not want to write anything in this function and  it will shows error if we dont write anything in this function so to fix this we use pass 
#print('hello function')

#print(hello_func()) # execute the function and  print Hello function
#hello_func() # this execute the function only when we are not returning anything inside the function just write a print statement inside the function 
#print(hello_func) # print this <function hello_func at 0x000001D36C4C31C0>
print(hello_func()) # print None when we do not return anything inside the function(just write a pass ) but it will give output of print statements that we wrote inside the function 

# def greet():
#     print("Hello!") # Displays text on screen, but returns None

# result = greet()   # Prints "Hello!"
# print(result)      # Output: None

print("-----------------------------")

# passing arguments or parameters 
def hello_func1(greeting,name='default value'):
    return '{},{}'.format(greeting,name) # here return type is string so data type is string 

# Moving this to the left margin so it executes outside the function
#print(hello_func1('Hi',name='Abhi')) # here name = value changes if we dont change this  then it will print default value


print("----postional Argment keyword-------")

def student_info(*args, **kwargs):
    print(args)#print in a tuple 
    print(kwargs) # print in  dictonary

# student_info('Math','Art', name='John',age=22)

courses = ['Math','Art']  #list 
info = {'name':'john', 'age':22} #dictonary

#without Unpacking 
student_info(courses, info) #*args captures both as elements inside a tuple: (['Math', 'Art'], {'name': 'john', 'age': 22}).
                          #**kwargs stays empty {} because you didn't pass any keyword arguments (like name='john').

#with unpacking 

# *courses unpacks the list into individual positional arguments: "Math", "Art".
# *args captures them as a tuple: ('Math', 'Art').

# **info unpacks the dictionary into individual keyword arguments: name='john', age=22.
# **kwargs captures them as a dictionary: {'name': 'john', 'age': 22}.
student_info(*courses, **info)



