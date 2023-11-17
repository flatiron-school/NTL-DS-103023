def pi_approx(n):
    """This function approximates pi.
    User inputs a number of points to choose
    from the space [-1, 1] x [-1, 1] and the
    function counts the number of times that
    the points fall inside the unit circle."""
    
    import numpy as np
    X = np.linspace(-1, 1, 100000)
    Y = X
    ctr = 0
    for _ in range(n):    
        X_r = np.random.choice(X)
        Y_r = np.random.choice(Y)
        if X_r ** 2 + Y_r ** 2 <= 1:
            ctr += 1
    return 4 * ctr / n