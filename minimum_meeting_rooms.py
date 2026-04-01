def minimum_meeting_rooms(nums: list) -> int:
   # Input: [[0,30], [5,10], [15,20]]
   # #Output: 2
   if len(nums) <= 1:
      return 1
   nums.sort()
   count = 1
   current = nums[0]
   
      
