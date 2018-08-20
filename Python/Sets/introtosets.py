#Sample Input
#10

#Sample Output
#169.375

def average(array):
    print("ARR", arr)
    setused = list(set(arr))
    #print(setused)
    average = (sum(setused)/len(setused))
    return(average)
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
