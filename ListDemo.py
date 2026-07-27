# we use square backets for list 
courses = ['History','Math','Physics','CompSci']
courses_2 = ['Art', 'Geo']
nums = [1,2,4,3,7,5,6]

#Slicing
# print(courses[3]) # print 3rd index value
# print(courses[0:2]) # print(courses[:2]) Print list  values from 0th to 1st index [0:2]here 2nd index not included 
# print(courses[2:4])# print(courses[2:]) print list values frm 2nd index to last index 

print("-----------------------------")

# courses.append('Art')
# courses.insert(0,'Art')
# courses.insert(-1,'Geo') # -1 means put thi value at last index 
# courses.insert(1,courses_2) # add list directly in 1st list
# courses.append(courses_2)  # add list directly in 1st list
#courses.extend(courses_2) # add individual elements of 2nd list in 1st list 
print(courses)

print('---------------------------------------------')
#courses.pop()# it removes the 1st index value if we set  pop(1) #  By default , it removes the last index value  
# popped = courses.pop() # to get the value who is removed 
# print(popped)
# print(courses)
# courses.reverse()
# print(courses)
# courses.sort() #['CompSci', 'History', 'Math', 'Physics']
# courses.sort(reverse=True) # ['Physics', 'Math', 'History', 'CompSci'] sort in descending order

# sorted_courses= sorted(courses) # this method will not affect the original list 
# print(sorted_courses)


# print(min(nums))
# print(max(nums))
# print(sum(nums))
 
#print(courses.index('CompSci')) # find the index of value 


print('----------------------------')\

#looping
# for course in courses:
#     print(course)

# for index,course in enumerate(courses):
#     print(index,course)    

# for index,course in enumerate(courses, start=1): # start with the index of 1
#     print(index,course)  


print('--------------------')

# convert list into string and separated by certain value we use join() method

# course_str = ','.join(courses)
# print(course_str)

# convert string to list by certain value using .split() method
# new_list = course_str.split(',')
# print(new_list)


# List are mutuable 
list_1 = ['History','Math','Physics','CompSci']
list_2 = list_1

print(list_1)
print(list_2)

list_1[0] = 'Art'
print(list_1)
print(list_2)

#  Two ways to Create an Empty list  
list_empty = []
list_empty1 = list()
print(list_empty)
print(list_empty1)



