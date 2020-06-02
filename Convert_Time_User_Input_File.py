

'''
Project Name: Read Text File, Change Military Time to Standard Time,
			  Write to a New Text File
Date: May 07, 2020
author: Olga Lazarenko
Description: the program will read csv file and convet the columns with dates expressed in military time to standard time:
			 the hours will be converted to standard time, PM/aM will be added
			 
Data Source: https://data.cityofnewyork.us/Transportation/2019-High-Volume-FHV-Trip-Records/4p5c-cbgn/data
			a sample of data was used to check if the code performes properly
'''

import os
import csv
print()
print("the data file is: NYC_TripData_2019_11_Sample")
print()
data_file=input("Enter the data file name here: ")
print()
print("the output file name: NYC_TripData_User_Output.csv")
data_output=input("Enter the data file for the output: ")
data_file_dir= 'E://_Python_Projects/GitHub_Random_Projects/Data_Files/'
data_file_path=data_file_dir+data_file+'.csv'
print(data_file_path)
print()
print("File exists:  " + str(os.path.exists(data_file_path))) #check if the file exsists

print()
os.stat(data_file_path)  # if the file doesn't exists, show the problem 
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
print()

with open(data_file_path,'rt') as file:

	with open(data_file_dir+data_output,'w') as new_file:
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
			
			new_a,new_b = create_new_time(new_hour_a,new_hour_b) # call the funtion 'create_new_time'
			
			
			def delete_insert_time(line_list): # the function will delete the 'old' time string and insert the 'new' time with AM/PM
				del line_list[1:3] # delete form the list 'old' pickup_time and dropoff_time
			
				line_list.insert(1,new_a) #insert into the list
				line_list.insert(2,new_b) #insert into the list
				return line_list
			
			line_list=delete_insert_time(line_list) # call the function
			new_str=','.join(line_list)
			#print(new_str,end='')
			
			new_file.write(new_str) #write new string to a file
			
with open(data_file_path,'rt') as file: # read the initial file
	text=file.read()
	print(text,end='')
	
print()
with open(data_file_dir+data_output,'r')as new_file: # read the output data
	new_text=new_file.read()
	print(new_text,end='')
	