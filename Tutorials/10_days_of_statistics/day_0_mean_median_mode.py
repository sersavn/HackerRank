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
