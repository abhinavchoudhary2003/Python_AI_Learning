# csv files stands comma separated values files  is a plain text file used to store tabular data, where each line is a row and values within a row are separated by commas (or sometimes other delimiters like tabs or semicolons).
import csv 
# use context manager with open()

# to read the csv file
# with open('names.csv','r') as csv_file:
#     csv_reader = csv.reader(csv_file)
    
#     next(csv_reader) # skips the first line

#     for line in csv_reader:
#         print(line)


# write in a csv file

#first read the original csv file 
# with open('names.csv','r') as csv_file:
#     csv_reader = csv.reader(csv_file)
# create a new csv file to write things from original file
    # with open('new_names.csv', 'w', newline='', encoding='utf-8') as new_file:
    #     csv_writer = csv.writer(new_file, delimiter='\t')

    #     for line in csv_reader:
    #         csv_writer.writerow(line) # create a new_names csv file with some modification, here changes in delimeter in original file 

# Here we are  reading the newcsv file 
# with open('new_names.csv','r') as csv_file:
#     csv_reader = csv.reader(csv_file, delimiter='\t') 

#     for line in csv_reader:
#         print(line)      





  # Working with the csv data using the dictionary reader and dictonary writer which is better than  regular reader and writer 

   # Dictonary reader   
with open('names.csv','r') as csv_file:
    csv_reader = csv.DictReader(csv_file)    

    for line in csv_reader:
        print(line) # here it will not print field names(first name) just like normal reader because here field now become as key
        


        #Dictonary Writer 
        # first read the original file 
with open('names.csv','r') as csv_file:
    csv_reader = csv.DictReader(csv_file) 
     # create a newDict file and modify that file and delete the email field(key) 
    with open('new_names_Dictfile.csv', 'w', newline='', encoding='utf-8') as new_Dictfile:
        fieldnames = ['first_name', 'last_name']

        csv_writer = csv.DictWriter(new_Dictfile,fieldnames=fieldnames, delimiter='\t')

        csv_writer.writeheader()

        for line in csv_reader:
            del line['email']
            csv_writer.writerow(line)
    


       

      






 