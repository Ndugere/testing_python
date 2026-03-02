def missing_number(arr: list) -> int:
    n = len(arr)
    expected_sum = (n * (n + 1)) // 2
    real_sum = sum(arr)
    return expected_sum - real_sum