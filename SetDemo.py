# we use curly brackets for set  it does not allow duplicates  and unordered 
cs_courses = {'History','Math','Physics','Compscie','Math'}
art_courses = {'History','Math','Art','Design'}
print(cs_courses.intersection(art_courses))
print(cs_courses.union(art_courses))
print(cs_courses.difference(art_courses))
# print('Math' in cs_courses)


# create an empty set 
empty_set1 = {} 
empty_set = set()
print(empty_set1) # this will print empty dictonary i.e.{}
print(empty_set) #  this will print set i.e. set()

# This works perfectly:
print(empty_set.add("Art"))

# This will crash with an AttributeError: 'dict' object has no attribute 'add'
# print(empty_set1.add("Art"))




# Works with dictionary(key:Value pair)


student = {'name':'John','age':25,'courses':['Math', 'CompSci'], 'name':'Abhi'}
print(student)
print(student['name']) 
# print(student['phone']) # shows error because this key does not  exist
print(student.get('name'))
#print(student.get('phone')) # print none because this key does not  exist

# But we can set default value of key that does not exist
print(student.get('phone','Not found'))

# key can't be duplicate if we create a new key with same name the old key value will be overridden by new  value 
student['name'] = 'Abhi'
print(student)

#update method to update the value of key 

student.update({'name':'jane', 'age':25,'phone':2424242})
print(student)


#Delete the specific key and value ]
 
# del student['name']
# print(student)

# #second way
# popped = student.pop('age')
# print(student)
# print(popped)

###################
print(len(student))
print(student.keys())
print(student.values())
print(student.items())



### looping 
# simple loop just print the keys 
# for key in student:
#     print(key)

for key,value in student.items():
    print(key,value)

