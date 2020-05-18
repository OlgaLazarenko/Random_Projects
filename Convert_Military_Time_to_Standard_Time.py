'''
Project Name: Read Text File, Change Military Time to Standard Time,
			  Write to a New Text File
Date: May 07, 2020
Author: Olga Lazarenko
'''

import os
import csv



print("File exists:  " + str(os.path.exists('E://_Python_Projects/fhv_tripdata_2019-11-small_part_ONLY.csv')))
#check if the file exsists

print()
os.stat('E://_Python_Projects/fhv_tripdata_2019-11-small_part_ONLY.csv') 
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



with open('E://_Python_Projects/fhv_tripdata_2019-11-small_part_ONLY_2.csv','rt') as file:

	with open('E://_Python_Projects/fhv_tripdata_2019-11-small_part_NEW.csv','w') as new_file:
		print()
		header=file.readline()
		new_file.write(header)
		
		print('---------------------')
	#print(line,end='')
		for line in file:
			print(line)
			line_list=line.split(',')
			a=line_list[1]
			b=line_list[2]

			a_part1=a[0:(a.find(' ')+1)] # month-day-year part
			b_part1=a[0:(b.find(' ')+1)]
			
			hour_a=int(a[-5:-3])
			hour_b=int(b[-5:-3])
			
			if hour_a>12:
				new_hour_a=str(hour_a-12)+ a[-3:]+" PM"
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
				new_hour_b='12'+ b[-3:] + " AM"				
				

			new_a= a[0:(a.find(' ')+1)] + new_hour_a 

			new_b= b[0:(b.find(' ')+1)] + new_hour_b 	
			
			
			del line_list[1:3] # delete form the list
			
			line_list.insert(1,new_a) #insert into the list
			line_list.insert(2,new_b) #insert into the list
			
			
			
			new_str=','.join(line_list)
			#print(new_str,end='')
			
			new_file.write(new_str) #write new string to a file
			
with open('E://_Python_Projects/fhv_tripdata_2019-11-small_part_ONLY_2.csv','rt') as file: # read the initial file
	text=file.read()
	print(text,end='')
	
print()
with open('E://_Python_Projects/fhv_tripdata_2019-11-small_part_NEW.csv','rt') as new_file:
	new_text=new_file.read()
	print(new_text,end='')
	