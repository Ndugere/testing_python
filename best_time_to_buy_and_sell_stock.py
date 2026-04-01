def best_time_to_buy_and_sell_stock(nums: list) -> int:
    #prices = [7,1,5,3,6,4]
    # #Output: 5
    # Buy on day 2 (price = 1) and sell on day 5 (price = 6)
    max_profit = 0
    left, right = 0, 1

    while right < len(nums):
        if nums[right] > nums[left]:
            profit = nums[right] - nums[left]
            max_profit = max(max_profit, profit)
        else:
            left = right
        
        right += 1
    
    return max_profit