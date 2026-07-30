

try:
    f = open('Testfile.txt')
    print("file exist")

    # when you want to manually raise an exception using raise 
    # f = open('Currupt_file.txt')
    # if f.name == 'Currupt_file.txt':
    #     raise Exception
except  FileNotFoundError as e:
    print(e)    
    print('File does not exist')
except Exception as e:
  #  print(e)
    print('file doesnot exist')
else: # this works when your try block does not catch any exception
    print(f.read())
    f.close()
finally:
    print("finally always works whether the exception raised or not ")        



