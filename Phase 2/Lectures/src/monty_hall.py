def play_mh(my_sel=1):
    
    import numpy as np

    doors = {1, 2, 3}

    prize = np.random.choice(list(doors))

    if prize != my_sel:
        (reveal,) = doors - {prize} - {my_sel}
    else:
        reveal = np.random.choice(list(doors - {prize}))
    
    (rem,) = doors - {reveal} - {my_sel}
    
    print(f'Monty reveals a goat behind Door #' + str(reveal))
    print(f'Do you wish to swap to Door #' + str(rem) + '?')
    
    choice = input('y or n: ')
    
    if choice == 'y':
        my_sel = rem
    
    if my_sel == prize:
        win = 'YOU WIN THE CAR!'
        result = 1
    
    else:
        win = 'you win a goat :('
        result = 0
    
    print(f'You open Door #' + str(my_sel) + ' and . . . ' + win)
    
    return result



def stats_mh(swap=True):
    
    import numpy as np

    doors = {1, 2, 3}

    prize = np.random.choice(list(doors))
    my_sel = np.random.choice(list(doors))

    if prize != my_sel:
        (reveal,) = doors - {prize} - {my_sel}
    else:
        reveal = np.random.choice(list(doors - {prize}))
    
    (rem,) = doors - {reveal} - {my_sel}
    
    if swap == True:
        my_sel = rem
    
    if my_sel == prize:
        result = 1
    
    else:
        result = 0
    
    return result