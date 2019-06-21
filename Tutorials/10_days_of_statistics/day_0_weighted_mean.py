'''
Input Format

The first line contains an integer, N, denoting the number of elements in arrays X and W.
The second line contains N space-separated integers describing the respective elements of array X.
The third line contains N space-separated integers describing the respective elements of array W.

Output Format

Print the weighted mean on a new line.
Your answer should be rounded to a scale of 1 decimal place (i.e., 12.3 format).
'''

'''
Sample Input

5
10 40 30 50 20
1 2 3 4 5

Sample Output

32.0
'''


import fileinput

def main():
    the_input = []
    for i in fileinput.input():
        the_input.append(i.split(' '))

    n_of_els = int(the_input[0][0].lstrip('\n'))
    x_arr_els = the_input[1]
    x_arr_els = [int(i.rstrip('\n')) for i in x_arr_els]
    w_arr_els = the_input[2]
    w_arr_els = [int(i.rstrip('\n')) for i in w_arr_els]
    print(weighted_avg(n_of_els, x_arr_els, w_arr_els))

def weighted_avg(n_els, x_arr, w_arr):
    tot_weighted_sum = 0
    sum_of_weights = 0
    for i in range(n_els):
        tot_weighted_sum += x_arr[i] * w_arr[i]
        sum_of_weights += w_arr[i]
    return round(tot_weighted_sum/sum_of_weights, 1)

main()
