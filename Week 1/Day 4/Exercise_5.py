a = 256
b = 256
print(a, b, a == b, a is b, id(a), id(b))

x = 99999
y = 99999
print(x, y, x == y, x is y, id(x), id(y))

s1 = "hello"
s2 = "hello"
print(s1, s2, s1 == s2, s1 is s2, id(s1), id(s2))

s3 = "hello world!"
s4 = "".join(["hello", " ", "world", "!"])
print(s3, s4, s3 == s4, s3 is s4, id(s3), id(s4))

list1 = [1, 2, 3]
list2 = [1, 2, 3]
print(list1, list2, list1 == list2, list1 is list2, id(list1), id(list2))
