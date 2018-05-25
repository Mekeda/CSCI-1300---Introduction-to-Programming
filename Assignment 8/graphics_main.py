'''
Images and Filters Program

By: Spencer Milbrandt

Created: 10/22/13
Last Modified: 10/27/13

This program imports GIF files that are in the same directory as the graphics_main.py file. From there the GIF file can 
go through filters that the user inputs. The program consists of a robust textual interface and allows the user to quit the
program at anytime as well as cancel a request if the user doesn't desire to choose the filter they selected. The user can 
also run as many images through the filter as they want. The program also has many exception cases to prevent crashes within
the program.

Uses a GIF image import.
'''
#This imports the list directory, graphics filters, and glob.
from os import listdir
from graphics_filters import *
import glob

#This will print a statement at the very beginning of the program.
print("Welcome to the GIF Image Filter Program!")

def directory_selection():
	
	# The try/except statement will catch any errors that the user inputs.
	# In this case it will return back to directory_selection() and run through
	# the definition again till the input satisfies the requirements.
	
	try:
		files = listdir(".")
		
		# This is the choice selection for the file the user wants to use in the 
		# filter. It then stores that file selection in choice_1 and runs it 
		# through the file list to obtain the file desired and assigning it to
		# selection_file using the glob import.
	
		nums = 1
	
		print("\nList of GIF files in Directory:")
		files = glob.glob("*.gif")
		for f in files:
			print(nums, f)
			nums = nums + 1 
		print(nums, "Quit")	
					
		choice_1 = int(input("\nEnter selection:\n"))
		if (choice_1 != nums):
			selection_file = files[choice_1-1]
		elif(choice_1 == nums):
			selection_file = ""
		return selection_file
	
	
	except:
		print("Invalid File Selection! - Please enter a valid selection!")
		while ( choice_1 >= nums):
			return directory_selection()

def filter_selection():
		
	# This is the filter selection UI. It will store the input that the user
	# chooses into choice_2. Which then is used for the main() definition.
	
	print("\nWhat filter would you like to choose?")
	print("1 Grayscale Filter")
	print("2 Black and White Filter")
	print("3 Red Tones Filter")
	print("4 Green Tones Filter")
	print("5 Blue Tones Filter")
	print("6 Posterize Filter")
	print("7 Inverted Filter")
	print("8 White and Black Filter")
	print("9 Hot Pink Awesomeness Filter")
	print("10 CU Pride Filter")
	print("11 Quit")
	choice_2 = input("\nEnter Selection:\n")
	
	return choice_2

def main():
	
	# This is the main function where the selection_file will be called to
	# the graphics_filters.py In order to keep the programming running
	# I had to use a while statement which will continue with the program
	# until the selection_file == "Quit".
	
	selection_file = True
	while (selection_file != ""):
		selection_file = directory_selection()
		if (selection_file == ""):
			pass
		else:
			while(selection_file != "Quit"):
				
			# This is the definition that takes the user's input for filter selection
			# and file selection. These are then called to the filters in 
			# graphics_filters.py and executed there.
	
				choice = filter_selection()
	
				if (choice == '1'):
					display_grayscale(selection_file)
			
				elif(choice == '2'):
					black_and_white(selection_file)
	
				elif(choice == '3'):
					red_tones(selection_file)
	
				elif(choice == '4'):
					green_tones(selection_file)
	
				elif(choice == '5'):
					blue_tones(selection_file)
	
				elif(choice == '6'):
					posterize(selection_file)
	
				elif(choice == '7'):
					inverted(selection_file)
		
				elif(choice == '8'):
					white_and_black(selection_file)
		
				elif(choice == '9'):
					hot_pink_awesomeness(selection_file)
	
				elif(choice == '10'):
					cu_pride(selection_file)
		
				elif(choice == '11'):
					selection_file = "Quit"
				
			print("\nWould you like to filter another image?")
				
if __name__ == '__main__':
	main()

	
	





