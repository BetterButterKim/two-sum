from typing import List

def twoSum(nums, target):
    first_index = 0
    second_index = 0
    new_List = []
    
    for index1 in range(0, len(nums)-1):
        first_index = index1
        for index2 in range(index1 + 1,len(nums)):
            second_index = index2
            if nums[first_index] + nums[second_index] == target:
                new_List = [first_index, second_index]
                print("Output:",new_List)          
    return new_List


List1 = [2, 7, 11, 15]
target1 = 26
twoSum(List1, target1)