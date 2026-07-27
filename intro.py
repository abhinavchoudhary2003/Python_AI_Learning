

# String Data type 


# #message1 = 'Bobby's world' # compiler will think that string ends at Bobby so it will show error 
# # To fix this we can do this 
# message2 = "Bobby's world" # 'Bobby\'s world'
# print(message2)

# # "" and '' are same here no one have extra functionality it justa matter how we use this 
# message3 = '''hyy my name is Abhinav Choudhary
# and I am from
# Himachal 
# Pradesh'''
# print(message3)

message = 'Hello world'
print(len(message))
print(message[0])
print(message[0:5]) # print the character from oth index to 5th index but 5th index not inxluded 
print(message.upper()) 
print(message.lower())
print(message.count('e')) # count the character in a string

print(message.find('w')) # it will print the w index no 
print(message.find('Hello')) # it will print the  index of first character where it is present So here H is at 0 

#message = message.replace('Hello', 'hii') # hello world went to gc because there is no reference variable is point to this objectv 
message1 = message.replace('Hello', 'hii') # new string object message1 created 
print(message1)

# concation of string 
greeting = 'Hello'
name = 'Michael'
# message = greeting +" "+ name 
message2 = '{}, {}'.format(greeting,name) #use placeholder 
message3 = f'{greeting.upper()},{name}' # use f it will provide us some extra functionality
print(message3)

print(dir(message)) # it will tell us which methos we can use on this String