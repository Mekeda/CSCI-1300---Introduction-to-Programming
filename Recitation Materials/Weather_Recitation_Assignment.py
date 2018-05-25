"""
This is a program to determine multiple values using the BoulderWeatherData.csv file 
as an input file.

1) Determine the highest daily rainfall for all the data.
2) Determine the average yearly, monthly, and daily rainfall.

By: Spencer Milbrandt

10/3/2013
"""
#This will read the data on specified file.	
infile = open("BoulderWeatherData.csv", "r")

#This is the process of compiling and stating what the highest daily rainfall for all the data.
rainFile = []
weatherFile = []

for line in infile:
	weatherFile.append(line.split(","))

for i in weatherFile:
	rainFile.append(i[4])
	

	
	

