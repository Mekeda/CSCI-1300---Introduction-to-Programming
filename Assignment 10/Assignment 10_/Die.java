/**
 * This class establishes the instance variables of myDieValue and myDieSides to 
 * create a program that will randomly roll a die with x amount of sides and print
 * out the value of that die.
 * 
 * @Spencer Milbrandt 
 * @V 1.0 
 * Last Modified 11/21/2013 
 */

import java.util.Random;

public class Die
{
    // instance variables 
    private int myDieValue;
    private int myDieSides;
    private Random myRandom;
    
    // Dice Class Constructors
   
    public Die()
    {
        // Initializes instance variables to default values.
        
       this.myDieSides = 4;
       this.myRandom = new Random();
       this.myDieValue = 1;
    }
    
    public Die(int numSides)
    {
        // Initialize value and random as above
        // using setDieValue to set the number of sides.
        
        this.myRandom = new Random();
        setDieSides(numSides);
        this.myDieValue = 1;
        
    }
    
    // Getter Methods.
    
    public int getDieSides()
    {
		return myDieSides;
    }
    
    
    public int getDieValue()
    {
        return myDieValue;
    }
    
    // Setter Method.
    
    /*
     * Remember, a die cannot have fewer than 4 sides
     *   or more than 100.
     */
    private void setDieSides(int newNumSides)
    {
        // A user of the Die class cannot call this method directly
        // it is a helper function for the Die.
        // This takes the input from TestDieClass for newNumSides
    
        if ((newNumSides > 3) && (newNumSides < 101))
			{
			myDieSides = newNumSides;
			}
		else
			{
			System.out.println("\nIncorrect Die Side value. Setting Die Side to default value.");
			myDieSides = 6;
			}
        
    }
    
    public void rollDie()
    {
		this.myDieValue = myRandom.nextInt(myDieSides) + 1;
    }
    
    // Print Die Method.
    // This will print the die value and 
    // will print an error message if it is for some
    // reason invalid which the code would need to change
    // in order for that to happen.
    
    public void printDie(int dieNum)
    {
		
        /*
         * if dieNum is <= 0 the output does not need to list which die 
         *    is being printed
         *    e.g. "Die Value: 5"
         * else, the output should indicate which die is being displayed,
         *    which is indicated by the value of dieNum
         *    e.g. "Die 2 Value: 5" is displayed when dieNum is 2
         */
         
        if (dieNum <= 0)
			System.out.println("\nDie Value: " + myDieValue);
		else if (dieNum > 0)
			System.out.println("\nDie " + dieNum + " Value: " + myDieValue);
		else
			System.out.println("Sorry. Couldn't evaluate the input for the Die Number.");
    }
}
