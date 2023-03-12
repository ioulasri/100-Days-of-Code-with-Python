def twoSum(nums, target):
            for i in range(len(nums)):
                for j in range(i+1, len(nums)):
                    if nums[i] + nums[j] == target:
                        return [i, j]


print(twoSum(nums=[3, 5, 6, 1], target=4))

