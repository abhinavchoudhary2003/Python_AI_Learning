# import my_module as mm
# from my_module import find_index   # it means now from this module we can only import find_index function it does not allow other methods and variables
                                     # if we try to imprt test variable it will show error 
from my_module import find_index, test   #  from my_module import * -> it will import everything from my_module  

#import sys imports the built-in sys module, which provides variables and functions used to interact directly with the Python interpreter and its operating environment.
import sys 

# when particular module is not present in the sys path or in environment variables 

# Two ways 
# import sys 
#1st way
#sys.path.append('/Users/AbhinavChoudhary/Desktop/My-modules')


#2nd way 
#is by adding that modules in our evironment variable directly so when Python starts up, it automatically reads the PYTHONPATH environment variable and adds those directory paths into sys.path
#This allows you to write import module_name from any script anywhere on your system without needing to write sys.path.append() every time!

courses = ['History','Math','Physics','CompSc']

# index = my_module.find_index(courses,'Math')
# index = mm.find_index(courses,'Math')

index = find_index(courses,'Math')
# print(test)
# print(index)

print(sys.path) #  print list of directories on my machine where python looks for modules



### Standard libraries 
import random
import math
import datetime
import calendar
import os # Accesses to underlying  os 
courses1 = ['History','Math','Physics','CompSc']

random_course = random.choice(courses)

# print(random_course)

rads = math.radians(90)
# print(rads)
# print(math.sin(rads))


today = datetime.date.today()
print(today)

print(calendar.isleap(2020))


print(os.getcwd()) # give current working directory where the current python file or script is located.It prints-> D:\Python_learning
print(os.__file__) # __file__ means dunder9(__) file Here  Python prints the absolute file path of the os.py module on your computer.
 



