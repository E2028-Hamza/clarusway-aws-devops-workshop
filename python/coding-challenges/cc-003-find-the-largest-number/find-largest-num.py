nums = input("Give me 5 different integer with space: ")

nums = nums.split(" ")

maxnum = 0

for i in range(len(nums)):
    if maxnum >= int(nums[i]):
        maxnum = maxnum
    else :
        maxnum = int(nums[i])

print(maxnum)