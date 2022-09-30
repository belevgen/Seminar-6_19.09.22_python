# первоначально:
# Реализуйте алгоритм перемешивания списка
# original_list = [2, 5, 8, 9, 3, 7]
# new_list = []
# for i in range(len(original_list)):
#    new_i = random.randrange(len(original_list))
#    original_list[i], original_list[new_i] = original_list[new_i], original_list[i]
# print(original_list)
# print(new_list)

import random

original_list = [2, 5, 8, 9, 3, 7]
new_list = [random.randrange(len(original_list)) for i in range(len(original_list))]
print(original_list)
print(new_list)