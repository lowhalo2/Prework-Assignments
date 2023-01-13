def is_consecutive(a_list):
    """
    Checks imputed list to see if it's in 
    consecutive order and return a boolean
    """
    boolean = True
    for index, num in enumerate(a_list):
        if index == 0:
            continue
        elif num-1 == a_list[index-1]:
            boolean = True
        else:
            boolean = False
            break
    return(boolean)

test_list = [12,13,14,15,16]
print(is_consecutive(test_list))