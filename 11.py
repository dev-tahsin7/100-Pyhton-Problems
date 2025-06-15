"""
Given the names and grades for each student in a class, can you write a program to find the student(s) with the second lowest grade?
Rules:
Store the student data in a nested list.
If multiple students share the second lowest grade,
print their names in alphabetical order, each on a new line.

Example:
If the records are [['chi', 20.0], ['beta', 50.0], ['alpha', 50.0]]
The scores are [20.0, 50.0]. The second lowest score is 50.0.
The students with that score are "beta" and "alpha".

Output:
alpha
beta
"""

# Solution
my_list = []
for _ in range(int(input())):
    name = input()
    score = float(input())
    my_list.append([name, score])

number_list = [score for name, score in my_list]
unique_list = set(number_list)
new_list = sorted(list(unique_list))

second_grade = 0
if len(new_list) > 1:
    second_grade = new_list[1]
else:
    pass

result_list = []

for name, score in my_list:
    if score == second_grade:
        result_list.append(name)

result_list.sort()
for name in result_list:
    print(name)