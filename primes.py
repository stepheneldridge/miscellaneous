m = 10 ** 7
nums = {i for i in range(3, m, 2)}
for i in range(3, m, 2):
    if i not in nums:
        continue
    nums -= set(range(2 * i, m, i))
nums.add(2)
print(len(nums))