names = ["z", "o", "v", "goida"]
ages = [1, 2 ,3 ,4]
sigma = [True, False, True, True]

users = list(zip(names,ages,sigma))
print(users)

print("user age:", dict(zip(names, ages)))