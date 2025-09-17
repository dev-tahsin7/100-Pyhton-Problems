"""Write a Python program that generates the following sequence of numbers.
The solution must be completed within a pre-defined code structure.

Sequence:
1
22
333
4444
55555

Code Structure:
Complete the single print statement

Constraints:
    Your solution must be a single line of code.
    Use only arithmetic operations.
    Do not use any string-related operations.
"""

for i in range(1,6):
    print(i * (10**i -1) // 9)

"""
Breakdown of the formula: 
The most important part of the code is the mathematical formula: (10**i - 1) // 9. 
This expression generates a number consisting of i number of ones.

Let's look at how this works for a few values of i:

    When i = 2: (10**2 - 1) // 9 simplifies to (100 - 1) // 9, which is 99 // 9 = 11.

    When i = 3: (10**3 - 1) // 9 simplifies to (1000 - 1) // 9, which is 999 // 9 = 111.

    When i = 5: (10**5 - 1) // 9 simplifies to (100000 - 1) // 9, which is 99999 // 9 = 11111.
    
    >> The final step is to multiply this number by i itself: i * (10**i - 1) // 9.

    When i = 2, the expression becomes 2 * 11 = 22.

    When i = 3, the expression becomes 3 * 111 = 333.

    When i = 4, the expression becomes 4 * 1111 = 4444.

The print() statement then displays this final result to the console for each iteration of the loop. 
This method is a great example of how mathematical patterns can be used to solve programming problems without relying on strings.



"""