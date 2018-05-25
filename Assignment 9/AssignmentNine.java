/**
* Value of an Investment (convert of Assignment 3 from Python)
* 
* By: Spencer Milbrandt
* 
* This program will calculate the nominal interest using values that the user
* inputs. After the inputs are put through the nominal interest calculation 
* the user will receive an input indicating how much money will be accumulated 
* over the amount of years the user chose.
* 
* Created: 11/1/2013
* Modified: 11/1/2013
*/

import java.util.Scanner;

public class AssignmentNine
{
	public static void main(String[] args)
	{	// This Scanner statement imports the ability to to use the keyboard to enter
		// a value designated in keyboard.next as a Double or Int in this program.
		Scanner keyboard = new Scanner(System.in);
		
		// This print statement just begins the program off by adding what the program does.
		System.out.println("This program calculates the future value of a nominal investment.");
		
		// Double and Int make the variables able to become a double or int. Thus I assigned principal
		// and npr as double. I then set period and year to be an integer.
		double p, n;
		int pr, y;
		
		// This asks the user to enter the initial principal and then assigns the variable p to the 
		// system double input on the next keyboard input.
		System.out.println("\nEnter the initial principal:");
		p = keyboard.nextDouble();
		
		// This does the same as the initial principal statement except it asks the nominal interest
		// rate.
		System.out.println("\nEnter the nominal interest rate:");
		n = keyboard.nextDouble();
		
		// This asks the user the number of compounding periods per year. Stores the next int 
		// keyboard input into pr.
		System.out.println("\nEnter the number of compounding periods per year:");
		pr = keyboard.nextInt();
		
		// This asks the user the number of years. Stores the next int keyboard input into y.
		System.out.println("\nEnter the number of years:");
		y = keyboard.nextInt();
	
		// This is the loop that will be performed for the calculation of nominal interest.
		int r = y*pr;
		for (int i = 1; i <= r; i++)
				p = p * (1 + (n/pr));
		
		// This will then print out the value in y years as p.
		System.out.print("\nThe value in " + y + " years is: " + p);
		
	}
}
