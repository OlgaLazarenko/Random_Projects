"""
 Date: Apr 17, 2020
 Author: Olga Lazarenko
 Project Name: Random String Lists
 Description: two lists with randomly selected string values will be created, 
				the user can select the size of the lists and the size of the strings,
				the list with distinct shared strings will be created,
				all lists can be presented in columns and the user can choose the number of columns.
				The function create_random_string_lists is used to generate the random lists of strings.
				The following fuctnions are used:
					-create_random_str_lists
					-shared_values_list
					-create_columns
								
"""

import random # import python module random
import string # import python module string 

print()
#the input from the user 
L1=int(input("Enter the lenght of the first list here: "))
if type(L1) != "int":
	print("wrong input")
L2=int(input("Enter the lenght of the second list here: "))
str_len=int(input("Enter the lenght of the string here: "))
col=int(input("Enter the number of columns here: "))
print()
print()
#check of if the input is a number




def create_random_string_list(L1,L2,str_len): # the inner/nested function to create ransom sting lists
	list1=[] # create a first list
	for l in range(L1):
		word=''.join(
				random.choice(string.ascii_lowercase)
				for n in range(str_len)
				) # join the random letters into a string of required length 
		list1.append(word) # populate the list

	list2=[] # create a second list
	for m in range(L2):
		word=''.join(
				random.choice(string.ascii_lowercase)
				for n in range(str_len)
				)
		list2.append(word)
	
	return list1,list2; # list1 and list2 are retured from the function
		
list1, list2 = create_random_string_list(L1,L2,str_len) 
print()
print("List1: "+str(len(list1))+ " values")
print(list1)
print()
print("List2: "+str(len(list2)) + " values")
print(list2)
	

def shared_values_list(list1,list2): # create the inner/nested function to obtain a list with distinct shared values 
	list3=[] # the list contains the shared values from the list1 and list2, there is a possibility that some values are not distinct

	for a in list1:
		for b in list2:
			if a==b:
				list3.append(a)
	
	list4=[] #leave onty the distinct shared values

	for i in list3:
		n=list3.count(i)
		if n==1:
			list4.append(i)
		else:
			m=list4.count(i)
			if m==0:
				list4.append(i)
		
	return list4
list4=shared_values_list(list1,list2)	
	
print()
print('---------------------------------')
print("The list with shared values contains  "+str(len(list4))+ " values")
print(list4)
print()	
	

def create_columns(list,col): # create a nested function to display the lists in columns
	n=0
	for i in list:
		n+=1
		if n !=col:
			print(i, end=" ")
		else:
			print(i)
			n=0
	return list
		
print()
print("List1 with "+str(len(list1))+" values")
list=create_columns(list1,col)
	
print()
print("List2 with "+str(len(list2))+" values")
list=create_columns(list2,col)
	
print()
print("List with the shared valules: " + str(len(list4))+ " values")
list=create_columns(list4,col)
	
print()
print("-----------------------")

#the end of the program
