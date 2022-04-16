
# words = [[1, 2, 3], "Hello", "how", "why"]
# print(words[0][1])
# list_function = list() # по-добре да използваме []
# print(list_function)

# some_text = "a b c d"
# result = some_text.split() # в скобите може да укажем по какво точно да разделя
# print(result)

# some_text = ["Hello", "World", ".!."]
# result = '<->'.join(some_text) # в спейса указваме как да се долепят
# print(result)


# result = list(range(1, 6))
# print(result)
# for i in range(1, 6):
#     print(i, end=" ")

# nums = [1, 2, 3, 3]
# print(nums.count(3)) # брои колко пъти се повтаря елемент (method)

# word = 'Hello'
# word_as_list = list(word)
# print(word_as_list) # превръщане на текст в лист
#
# num = 156
# num_as_string = str(num)
# print(list(num_as_string)) # превръщане на числа в лист
# list

# nums = [1, 3, 4, 5, 6, 12, 33, 44, 34, 666]
# print(nums[-1]) # може да достъпваме индексите отзад напред
# print(len(nums))

# some_list = ["Sasha", "Alex", "Athene"]
# print(some_list.count("Alex"))

# nums = [20, 5, 30]
# for index in range(len(nums)):
#     nums[index] = 1
#
# print(nums)


# nums = [20, 5, 30]
# print(*nums) # * пред масива го unpack !

# data = [1, 12.5, False, "Hello", 2]
# list_only_integers = []
#
# for el in data:
#     if isinstance(el, int) and not isinstance(el, bool):
#         list_only_integers.append(el)
#
# print(list_only_integers)

# word = "Hello"
# word_list = list(word)
#
# for el in word_list:
#      print(ord(el))

# n = int(input())
# list_names = []
# for num in range(n):
#     names = input()
#     list_names.append(names)
#
# print(list_names)

# nums = [1, 2, 3]
# nums.pop()
# print(nums) # маха последното, ако не е указано
# # pop работи с индекси не с елементите в списъка!!!

# my_list = ["dog", "cat", "fish"]
# while len(my_list) > 0:
#     print(my_list[0], end=" ")
#     my_list.pop(0) # друг вариант е del my_list[0] -> пак трие

# my_list = ["dog", "cat", "fish"]
# while len(my_list) > 0:
#     print(my_list.pop(0), end=" ")

# nums = [1, 2, 3]
# nums.reverse() # обръща листа
# for el in nums:
#     print(el)

# numbers = [1, 2, 3, 3, 3]
# numbers.remove(3)
# print(numbers)