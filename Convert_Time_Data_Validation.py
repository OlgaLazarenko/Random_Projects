
#!/bin/python3

'''
Project Name: Read Text File, Change Military Time to Standard Time,
			  Write to a New Text File and Validate the Data 
Date: June 22, 2020
Author: Olga Lazarenko
Description: the purpose of the program:
			- read csv file and convert the columns with dates expressed in military time to standard time:
			  the hours will be converted to standard time, PM/AM will be added;
			- the validation of the data will be done: the rows with errors will be removed and saved at a special file;
			- Command Line Arguments (the input file, the output file,the errors file) will be passed by the user to run the code;
			- count the rows at the initial data files, at the output file, at the errors file;
			- count the rows with errors for each field			 
			 	
Specification: 1)dispatching_base_num: the values should be in the form 'B00123', the first character should be a letter and the following five
				characters should be numbers;
				2)pickup_datetime: the values should be in the format "%d/%m/%Y %H:%M" (ex: '02/15/2019 16:07')
				3)dropoff_datetime: the values should be in the format "%d/%m/%Y %H:%M"
				4)PULocation: the values should be three or less characters long, only positive decimals are allowed
				5)DOLocation: the values shold be three or less characters long, only positive decimals are allowed
				6)flag: the values can be either 1 or blank;
				

Data Source: https://data.cityofnewyork.us/Transportation/2019-High-Volume-FHV-Trip-Records/4p5c-cbgn/data
			a sample of data was used to check if the code performes properly
'''

import os
import glob
import csv
import datetime # use the module to check the datetime format
import sys # the module will allow the user to supply the command line arguments 

data_folder=sys.argv[1] #the argument/the input file passed by the user at the command line
output_file=sys.argv[2] #the output file passed as the third argument at the command line 
errors_file=sys.argv[3] # the errors file passed as the forth argument at the command line 

print()
print("Folder exists: " + str(os.path.exists(data_folder)))
#check if the input file exists 
					
print()
os.stat(data_folder)
# if the input folder doesn't exists, show the problem 

print()

os.chdir(data_folder)
all_Files=glob.glob('*.csv')

my_Files=[]
for f in all_Files:
  if f[0:8] =="TripData":
    my_Files.append(f)

print()
print("The data files: ")  #show what files in the folder 
for f in my_Files:
	print(f)
print()

data_files=[]
a=0
while a in range(len(my_Files)):
	data_files.append(data_folder + '\\'+ my_Files[a])
	a+=1
print("The full name of the files: ")#show the full names of the files in the folder 
for f in data_files:
	print(f)
print('---------------------------------------------')
#declare variables to count the rows:
initial_rows=0
output_rows=0
errors_rows=0
errors_baseID=0
errors_licenceID=0
errors_pickup=0
errors_dropoff=0
errors_PUlocation=0
errors_DOlocation=0
errors_flag=0
total_errors=0

num_loop=1 # this variable will be used to control the writing the column names to the output file, the errors file
			#this should be written to the mentioned above files once

