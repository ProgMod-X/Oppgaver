nums = []
nums.append(float(input("Num 1: ")))
nums.append(float(input("Num 2: ")))

def minst(nums):
    nums.sort()
    return nums[0]

def stoerst(nums):
    nums.sort()
    return nums[1]

print(f"{minst(nums)} er minst")
print(f"{stoerst(nums)} er størst")