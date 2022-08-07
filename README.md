# Real-Estate-Analyzer

Lists and Real Estate Analyzer

The owner of BDJ Real Estate of Springfield has hired you to design a sales analyzer program for real estate sales.  You can enter the property sales by entering a valid sales dollar amount repeatedly until the user says No to more input.  You don’t know up front of how many entries you will have so a List must be used. 

Once the data entry is complete you write code to find out the different analytics for the sales: Min, Max, Average, Median, Total and Commission. 

1. Code a function Code a function called getFloatInput that receives a string as a parameter to be used as the prompt input text and it returns a float. You will be calling this function for each value to be inputted and assign the function’s return value and assign to each of the listed variables. For example: 
 fSalesPrice = getFloatInput(“Enter property sales value:”)
Perform data validation within the function on the inputted value using Python error handling which can be found in Blackboard.  Use Python’s loops to accomplish the sub-tasks below:
If the contents are not numeric issue a message and prompt them again until the user enters a valid number for each of the input variables.  
Make sure the inputted value are non-zero and positive values or issue an error message and ask for input again.  
Return a valid non-zero float.

2. Code a function called getMedian that receives a list and returns a float that does the following (you must write your own code you can NOT use the median function in the Python statistics module):
If the number of entries in the list is odd, divide the count by 2 and use that entry as the median
If the number of entries in the list is even divide the count by 2.  Take that that entry and the entry before it and average the two elements and use that as the median. 
Return the calculated median value.

3. Code a main function that includes these requirements:
Use a list to store all the user inputted sales values.
Code a loop that repeats until the user enters a N to exit the loop:
Each time through the loop call the getFloatInput function to prompt the user for the sales price.  
Each value returned from the function getFloatInput must be added to the list
Prompt the user with “Enter another value Y or N”.   If the user enters a Y or y repeat the user input loop. If the user enters a N or n exit the loop.  If any other value is entered keep asking until a Y, y, N or n is entered.
Sort the list from smallest value to largest.
Refer to the sample output below to help you code and visualize the required output and make sure it matches the screen shot below before submitting your code.
Output each entry in the sorted list to the screen that is formatted as currency with 2 decimal positions
Determine the Minimum value and output formatted as currency with 2 decimal positions to the screen.
Determine the Maximum value and output formatted as currency with 2 decimal positions to the screen.
Determine the Total value and output formatted as currency with 2 decimal positions to the screen.
Calculate the Average and output currency with 2 decimal positions to the screen.
Determine the Median by calling the getMedian function you coded in Step 2 by passing list of values that was populated in the loop.  Receive the Median value returned from the getMedian function and output formatted value as currency with 2 decimal positions. 
Determine the Commission by multiplying the Total of the calculation by .03 and output the formatted value as currency with 2 decimal positions.

4.Make sure to include comments in your code.