for input_file in data_files:
	with open(input_file,'rt') as file1: #open the initial file to read from it

		with open(output_file,'a+') as file2: #create a file for the output and write to it, the next data will be appended
     
			with open(errors_file,'a+') as file3: #create a file for rows with errors, after reading each file, the errors will be appended
				header=file1.readline() #read the first row containing the columns name
				format_time='%m/%d/%Y %H:%M'
	
				if num_loop==1: # the columns name should be written to the output and errors files only once 
					file2.write(header) #write the columns name to the output file 
					file3.write(header) #write  the columns names to the errors file
				num_loop+=1

		
				for line in file1: #iterate over rows of the file

					line_list=line.split(',') #split the line/row into a list by the comma separators
					initial_rows+=1 #count the initial data rows

					licenseID=line_list[0]
					base=line_list[1] #the first item in the list, 
					a=line_list[2] #pickup_time,the second item in the list
					b=line_list[3] #drop-off time,the third element in the list
					PUlocation=line_list[4] #locationID, the forth element in the list
					DOlocation=line_list[5] 
					flag=line_list[6]
					
					
					'''validate the licenceID field,
					if an error is present,move the row to the errors file and take another row to validate;
					count the rows with this type of error unsing the variable errors_licenceID'''
					if len(licenseID)!=6 or licenseID[0:2]!="HV" or str.isnumeric(licenseID[2:])=="False":
						file3.write(line) # move the row to the error file
						errors_licenceID+=1  # count the number of rows with this error
						errors_rows+=1 # total rows with errors 
						continue #if an error is present,skip the rest of the code in the loop and take another row to validate
               
					'''validate the second element in the list, the baseID;
					count the errors at his field: errors_licenceID variable '''
					if len(base)!=6 or base[0]!= "B" or str.isnumeric(base[1:])=="False":
						file3.write(line) # move the row to the error file
						errors_baseID+=1 # count the errors at this field
						errors_rows+=1
						continue #if an error is present,skip the rest of the code in the loop and take another row to validate
					

					try: #validate the pickup date and time format
						datetime.datetime.strptime(line_list[2], format_time)
					except:
						file3.write(line) # if the datetime format is incorrect, write the row to the errors file
						errors_pickup+=1 # count the errors at this field
						errors_rows+=1
						continue
					
					try: #validate the drop-off  date and time format
						datetime.datetime.strptime(line_list[3],format_time) 

					except:	
						file3.write(line) #move the row to the error file
						errors_dropoff+=1 #count the errors at the drop-off datatime field
						errors_rows+=1
						continue 
					# create the function validate_location(locationID) to validate the PUlocation/ DOlocation
					def validate_location(locationID):
						if not locationID.isnumeric():
							file3.write(line)
						elif int(locationID) <= 0:
							file3.write(line)
						elif int(locationID) >= 1000:
							file3.write(line)
							
							

					# call the function to validate pick-up/ drop-off location
					validate_location(PUlocation)
					validate_location(DOlocation)
					
						
					#validate the next column 
					if flag.strip() != '':
						file3.write(line)
						errors_flag+=1 #count the rows with errors at the flag field
						errors_rows+=1
						continue
					
				
					hour_a=int(a[-5:-3])
					hour_b=int(b[-5:-3])
				
			
					
					def convert_to_stand_time(hour_a,hour_b): # create a function with two parameters 
						if hour_a>12:
							new_hour_a=str(hour_a-12)+ a[-3:]+" PM"  # convert to standard time and add "AM/PM" to hours
						elif hour_a<12:
							new_hour_a=str(hour_a) + a[-3:]+" AM"
						elif hour_a==12:
							new_hour_a=str(hour_a) + a[-3:] + " PM"
						elif hour_a==0:
							new_hour_a='12'+ a[-3:] + " AM"
					
						if hour_b>12:
							new_hour_b=str(hour_b-12)+ b[-3:]+" PM" 
						elif hour_b<12:
							new_hour_b=str(hour_b) + b[-3:]+" AM"
						elif hour_b==12:
							new_hour_b=str(hour_b) + b[-3:] + " PM"
						elif hour_b==0:
							new_hour_b='12'+ b[-3:] + "AM"
						return(new_hour_a, new_hour_b)
			
					new_hour_a, new_hour_b=convert_to_stand_time(hour_a, hour_b) # call the function 'convert_to_stand_time'
													
					def create_new_time(new_hour_a, new_hour_b): # the function will create new time strings for pickup and dropoff 											# pass two arguments( hour_a, hour_b) to the function
						new_a= a[0:(a.find(' ')+1)] + new_hour_a 
						new_b= b[0:(b.find(' ')+1)] + new_hour_b 
						return(new_a,new_b)
				
					new_a,new_b = create_new_time(new_hour_a,new_hour_b) # call the funtion 'create_new_time'
		
		

					def delete_insert_time(line_list): # the function will delete the 'old' time string and insert the 'new' time with AM/PM
						del line_list[2:4] # delete from the list 'old' pickup_time and dropoff_time
						line_list.insert(2,new_a) #insert into the list
						line_list.insert(3,new_b) #insert into the list
						return line_list

					line_list=delete_insert_time(line_list) # call the function
					new_str=','.join(line_list)
					file2.write(new_str) #write to the output_file
					output_rows+=1

print('The initial data (sample):')
print()				
with open(data_files[1],'rt') as file1: # read the initial file
	for i in range(0,11):# print the first ten rows
		text=file1.readline()
		print(text,end='')
print()
print('-------------------------------------------')

print("My output file: {}".format(output_file))
print()
with open(output_file,'rt') as file2:
	for i in range(0,11):
		text=file2.readline() #read the first ten rows
		print(text,end='')	
print('-------------------------------------------')
print()	
print('The errors file (sample): {}'.format(errors_file))
print()
with open(errors_file,'rt') as file3: # read some rows from the file stored the rows with errors
	for i in range(0,11):
		text=file3.readline() #read the first ten rows
		print(text, end='')
print('------------------------------------------')
print()

print(str(initial_rows)+ "  initial data rows")
print(str(output_rows)+ "  rows at the output file")
print(str(errors_rows)+ "  rows at the errors file")
print()
print("Errors: ")
print(str(errors_licenceID)+ "   licenceID field")
print(str(errors_baseID)+ "   baseID field")
print(str(errors_pickup)+ "   pick-up date/time field")
print(str(errors_dropoff)+ "   drop-off date/time field")
print(str(errors_PUlocation)+ "   pick_up location field")
print(str(errors_DOlocation)+ "   drop-off location filed")
print(str(errors_flag)+ "   flag field")
print()
