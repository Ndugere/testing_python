def move_zeros_to_the_left(nums: list) -> list:
    #[0,1,2,0,0]
    index_pos = 0
    for num in nums:
        if num != 0:
            nums[index_pos] = num
            index_pos += 1
    for i in range(index_pos, len(nums)):
        nums[i] =0
    
    return nums