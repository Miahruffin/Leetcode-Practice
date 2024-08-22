
def twoSum(self, nums: List[int], target: int) -> List[int]:
    prevMap = {} # val : index, Hash Map
        
        # Iterates through array taking the difference and subtracting it and search if the difference is within the has map already.
        
    for i, n in enumerate(nums): 
        diff = target - n
        if diff in prevMap:
            return[prevMap[diff], i]
        prevMap[n] = i