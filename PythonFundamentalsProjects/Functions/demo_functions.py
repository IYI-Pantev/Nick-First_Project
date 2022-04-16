# def custom_split(text, sep):
#     result = text.split(sep)
#     return result
#
# print(custom_split("Hello;there", ";"))

# def multiply_self(number):
#     result = number*number
#     return result
#
# print(multiply_self(7)) # 50 % създаваме функция с параметри, 50% да я извикаме

# def heading():
#     print("FreeMindHub")
# def bottom_heading():
#     print("Contacts: ...")
#
# def web_site(): # може да извикваме функции от главна функция !!!
#     heading()
#     bottom_heading()
#
# web_site()

# def person(first_name, last_name = "unknown"):
#     return first_name, last_name
#
# print(person("Nick")) # във функцията се подават
# # или параметри или аргументи по подразбиране
from turtle import width


# def area(width, height):
#     return width*height
# print(area(height = 2, width = 1)) # ключови аргументи

# data = input().split()
#
# numbers = [int(el) for el in data]  #прави същото като долното
#
# # for el in data:
# #     numbers.append(int(el))
# print(data)
# print(numbers)

# a = [1, 2 ,3]
# b = a.copy() #така ако променим едното не се променя и другото
# #защото листовете са референтни тип данни
# #това прави ново място в паметта със същите данни
# #по дифолт иначе проенливите ще сочат към едно място на памет

# a = [1, 2, 3]
# b = [num for num in a]
# a.append(100)
# print(id(a))
# print(id(b))

# data = [-5, 3, 2, 0, -1, 4]
# converted = [x**2 for x in data if x > 0]
# print(converted)

data = [-5, 3, 2, 0, -1, 4]
num = data.pop()
print(num)
print(data)