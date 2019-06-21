'''
Input Format

The first line contains an integer, N , denoting the number of elements in the array.
The second line contains N space-separated integers describing the array's elements.
'''

'''
Output Format

Print  lines of output in the following order:

Print the mean on a new line, to a scale of 1 decimal place (i.e., 12.3 ,7.0).
Print the median on a new line, to a scale of 1 decimal place (i.e., 12.3 ,7.0).
Print the mode on a new line; if more than one such value exists, print the numerically smallest one.
'''

'''
Sample Input

10
64630 11735 14216 99233 14470 4978 73429 38120 51135 67060
'''

'''
Sample Output

43900.6
44627.5
4978
'''

import fileinput
import sys

input_str = []
for n in fileinput.input():
    input_str.append(n.split(" "))

num_amount = int(input_str[0][0])
nums = input_str[1:][0]
nums = sorted([int(i) for i in nums])

def mean():
    num_sum = sum(nums)
    return num_sum/num_amount

def median():
    if num_amount%2==0:
        median_id = int(num_amount/2)
        return (nums[median_id-1] + nums[median_id])/2
    else:
        return nums(int(num_amount/2))

def mode():
    vals_dict = dict()
    for i in set(nums):
        vals_dict[i] = 0

    for i in nums:
        vals_dict[i] += 1

    highest_v_candidates = []
    for k,v in vals_dict.items():
        highest_v_candidates.append(v)

    highest_v = max(highest_v_candidates)

    potential_mode = []
    for k,v in vals_dict.items():
        if highest_v == v:
            potential_mode.append(k)
    return min(potential_mode)


print(mean())
print(median())
print(mode())
