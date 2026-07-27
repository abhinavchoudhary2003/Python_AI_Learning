num = 3.0
print(type(num)) # check data type 


num_1 = 5
num_2 = 2
print(num_1/num_2) # Division       
print(num_1//num_2) # Floor Division (rounds float to int)
print(num_1**num_2) # Exponent  means give ans of 5^2 = 25
print(num_1 % num_2)

# Built in functions 

num_3 = -5
print(abs(num_3)) # removes the negative sign if there is one.

num_4 = 3.75
print(round(num_4)) #round function - round(value)  to the closest number
print(round(num_4,1))# returns 3.8, ie. round till  the 1 digit 


#Type Casting

num_5 = '10'
num_6 = '20'

#Type Casting to integer
num_5 = (int)(num_5)
num_6 = (int)(num_6)
print(num_5 + num_6)