if True:
    print('Statemnt is true')

if False:
    print("Doesn't print anything")    


    # So if statement works only when condition is True and if or elif conditions are false then it will print else statements 
# Comparisons:
# Equal:            ==
# Not Equal:        !=
# Greater Than:     >
# Less Than:        <
# Greater or Equal: >=
# Less or Equal:    <=
# Object Identity:  is

Language = 'java'
if(Language == 'Python'):
    print('Language is python')
elif(Language == 'java'):
    print('language is java')
else:
    print('no language found')        


print('--------------------------------------')

# Diff between == and is
a = [1,2,3]
b = [1,2,3]
print(a == b) # true here it compares the value
print(id(a))
print(id(b)) 
print(a is b) # false , here it compares the object id and both have different id's(means both are different object in memory)


print('-------------------------------------------')
    # and returns true  when btoh conditions are true
    # or return true when alteast one condition should be True
    # not make True-> False or False->True
user = 'Admin'
logged_in = False
if(user == 'Admin' and logged_in):
    print('Admin page')
else:    
    print('Bad page')    

print('------------------------------------------------')

#  conditions which always givesFalse Values:
    # False
    # None
    # Zero of any numeric type
    # Any empty sequence. For example, '', (), [].
    # Any empty mapping. For example, {}.

# condition = False
# condition = None 
# condition = 0
condition = '' # 'S' -> then it will print condition is true
if(condition):
   print('condition is true')
else:
    print('condition is false')    



    #NOTE : There is no switch case in python language 

