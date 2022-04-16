from unittest import result

tail = input()
body = input()
head = input()

result = [head, body, tail]
print(result)

result[0], result[2] = result[2], result[0] # размяна
print(result)
