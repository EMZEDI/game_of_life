#  Shahrad Mohammadzadeh
#  ID:260955645
#  Game of life code
 
 
def is_valid_universe(my_2D_list):
    """(list)-> bool
    Given a 2D list (or a list) the function detects if its a valid universe based on the rules
    given in the handout or not. It returns a boolean True if its a valid universe False otherwise.
    >>> is_valid_universe([[1,2,3]])
    False
    >>> is_valid_universe([[1,0,0], [1,1]])
    False
    >>> is_valid_universe([[0,1], [0,1], [0,0]])
    True
    """
    # checks type of sublists
    for elem in my_2D_list: 
        if type(elem) != list:
            return False
    # checks if the outer list is empty or not    
    if len(my_2D_list) == 0:  
        return False
    
    # iterate through the outer list to check the conditons
    for element in my_2D_list:
        # checks if all the elementd are 0,1
        if element.count(0) + element.count(1) == len(element): 
            continue
        else:
            return False
    
    # iterates through the list to check if its rectangular or not
    for i in range(len(my_2D_list)): 
        if len(my_2D_list) == 1 or i == len(my_2D_list) - 1: # checks if the length is one or 
            break                                            # reached the last index
        # to check length of all sublists
        elif len(my_2D_list[i]) == len(my_2D_list[i+1]): 
            continue
        else:
            return False
        
    return True # if all the tests pass, it returns true
 
 
 
def universe_to_str(my_2D_list):  
    """(list)->str
    given a valid universe() described above, the function changes the int value
    of the universe to a string representation of it.
    >>> a = universe_to_str([[0,0,0], [1,0,1], [1,1,1], [0,0,1], [0,1,0], [0,0,0]])
    >>> print(a)
    +---+
    |   |
    |* *|
    |***|
    |  *|
    | * |
    |   |
    +---+
    >>> b = [[0, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 1, 0, 1, 0], \
              [0, 0, 1, 0, 0], [0, 0, 0, 0, 0]]
    >>> print(universe_to_str(b))
    +-----+
    |     |
    |  *  |
    | * * |
    |  *  |
    |     |
    +-----+
    >>> x = [[1,0], [0,1]]
    >>> print(universe_to_str(x))
    +--+
    |* |
    | *|
    +--+
    """
    # to be used in the first and the last/ strings that will be concatenated with
    #the other strings later on
    
    first_last = ("+" + ((len(my_2D_list[0])) * "-") + "+")   
    final_str = ''
    
    # iteratre through the list and starts changing to string
    for element in my_2D_list: 
        string = ''
        start = ("|")
        string += start
        
        # iterates through each element and finds 1s and 0s
        for el in element:   
            if el == 1:
                one = ("*")
                string += one
            else:
                zero = (" ")
                string += zero
         
         # adds the modifications to the final string
        final_str += (string + "|" + "\n")  
    
    
    return (first_last + "\n" + final_str + first_last)  # return the final string
    
 
 
def count_live_neighbors(universe, x, y):
    """(list, int, int)->int
    Given a valid universe and two arguments x, y presenting the location of a cell
    the function calculates the live neighbors around the mentiuoned cell
    diagonaly and in height and width!
    >>> beehive = [[0, 0, 0, 0, 0, 0], \
                  [0, 0, 1, 1, 0, 0], \
                  [0, 1, 0, 0, 1, 0], \
                  [0, 0, 1, 1, 0, 0], \
                  [0, 0, 0, 0, 0, 0]]
    >>> count_live_neighbors(beehive,  1,  3)
    2
    >>> a = [[0,0], \
            [1,0]]
    >>> count_live_neighbors(a, 0, 0)
    1
    >>> b = [[1,1,1], \
            [1,1,1], \
            [1,1,1], \
            [0,0,0]]
    >>> count_live_neighbors(b, 3, 2)
    2
    >>> count_live_neighbors(b, 1, 2)
    5
    """
    neighbors = 0  # int of neighbors
    a = True  # used in while loops later
    
    # iterate through the row before and check neighborhood
    for index in [-1, 0, 1]:  
        while a:
            try:
                #  checks if the index is <0 or not
                if x-1 < 0 or y+index < 0:  
                    a = False
                    continue
                # if there is live neighbor in the last row
                if universe[x-1][y+index] == 1:  
                    neighbors += 1
                    a = False
                else:
                    a = False
                     # if not, do nothing
            except(IndexError): 
                a = False
                continue
        a = True # change a back to true
    
    
     # iterate through the row that the element is existing at
    for index2 in [-1, 1]: 
        while a:
            try:
                #  checks if the index is <0 or not
                if x<0 or y+index2<0:  
                    a = False
                    continue
                # if there is live neighbor in the last row
                if universe[x][y+index2] == 1:  
                    neighbors += 1
                    a = False
                else:
                    a = False
            except(IndexError):  # if not, do nothing
                a = False
                continue
        a = True # change a back to true
        
        
    # iterate though the next row   
    for index3 in [-1, 0, 1]: 
        while a:
            try:
                #  checks if the index is <0 or not
                if x+1<0 or y+index3<0:  
                    a = False
                    continue
                # if there is live neighbor in the last row
                if universe[x+1][y+index3] == 1:  
                    neighbors += 1
                    a = False
                else:
                    a = False
            except(IndexError):  # if not, do nothing
                a = False
                continue
        a = True # change a back to true 
        
    return neighbors
 
 
 
