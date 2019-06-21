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
Print the mode on a new line;
if more than one such value exists, print the numerically smallest one.
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

INPUTSTR = []
for n in fileinput.input():
    INPUTSTR.append(n.split(" "))

NUM_AMOUNT = int(INPUTSTR[0][0])
NUMS = INPUTSTR[1:][0]
NUMS = sorted([int(i) for i in NUMS])

def mean():
    num_sum = sum(NUMS)
    return num_sum/NUM_AMOUNT

def median():
    if NUM_AMOUNT%2 == 0:
        median_id = int(NUM_AMOUNT/2)
        return (NUMS[median_id-1] + NUMS[median_id])/2
    else:
        return NUMS(int(NUM_AMOUNT/2))

def mode():
    vals_dict = dict()
    for i in set(NUMS):
        vals_dict[i] = 0

    for i in NUMS:
        vals_dict[i] += 1

    highest_v_candidates = []
    for k, v in vals_dict.items():
        highest_v_candidates.append(v)

    highest_v = max(highest_v_candidates)

    potential_mode = []
    for k, v in vals_dict.items():
        if highest_v == v:
            potential_mode.append(k)
    return min(potential_mode)


print(mean())
print(median())
print(mode())
