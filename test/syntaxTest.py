print("Hello, World!")
print(2 + 3)
print(11 * 16)
print(11 ** 16)
print(30 // 11)
print(30 % 16)

message = "Hello"
message += ", World!"
print(message)

list1 = ["mes", 2, 3.14]
for e in list1:
    t = type(e)
    if isinstance(e, str):
        print('yes')
    print(t, ':', e)

print(list1)
list1.append(7)
print(list1)
list1.pop(1)
print(list1)


