print("Integer are immutable and numbers can't be change we can change only the pointers")
num1 = 11
num2 = num1

print(num1)
print(num2)
print(id(num1))
print(id(num2))

num2 = 22

print(num1)
print(num2)
print(id(num1))
print(id(num2))

print("------------Dictonary------------")

print("Dictonay are mutable")

dict1 = {'Value': 11}
dict2=dict1
print(dict1)
print(dict2)
print(id(dict1))
print(id(dict2))

dict2['Value'] = 22
print(dict1)
print(dict2)
print(id(dict1))
print(id(dict2))