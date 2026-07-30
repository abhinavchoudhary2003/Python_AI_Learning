# file objects 


# f = open('Text.txt','r')
# print(f.mode)
# f.close()


# Using context manager Her̥e we have no need to close this file it automatically closes that file 

with open('Text.txt','r') as f:
  #  file_content = f.read() # read complete file 
   # file_content1 = f.readlines() # read all ines 
    file_content2 = f.readline() # read first line
    print(file_content2)
    

