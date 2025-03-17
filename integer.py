def is_palindrome(x: int) -> bool:
    return str(x) == str(x)[::-1]

# Test cases
print(is_palindrome(121))   # Output: True
print(is_palindrome(-121))  # Output: False
print(is_palindrome(10))    # Output: False



def two_sum(nums: list[int], target: int) -> list[int]:
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []

print(two_sum([2,7,11,15], 9))   # Output: [0,1]
print(two_sum([3,2,4], 6))       # Output: [1,2]
print(two_sum([3,3], 6))         # Output: [0,1]

