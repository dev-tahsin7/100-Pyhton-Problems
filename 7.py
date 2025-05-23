"""Question: Find the Runner-Up Score

Given the participants score-sheet for your University Sports Day,
you are required to find the runner-up score. You are given nn scores.
Store them in a list and find the score of the runner-up.

Input Format:
    The first line contains n.
    The second line contains an array A[] of n integers, each separated by a space.

Constraints
    2≤n≤10
    −100≤A[i]≤100

Output Format:
Print the runner-up score.
"""

# Solution
if __name__ == '__main__':
    n = int(input())

    if 2 <= n <= 10:
        arr = map(int, input().split())

        # List to set to remove duplicate value
        x = list(set(arr))
        # sort for high to low
        x.sort(reverse=True)

        # X[1] is the 2nd value
        print(x[1])