#For loop

nums = [1,2,3,4,5]
for num in nums:
    if(num==3):
        print('found!')
#        break # break is used to break the loop here when num == 3 the loop will be break
 #       continue # skip the current iteration of loop and go to the next iteration
    print(num)
print("----------------------------------")
#Nested loop
for num in nums:
    for letter in 'abc':
        print(num,letter)   

# print in range 

# for i in range(10): # starts from o to 9
for i in range(1,11): # starts from 1 and print till 10
    print(i)


print('-------------------------------------------')
# for loops iterate through certain number of values 
# while loops  will keep going until a certain condition is met or we hit a break 

x =0
while x<10:
    if x == 5:
        break;
    print(x)
    x=x+1