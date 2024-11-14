names = ["z", "v", "o"]
ages = (16, 25, 41)

def checker(user):
    name, age = user
    return age > 21

users = list(zip(names, ages))
sigma = list(filter(checker, users))
print(sigma)