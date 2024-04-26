#Importuje biblioteki programistyczne
import numpy as np 
import math 
#Ile liczb w wektorze jest ustalona
n = int(3)
#Wiersze poniżej odczytuje dane wejściowe od użytkownika za pomocą funkcji map()
list1 = list(map(int, 
	input("\nEnter 3 numbers of the first Vector separated by space : ").strip().split()))[:n]
list2 = list(map(int, 
	input("\nEnter 3 numbers of the second Vector separated by space : ").strip().split()))[:n]
#Tworzy wektory  
v = np.array([(list1)]) 
s = np.array([(list2)])
#Kalkuluje mnożenie wektorowe
r = np.cross(v, s) 
print("Cross product of these two Vectors is : ")
print(r) 