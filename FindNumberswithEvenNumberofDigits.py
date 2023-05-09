# Given an array nums of integers, return how many of them contain an even number of digits.

# Example 1:

# Input: nums = [12,345,2,6,7896]
# Output: 2
# Explanation: 
# 12 contains 2 digits (even number of digits). 
# 345 contains 3 digits (odd number of digits). 
# 2 contains 1 digit (odd number of digits). 
# 6 contains 1 digit (odd number of digits). 
# 7896 contains 4 digits (even number of digits). 
# Therefore only 12 and 7896 contain an even number of digits.
# Example 2:

# Input: nums = [555,901,482,1771]
# Output: 1 
# Explanation: 
# Only 1771 contains an even number of digits.
 
# Constraints:

# 1 <= nums.length <= 500
# 1 <= nums[i] <= 10^5

"""PSEUDO CODE
create an empty int variable and call it count

use for loop
    take the first value 
    change the value to a string
    count the characters and assign to a variable
    control the variable with if statement and %
    increase the count varieble by 1
"""


nums = [555,901,482,1771]
count = 0 

for num in range (len(nums)):
    numbers_in_order = nums[num]
    str_num = str(numbers_in_order)
    number_digits = len(str_num)
    if number_digits % 2==0:
        count +=1
print(count)