"""
Add your required comments up here. You can get them
from the assignment 2 file if you would like.
"""
# futval.py
#	 A program to compute the value of an investment
#	 carried 10 years into the future

def main():
	# Step 1: it isn't always a 10 year investment now, change this so it makes sense
	print("This program calculates the future value of a nominal investment.")


	principal = eval(input("Enter the initial principal: "))
	
	# Step 2: there isn't an annual interest rate now, so change this 
	#	variable name and input string prompt to something more appropriate.
	npr = eval(input("Enter the nominal interest rate: "))

	# Step 3: add a statement below to get the number of compound periods
	period = eval(input("Enter the number of compounding periods per year: "))
	
	# Step 4: add a statement below to get the number of years for the investment
	year = eval(input("Enter the number of years: "))
	
	# Step 5: the for-loop is no longer always going to execute 10 times
	#  You need to change the expression inside range to make the
	#  loop iterate the correct number of times	 range(<expr>).
	# Hint: You will use two variables entered by the user to do this.
	for i in range(year*period):
		# Step 6: The principal calculation needs to be updated to use the
		#	nominal interest rate instead of annual percentage rate
		principal = principal * (1 + (npr/period))

	# Step 6: Change this print statement so that it displays the
	#	number of years the user enters
	print("The value in", year,"years is:", principal)

main()
