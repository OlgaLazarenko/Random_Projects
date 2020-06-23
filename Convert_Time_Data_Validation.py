

'''
Project Name: Read Text File, Change Military Time to Standard Time,
			  Write to a New Text File and Validate the Data 
Date: June 22, 2020
author: Olga Lazarenko
Description: the program will read csv file and convert the columns with dates expressed in military time to standard time:
			 the hours will be converted to standard time, PM/AM will be added;
			 the validation of the data will be done, the rows with errors will be removed and saved at a special file 
			 	
Specification: 1)dispatching_base_num: the values should be in the form 'B00123', the first character should be a letter and the following five
				characters should be numbers;
				2)pickup_datetime: the values should be in the format "%d/%m/%Y %H:%M" (ex: '02/15/2019 16:07')
				3)dropoff_datetime: the values should be in the format "%d/%m/%Y %H:%M"
				4)PULocation: the values should be three or less characters long, only positive decimals are allowed
				5)DOLocation: the values shold be three or less characters long, only positive decimals are allowed
				

Data Source: https://data.cityofnewyork.us/Transportation/2019-High-Volume-FHV-Trip-Records/4p5c-cbgn/data
			a sample of data was used to check if the code performes properly
'''

import os
import csv
import datetime # use the module to check the datetime format

print()
print("File exists:  " + str(os.path.exists('E://_Python_Projects/GitHub_Random_Projects/Data_Files/TripData_2.csv')))
#check if the file exsists

print()
os.stat('E://_Python_Projects//GitHub_Random_Projects/Data_Files/TripData_2.csv') 
# if the file doesn't exists, show the problem 

print()


with open('E://_Python_Projects/GitHub_Random_Projects/Data_Files/TripData_2.csv','rt') as file: #open the initial file to read from it

	with open('E://_Python_Projects/GitHub_Random_Projects/Data_Files/TripData_2_Output.csv','w') as new_file: #create a file for the output and write to it
		
		with open('E://_Python_Projects/GitHub_Random_Projects/Data_Files/TripData_2_Errors.csv','w') as errors_file: #create a file for rows with errors

			header=file.readline() #read the first row containing the columns name
			new_file.write(header) #write to the output file the columns name 
			errors_file.write(header) #write to the errors file the comlumns name
		
		
			for line in file: #iterate over rows of the file
			
				format_time ="%d/%m/%Y %H:%M" # the pickup and the dropoff time should be in this format

				line_list=line.split(',') #split the line/row into a list by the comma separators
				
				base=line_list[0] #the first item in the list, 
				a=line_list[1] #pickup_time,the second item in the list
				b=line_list[2] #dropoff time,the third element in the list
				location=line_list[3] #locationID, the forth element in the list
				
			
				#validate the first element in the list, the base ID
				if len(base)!=6 or base[0]!='B' or str.isdecimal(base[1:])=="False":
					errors_file.write(line) # move the row to the error file
					continue #if an errow is present,skip the rest of the code in the loop and take another row to validate
					
				try:
					datetime.datetime.strptime(line_list[1], format_time)
				except:
					errors_file.write(line) # if the datetime format is incorrect, write the row to the errors file
					continue
				
				try:
					datetime.datetime.strptime(line_list[2],format_time)
				except:	
					errors_file.write(line) #move the row to the error file
					continue
					
				if len(line_list[3])!=3  or str.isdecimal(line_list[3])=="False": 
					errors_file.write(line)
					continue
					
					
				
				a_part1=line_list[1][0:(line_list[1].find(' ')+1)] # month-day-year part for the pickup datetime values 
				b_part1=line_list[2][0:(line_list[2].find(' ')+1)] #month-day-year part for the dropoff datetime values
				
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
														
				def create_new_time(new_hour_a, new_hour_b): # create new time string for pickup and dropoff 											# pass two arguments( hour_a, hour_b) to the function
					new_a= a[0:(a.find(' ')+1)] + new_hour_a 
					new_b= b[0:(b.find(' ')+1)] + new_hour_b 
					return(new_a,new_b)
			
				new_a,new_b = create_new_time(new_hour_a,new_hour_b) # call the funtion 'create_new_time'
			
			
				def delete_insert_time(line_list): # the function will delete the 'old' time string and insert the 'new' time with AM/PM
					del line_list[1:3] # delete form the list 'old' pickup_time and dropoff_time
				
					line_list.insert(1,new_a) #insert into the list
					line_list.insert(2,new_b) #insert into the list
					return line_list
			
				line_list=delete_insert_time(line_list) # call the function
				new_str=','.join(line_list)
				#print(new_str,end='')
			
				new_file.write(new_str)

print('The initial data (sample):')
print()				
with open('E://_Python_Projects/GitHub_Random_Projects/Data_Files/TripData_2.csv','rt') as file: # read the initial file
	for i in range(1,11):# print the first ten rows
		text=file.readline()
		print(text,end='')
print('-------------------------------------------')

print()
print()
print('The output data (sample) with standard time format:')
print()
with open('E://_Python_Projects/GitHub_Random_Projects/Data_Files/TripData_2_Output.csv','r') as new_file:  # read some rows from the output file with validated values                  
	for i in range(1,11):
		new_text=new_file.readline() #read the first ten rows
		print(new_text,end='')	
print('-------------------------------------------')
print()	
print('The errors file (sample):')
print()
with open('E://_Python_Projects/GitHub_Random_Projects/Data_Files/TripData_2_Errors.csv','r') as errors_file: # read some rows from the file stored the rows with errors
	for i in range(1,11):
		errors=errors_file.readline() #read the first ten rows
		print(errors, end='')
print('------------------------------------------')

