nums = [19,22,48,15,65]

minimum = nums[0]

for num in nums:
    if num < minimum:
        minimum = num
print("minimum num is: ",minimum)