class Solution:
    #Sid
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictionary = {}
        for  index, element in enumerate(nums):
            bal = target - element 
            if bal in dictionary:
                return [dictionary[bal], index]
            dictionary[element] = index
