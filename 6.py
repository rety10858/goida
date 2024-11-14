def goida(a):
    return(a%3 == 0)

nums = [24, 65, 23, -32, 75]
result = list(map(goida, nums))
print(result)

def zov(a, b):
    return a*b

nums = [1, 2, 3, 4]
nums1 = [2, 3, 4, 5]

nums2 = list(map(zov, nums, nums1))

print(nums2)