'''The included code stub will read an integer,'n',from STDIN.
Without using any string methods, try to print the following:
Note that 123...n

Example
n = 5
Print the string 12345 '''

# Solution
n = int(input())
if 1<= n <= 150 :
    for i in range(1, n+1):
        print(i, end="")
