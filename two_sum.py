def solution(nums, target):

    num_index_dict = {}

    for i, num in enumerate(nums):
        the_other_number = target - num
        if the_other_number in num_index_dict:
            return [num_index_dict[the_other_number], i]
        num_index_dict[num] = i

    return False