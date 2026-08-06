#Exercise 1. Print first 10 natural numbers using while loop

# x =1
# while(x<=10):
#     print(x)
#     x+=1


#Exercise 2. Display numbers from -10 to -1 using for loop

# for i in range(-10,0):
#     print(i)

# Exercise 3: Write a program to display a message “Done” after the successful execution of a for loop that iterates from 0 to 4.

# for i in range(5):
#     print(i)
# else:
#     print("done!")    


# Exercise 4. Write a program that accepts a number from the user and calculates the sum of all numbers from 1 up to that number.
# Take input from user and convert to integer
# number = int(input("Enter a number:"))

# sum =0
# for i in range(1, number+1):
#     sum = sum + i

# print(sum)


# Excercise 5. Create a program that takes an integer and prints its multiplication table from 1 to 10.

# number = 2

# for i in range(1,11):
#     print(str(number)+' * '+str(i)+' = '+ str(number*i))


#Exercise 6. Write a program that takes an integer n and prints the cube of every number from 1 to n in the format Current Number is : 1 and the cube is 1.

# n = int(input())
# for i in range(1,n+1):
#     print('Current Number is : '+str(i)+ ' and the cube is '+str(i**3)) # i**3 means i*i*i

        
# Exercise 7. Practice Problem: Given a list of numbers, iterate through it and print numbers that satisfy these conditions:
           # The number must be divisible by five.
           # If the number is greater than 150, skip it and move to the next.
           # If the number is greater than 500, stop the loop entirely.

# numbers = [12, 75, 150, 180, 145, 525, 50]         
 
# for num in numbers:
#     if num >500:
#         break
#     if num >150:
#         continue    
#     if num % 5 ==0:
#         print(num)

# Exercise 8. Given a list of numbers, use a loop to count how many times a specific number (e.g., 10) appears.

# list1 = [10, 20, 10, 30, 10, 40, 50]
# target = 10
# count =0
# for i in list1:
#     if(i==target):
#         count +=1
# print(f'{target} appears {count} times')       


# Practice Problem9: Given a Python list, use a loop to print only the elements that are located at odd index positions (index 1, 3, 5, etc.).

# my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# new_list= []
# for i in range(1, len(my_list), 2):
#     print(my_list[i], end =" ")
            

 # Exercise10:  Given a list, iterate it in reverse order and print each element.

# list1 = [10, 20, 30, 40, 50]
# for i in range(len(list1)-1,-1): it means strat at 4, step forward by +1, stop before -1
# But 4 is already bigger than -1 — and you're stepping forward (adding 1 each time), so you'll never reach -1 by going up. Python can't get there, so the range is empty.
# for i in range(len(list1)-1,-1): # "Start at 4, step backward by -1 each time, stop before reaching -1 (i.e., stop once you pass 0)."
#     print(list1[i], end =" ")
# print()
# for item in reversed(list1):
#     print(item, end=" ")     


# Exercise11: Reverse a string using a for loop

# Original='Python'
# reversed = ''

# for i in range(len(Original)-1,-1,-1):
#     reversed += Original[i]
# print(reversed)
# print(Original)    


# Exercise12:  Write a program that counts the total number of vowels and consonants in a given sentence, ignoring spaces and special characters.

# alphabets = "Loops are Fun!"
# vowels = 0
# Consonants = 0
# for i in range(0,len(alphabets)):
#     if(alphabets[i]== ' 'or alphabets[i]== '!'):
#         continue
#     if(alphabets[i]=='a'or alphabets[i]=='e'or alphabets[i]=='o'or alphabets[i]=='u'or alphabets[i]=='i'):
#         vowels+=1
#     else:
#         Consonants+=1    
# print(vowels)
# print(Consonants)

#  use .isalpha() : .isalpha() is a built-in string method that checks whether a character (or string) consists only of alphabetic letters — and returns True or False. 

sentence = "Loops are Fun!"
vowels = "aeiou"
v_count = 0
c_count = 0

for char in sentence.lower():
    if char.isalpha():  # Only process letters
        if char in vowels:
            v_count += 1
        else:
            c_count += 1

print(f"Vowels: {v_count}")
print(f"Consonants: {c_count}")