def get_next_gen_cell(universe2, x, y):
    """(list)->int
    Given a valid universe as an input plus integers x and y (location), the function returns the
    state of the specified cell in the next generation. Based on the rules of the game
    >>> beehive = [[0,0,0,0,0,0],[0,0,1,1,0,0],[0,1,0,0,1,0],[0,0,1,1,0,0],[0,0,0,0,0,0]]
    >>> get_next_gen_cell(beehive, 1, 3)
    1
    >>> get_next_gen_cell(beehive, 2, 3)
    0
    >>> a = [[1,0], [1,0]]
    >>> get_next_gen_cell(a, 0, 0)
    0
    >>> get_next_gen_cell(a, 1, 1)
    0
    >>> c = [[1,1,1], [0,1,1], [0,0,1], [1,1,0]]
    >>> get_next_gen_cell(c, 2, 2)
    1
    """
    # live at the beginning 
    if universe2[x][y] == 1: 
        if count_live_neighbors(universe2, x, y)<2 or count_live_neighbors(universe2, x, y)>3:
            # when the live neighbots are less than 2 or more than 3
            return 0
        elif count_live_neighbors(universe2, x, y) in (2, 3): # otherwise return 1
            return 1
    else:
        if count_live_neighbors(universe2, x, y) == 3: # other case, when live neighbors are 3
            return 1
        else:
            return 0 # otherwise returns 0
            
    
 
def get_next_gen_universe(universe1):
    """(list) -> list
    Given a valid universe as an input, the function returns a two-dim list
    of integers with equal dimensions representing the universe in its next generation
    >>> tub = [[0, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 1, 0, 1, 0], \
              [0, 0, 1, 0, 0], [0, 0, 0, 0, 0]]
    >>> get_next_gen_universe(tub)
    [[0, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 1, 0, 1, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 0]]
    >>> a = [[0,0], [0,1]]
    >>> get_next_gen_universe(a)
    [[0, 0], [0, 0]]
    >>> b = [[1,1,1], [0,0,0], [1,1,0], [0,0,1], [0,0,0]]
    >>> get_next_gen_universe(b)
    [[0, 1, 0], [0, 0, 1], [0, 1, 0], [0, 1, 0], [0, 0, 0]]
    """
    next_gen_uni = [] # next gen univserse
    element_edit = [] # edits the element later
    
    # iterate through the universe 1 and add sublists to new lists
    for index in range(len(universe1)):
        
        # iterate again for the elements of the elements
        for jindex in range(len(universe1[index])):
            a = (get_next_gen_cell(universe1, index, jindex)) # add sublists to new lists
            element_edit = element_edit + [get_next_gen_cell(universe1, index, jindex)]
           
        next_gen_uni.append(element_edit) # add the new lists to the final changed list
        element_edit = [] # turn back to cmpty list        
    return next_gen_uni # return the final list
 
 
 
def get_n_generations(final_universe, n):
    """(list)->str
    given a universe and an integer n, the function finds the next m generations of the universe
    If the universe is periodic(based on the rules mentioned in the assignment), m equals the min
    between n and the period of the universe. Otherwise, m equals the period.
    If the types of the inputs are not correct, we face a typeerror
    if not a valid universe we face a value error
    if n is not greater than zero we get value error
    >>> tub = [[0, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 1, 0, 1, 0], \
                 [0, 0, 1, 0, 0], [0, 0, 0, 0, 0]]
    >>> g = get_n_generations(tub, 5)
    >>> len(g)
    1
    >>> a = [[0,0], [0,1], [1,0], [0,0]]
    >>> b = get_n_generations(a, 21)
    >>> len(b)
    2
    >>> print(b[1])
    +--+
    |  |
    |  |
    |  |
    |  |
    +--+
    >>> get_n_generations(a, -2)
    Traceback (most recent call last):
    ValueError: Not a positive number n
    >>> get_n_generations([1,2], -2)
    Traceback (most recent call last):
    ValueError: Not a valid universe
    >>> get_n_generations(0, 2)
    Traceback (most recent call last):
    TypeError: Not the decent types
    """
    if (type(final_universe) != list) or (type(n) != int): # raise Type error
        raise TypeError("Not the decent types")
    
    if not is_valid_universe(final_universe): # raise value error
        raise ValueError("Not a valid universe")
    
    if n <= 0: # raise value error
        raise ValueError("Not a positive number n")
    
    copy = []
    #copy final universe to a new list to use later
    for el in final_universe:
        cop = [] # a new copy
        for element in el:
            cop = cop + [element]    
        copy.append(cop)
    
    m = n # to start with
 
    for i in range(n): # iterate through the universe
        if get_next_gen_universe(final_universe) == final_universe:
            m = i + 1
            break
        else:
            final_universe = get_next_gen_universe(final_universe)
 
    
    list_of_str = [] # to be changed later in the iteration
    for j in range(m):
        list_of_str.append(universe_to_str(copy)) # add the copy str to the new list
        copy = get_next_gen_universe(copy) # change copy to the new universe 
        
    return list_of_str 
 
