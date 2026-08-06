s = 'world'
if(s=='world'):
    print('True')
else:
    print("False")

nums =[1,2,3,4,5]
# for num in nums:
#     if(num==3):
#         continue
#     print(num)     
for num in nums:
    for letter in 'abc':
        print(num,letter)

print()
for i in range(1,10):
    print(i)    