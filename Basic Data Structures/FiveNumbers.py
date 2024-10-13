print("Enter 5 Numbers!")
nums = [ ]
i = 0
y = 0
sum = 0
for i in range(5):
    nums.append(input("Enter Number: "))
    print(nums)
for y in range(5):
    sum += int(nums[y])
print(sum)