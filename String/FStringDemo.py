first_name = 'Abhinav'
last_name = 'Choudhary'
# here we use String Formatting
# sentence = 'My name is {} {}'.format(first_name,last_name)
# print(sentence)

# FString provides us some extra functionality within a placeholders
sentence = f'My name is {first_name.upper()} {last_name.upper()}'
print(sentence)


# work with dictonary
person = {'name': 'Jenn', 'age': 23}

# sentence1 = 'My name is ' + person['name'] + ' and I am ' + str(person['age']) + ' years old.'
# print(sentence1)

# use f string 
sentence1 = f"My name is {person['name']} and I am {person['age']} years old"
print(sentence1)

# We can do  run functions, and do calculations by using FString

calculation = f'4 times 11 is equal to {4*11}'
print(calculation)

for n in range(1,11):
    sentence2 = f'The value is {n:04}' # it means 0 padded with 4 values 
    print(sentence2)


    #fString with float values 
pi = 3.14159265

sentence3 = f'Pi is equal to {pi:.4f}'
print(sentence3)




    
