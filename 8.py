"""
You are given the marks of multiple students stored in a dictionary format.
Each student has 3 test scores. Your task is to:
1. Identify the student with the highest average score.
2. Print their name and the average score, formatted to 2 decimal places.
"""

# Solution
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    acess = student_marks[query_name]
    avarg = sum(acess) / len(acess)
    print(format(avarg, ".2f"))