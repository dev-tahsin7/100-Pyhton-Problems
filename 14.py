"""
From the numbers 30, 53, 29, 32, 15, 9, 22, 47, 49, 13, 40, 33,
a total of 6 pairs were formed by taking two numbers.
The sum of the member numbers of each of these pairs is equal.
If pairs are formed this way, what number was in the same pair with 22?
"""

list_of_num = [30, 53, 29, 32, 15, 9, 22, 47, 49, 13, 40, 33]

sum_of_list = sum(list_of_num)

paris = sum_of_list / 6

pairs_with_22 = paris - 22

print(f"Paris of 22 is : {int(pairs_with_22)}")


# print(sum_of_list)
# print(paris)



