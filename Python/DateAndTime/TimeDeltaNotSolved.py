import sys

def time_delta(t1, t2):
    return(t1 - t2)
    # Complete this function

t = int(input().strip())
for a0 in range(t):
    t1 = input().strip()
    t2 = input().strip()
    delta = time_delta(t1, t2)
    print(delta)
