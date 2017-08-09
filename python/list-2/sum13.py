''' Return the sum of the numbers in the array, returning 0 for an empty array. Except the number 13 is very unlucky, so it does not count and numbers that come immediately after a 13 also do not count. '''

# sum13([1, 2, 2, 1]) → 6
# sum13([1, 1]) → 2
# sum13([1, 2, 2, 1, 13]) → 6

def sum13(nums):
  if len(nums) == 0:
    return 0
    
  for i in range(len(nums) - 1):
    if nums[i] == 13:
      nums[i] = 0
      nums[i+1] = 0
      
  if nums[-1] == 13:
    nums[-1] = 0
    
  return sum(nums)
