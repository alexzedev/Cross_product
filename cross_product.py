#Importing libraries
import numpy as np 
import math 
#Number of numbers in vector
n = int(3)
# Lines below reads inputs from user using map() function
list1 = list(map(int, 
	input("\nEnter 3 numbers of the first Vector separated by space : ").strip().split()))[:n]
list2 = list(map(int, 
	input("\nEnter 3 numbers of the second Vector separated by space : ").strip().split()))[:n]
#Creates vectors  
v = np.array([(list1)]) 
s = np.array([(list2)])
#Calculate cross product
r = np.cross(v, s) 
print("Cross product of these two Vectors is : ")
print(r) 