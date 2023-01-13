def first_odd():
    """Prints every odd number between 1 and 100"""
    for odd in range(1,100):
        if odd % 2 ==0:
            continue
        else:
            print(odd)
     

first_odd()