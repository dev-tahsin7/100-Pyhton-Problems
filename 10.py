#3D Coordinates Exclusion
'''
You are given four integers x, y, z, and n representing the dimensions of a 3D cuboid and a condition number.
You need to generate a list of all possible coordinates [i, j, k] such that:
    0 ≤ i ≤ x
    0 ≤ j ≤ y
    0 ≤ k ≤ z

Your task is to print the list of coordinates excluding any list where the sum i + j + k == n.
📌 You must use list comprehension to solve this problem.

>> Sample Input:
1
1
2
3

>> Sample Output:
[[0, 0, 0], [0, 0, 1], [0, 0, 2], [0, 1, 0], [0, 1, 1],[1, 0, 0], [1, 0, 1], [1, 1, 0], [1, 1, 2]]
'''

# Solution- 1 : using lamda function
x = int(input())
y = int(input())
z = int(input())
n = int(input())

my_list = [[i, j, k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i + j + k != n]
print(my_list)

# Solution -2
my_list1 = []
for i in range(x+1):
    for j in range(y+1):
        for k in range(z+1):
            if i + j + k != n:
                my_list1.append([i,j,k])

print(my_list1)