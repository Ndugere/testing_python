def move_zeros(nums: list)-> list:
    #Input:  nums = [0,1,0,3,12]
    #Output: [1,3,12,0,0]

    left_pointer, right_pointer = 0, 1
    while right_pointer < len(nums):
        if nums[left_pointer] == 0:
            while right_pointer< len(nums) -1 and nums[right_pointer]==0:
                right_pointer += 1
            nums[left_pointer] = nums[right_pointer]
            nums[right_pointer] = 0
        left_pointer+=1
        right_pointer+=1
    return nums
print(move_zeros(nums = [ 1, 0, 0, 0, 1]))