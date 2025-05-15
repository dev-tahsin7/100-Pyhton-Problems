"""
Simple Summation
Problem Statement:
Write a program that calculates and prints the sum of two numbers entered by the user.
Input:
The input consists of two integers.
Output:
Output a single line containing the sum of two integers.
Constraints:
    -2 31 ≤ |S| ≤ 231 - 1

Example:
Enter two numbers
Input:
5 2
Output:
7
"""

# Solution:
numbers_str = input()
numbers_list = numbers_str.split()

if len(numbers_list) == 2:
        x = int(numbers_list[0])
        y = int(numbers_list[1])
        sum_result = x + y
        print(sum_result)
else:
    pass