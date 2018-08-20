def minion_game(string):
    Kevin = 0
    Stuart = 0

    for i,j in enumerate(string):
        if j in 'AEIOU':
            Kevin += len(string) - i
        else:
            Stuart += len(string) - i

    if Stuart > Kevin:
        return('Stuart ' + str(Stuart))
    elif Stuart < Kevin:
        return('Kevin ' + str(Kevin))
    else:
        return('Draw')

print(minion_game('BANANA'))
