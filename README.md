The Function:

The function of this is a binary calculator.
A binary calculator is a type of calculator which takes two sets of binary string, and allows you to add, subract, multiply, them together.
The calculator also checks for errors and impossible math problems to avoid issues using it.

How it works:

In the programming the first step it does is checking if any of the inputs contain any numbers besides 0's and 1's, if it does, it flaggs it as an error.
The next step it does is checking that the inputs are the valid length for binary, 8 characters long.
After those are confirmed, it takes the first input and converts it into its decimal value.
Then, it takes the second input and converts that into its decimal value.
After those are converted, it checks the type of operator being used, and using it, it determines if the decimal values of both inputs should be added, subtracted, multiplied, or divided.
If the operator is division, it does an extra check to make sure that the second input is not 0, to prevent the calculator from dividing by 0.
After that it takes the sum and checks if it is over 255 or under 0.
If the sum is larger than 255 or under 0, it detects it and flags it as a stack overflow.
Finally, the calculator goes through the sum and converts it back from decimal to its binary value, leaving you with the answer.