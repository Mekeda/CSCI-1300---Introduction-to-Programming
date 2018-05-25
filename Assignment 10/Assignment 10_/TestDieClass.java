/**
 * This program helps test the Die.java file. The die will be 
 * ran through 25 times to get a decent amount of tests.
 * 
 * @Spencer Milbrandt
 * @V 1.0 
 * Last Modified on 11/21/2013
 */
import java.util.Scanner;

public class TestDieClass
{
	
    public static void main(String [] args)
    {
		
		Scanner keyboard = new Scanner(System.in);
		
		// This for loop will repeat the default test 6 times
		// and will print out the die on 6 separate lines.
		
		System.out.println("Testing the default sided die.");
		for (int i = 1; i <= 6; i++)
			{
			Die die1 = new Die();
			die1.rollDie();
			die1.printDie(i);
			}
		
		// This for loop will repeat 5 times with a classic 20 sided die from DND.
		// It will print out random rolls of within 20 on separate lines.
		
		System.out.println("\nThis die will test if it were the classic 20 die from DnD! ");
		for (int i = 7; i <= 11; i++)
			{
			Die die2 = new Die(20);
			die2.rollDie();
			die2.printDie(i);
			}
		
		// This for loop will repeat 3 times with a negative input for die sides.
		// Because of this it will set the sides to the default value of 6 within 
		// Die.java and print out the numbers like in the first example.
		
		System.out.println("\nThis roll is to test when the die sides are negative.");
		for (int i = 14; i <= 16; i++)
			{
			Die die3 = new Die(-1);
			die3.rollDie();
			die3.printDie(i);
			}
		
		// This for loop repeats 4 times to test when a number is greater than 100. 
		// This will set the number of sides to the default value of 6 from the Die.java
		// file. It will then act like the 3rd example here within the TestDieClass.java file.
			
		System.out.println("\nThis roll is to test when the die sides are greater than 100.");
		for (int i = 17; i <= 20; i++)
			{
			Die die4 = new Die(102);
			die4.rollDie();
			die4.printDie(i);
			}
		
		// This for loop will print 5 times and ask the user for an input for the 
		// number of sides on the die they want. This will then run through the Die()
		// class in the Die.java file and print out the value on 5 separate lines. If the 
		// input of the user is less than 4 or greater than 100 it will be set to the default
		// value once again of 6.
			
		System.out.println("\nNow it's your turn to choose the die number!");
		for (int i = 21; i <= 25; i++)
			{
			System.out.println("\nPlease choose a number between 4 and 100!");
			int sides = keyboard.nextInt();
			Die die5 = new Die(sides);
			die5.rollDie();
			die5.printDie(i);
			}
         
    }
}
