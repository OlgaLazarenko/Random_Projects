

'''
Project Name: Read Text File, Change Military Time to Standard Time,
			  Write to a New Text File
<<<<<<< HEAD
Date: June 6, 2020
author: Olga Lazarenko
Description: the program will read csv file and convet the columns with dates expressed in military time to standard time:
			 the hours will be converted to standard time, PM/aM will be added;
			 command line arguments (the input file, the output file) will be passed by the user to run the code
=======
Date: june 6 2020
author: Olga Lazarenko
Description: the program will read csv file and convet the columns with dates expressed in military time to standard time:
			 the hours will be converted to standard time, PM/aM will be added:
       the user passes the input file and the output file as the command line arguments
>>>>>>> 165d2428a3d16900d1556668ebfb30a22f086efd
			 
Data Source: https://data.cityofnewyork.us/Transportation/2019-High-Volume-FHV-Trip-Records/4p5c-cbgn/data
			a sample of data was used to check if the code performes properly
'''

import os
import csv
<<<<<<< HEAD
import sys 

input_file=sys.argv[1] #the argument/the input file passed by the user at the command line
output_file=sys.argv[2] #the output file passed as the third argument at the commmand line by the user 
# E://_Python_Projects/GitHub_Random_Projects/Data_Files/NYC_TripData.csv

print("File exists:  " + str(os.path.exists(input_file)))
#check if the file exsists
=======
import sys

'''the input file: C:\OLGA_PROJECTS\Python_Projects\Random_Projects\Data_Files\NYC_TripData_2019_11_Sample.csv
the output file: C:\\OLGA_PROJECTS\\Python_Projects\\Random_Projects\\Data_Files\\NYC_TripData_2019_11_Output.csv '''


input_file=sys.argv[1] # the input file argument
output_file=sys.argv[2] # the output file argument

print("File exists:  " + str(os.path.exists(input_file)))
>>>>>>> 165d2428a3d16900d1556668ebfb30a22f086efd

print()
os.stat(input_file) 
# if the file doesn't exists, show the problem 
print('------------')
print()


		# while True:
			# line=file.readline()
			# line_list=line.split(',')
			
			# if not line:
				# break
		# print()
	# i = 0
	# for line in file:
		# i += 1
		# print(str(i) + ' - ' + line, end=' ')



with open(input_file,'rt') as file:

	with open(output_file,'w') as new_file:
		print()
		header=file.readline()
		new_file.write(header)
		
		for line in file:
			line_list=line.split(',')
			a=line_list[1] #pickup_time
			b=line_list[2] #dropoff time

			a_part1=a[0:(a.find(' ')+1)] # month-day-year part
			b_part1=b[0:(b.find(' ')+1)]
			
			hour_a=int(a[-5:-3]) # hour part
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
			
<<<<<<< HEAD
			new_a,new_b = create_new_time(new_hour_a,new_hour_b) # call the funtion 'create_new_time'
=======
			new_a,new_b = create_new_time(new_hour_a,new_hour_b) # call the function 'create_new_time'
>>>>>>> 165d2428a3d16900d1556668ebfb30a22f086efd
			
			
			def delete_insert_time(line_list): # the function will delete the 'old' time string and insert the 'new' time with AM/PM
				del line_list[1:3] # delete form the list 'old' pickup_time and dropoff_time
			
				line_list.insert(1,new_a) #insert into the list
				line_list.insert(2,new_b) #insert into the list
				return line_list
			
			line_list=delete_insert_time(line_list) # call the function
			new_str=','.join(line_list)
			#print(new_str,end='')
			
			new_file.write(new_str) #write new string to a file
<<<<<<< HEAD

# with open(input_file,'rt') as file: # read the initial file
	# text=file.read()
	# print(text,end='')
	
# print()
# with open(output_file,'r') as new_file: # read the output data
	# new_text=new_file.read()
	# print(new_text,end='')
=======
			
with open(input_file,'rt') as file: # read the initial file
	text=file.read()
	print(text,end='')
	
print()
with open(output_file,'r') as new_file: # read the output data
	new_text=new_file.read()
	print(new_text,end='')
>>>>>>> 165d2428a3d16900d1556668ebfb30a22f086efd
	