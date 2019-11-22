#Write a program to identify duplicate values from list

arr = [1, 5, 8, 5, 7, 6, 3]
def find_duplicate(nums):
    dublicates = []
    nums.sort()
    for i in range(len(nums)-1):
       if nums[i] == nums[i+1]:
          dublicates.append(nums[i])
    return dublicates         



print(find_duplicate(arr))    