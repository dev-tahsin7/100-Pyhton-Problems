"""
Problem: List Commands

You are given an empty list, arr = [].

Your task is to read a number n (the total number of commands),
and then read n lines of commands. Each command will be one of the following:

✅ List of Valid Commands:
    insert i e – Insert integer e at position i
    print – Print the list
    remove e – Delete the first occurrence of integer e
    append e – Insert integer e at the end of the list
    sort – Sort the list in ascending order
    pop – Remove the last element from the list
    reverse – Reverse the list

🔄 Input Format:
    The first line contains an integer n, the number of commands.
    The next n lines each contain a command from the list above.

📤 Output Format:
    For every print command, print the list on a new line.

✅ Constraints:
    The elements added to the list will be integers.
    All commands are guaranteed to be valid and in the correct format.

🧪 Sample Input:
12
insert 0 5
insert 1 10
insert 0 6
print
remove 6
append 9
append 1
sort
print
pop
reverse
print

📤 Sample Output:
[6, 5, 10]
[1, 5, 9, 10]
[9, 5, 1]
"""
arr = []
N = int(input())

for _ in range(N):
    command = input().split()
    action = command[0]

    if action == "insert":
        i = int(command[1])
        e = int(command[2])
        arr.insert(i,e)

    elif action == "print":
        print(arr)

    elif action == "remove":
        e = int(command[1])
        arr.remove(e)

    elif action == "append":
        e = int(command[1])
        arr.append(e)

    elif action == "sort":
        arr.sort()

    elif action == "pop":
        arr.pop()

    elif action == "reverse":
        arr.reverse()