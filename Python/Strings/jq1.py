score = input("Enter Score: ")
try:
    score = float(score)
    if score>1:
        print('Over range')
        exit()
    elif score<0:
        print('Over range')
        exit()
except:
    if score<0.6:
        p == str(F)
    elif score<0.7:
        p == str(D)
    elif score<0.8:
        p == str(C)
    elif score<0.9:
        p == str(B)
    elif score<=1:
        p == str(A)
        print(p)
