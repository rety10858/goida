name = "Sergeev Elisey"
name2 = "_".join(name)
print(name2)
name3 = name2.upper()
name4 = name2.lower()
a =  [ord(symbol) for symbol in name3]
b =  [ord(symbol) for symbol in name4]
print(a)
print(b)
print('min:', min(a))

print('max:', max(a))

print('min:', min(b))

print('max:', max(b))