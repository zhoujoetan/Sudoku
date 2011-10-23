import copy

def read_sudoku(file):
    '''read sudoku puzzle from a given file.'''
    stream = open(file)
    data = stream.readlines()
    stream.close()
    return eval("".join(data))

def convertToSets(problem):
    '''convert the two-dimensional array of integers to sets.'''
    x = {1, 2, 3, 4, 5, 6, 7, 8, 9}
    ret = copy.deepcopy(problem)        #deepcopy a nested list 
    for i in range(len(problem)):
        for j in range(len(problem[i])):
            if problem[i][j] == 0:
                ret[i][j] = copy.deepcopy(x)    #sets are mutable!
            else:
                ret[i][j] = {ret[i][j]}     #convert integer to set
    return ret  

def convertToInts(problem):
    '''convert the two-dimensional array of sets to integers.'''
    ret = copy.deepcopy(problem) 
    for i in range(len(problem)):
        for j in range(len(problem[i])):
            if len(problem[i][j]) == 1:     #convert sets to int
                ret[i][j] = list(problem[i][j])[0]  #cannot index sets
            else:
                ret[i][j] = 0       #if this set contains more than 1 int
    return ret  

def getRowLocations(rowNumber):
    '''return a list of all nine locations given a rowNumber.'''
    return [(rowNumber, i) for i in range(9)]

def getColumnLocations(columnNumber):
    '''return a list of all nine locations given a columnNumber.'''
    return [(i, columnNumber) for i in range(9)]

def getBoxLocations(Location):
    '''return a list of all nine locations within the same box 
       given a location.'''
    row = Location[0] // 3 * 3          #put (row, column) on top-left corner
    column = Location[1] // 3 * 3
    return [((row + i), (column + j)) for j in range(3) for i in range(3)]

def eliminate(problem, location, listOfLocations):
    '''remove the number in location from listOfLocations.'''
    sets = problem[location[0]][location[1]]
    if len(sets) != 1:
        print('Location should contain only 1 number!')
        return 0
    removals = 0
    element = list(sets)[0]
    for loc in listOfLocations:
        if loc != location:      #element at location must be excluded
            #principle: if element is in the set, then delete it from this set
            if element in problem[loc[0]][loc[1]]:  
                problem[loc[0]][loc[1]].remove(element)
                removals += 1           #record the total removals
    return removals

def isSolved(problem):
    '''determine if a sudoku is solved.'''
    for i in range(9):
        for j in range(9):
            #sudoku is solved if every location has only 1 number
            if len(problem[i][j]) != 1:     
                return False
    return True

def solve(problem):
    '''try solving the given sudoku problem and print the result out.'''
    while True:
        removals = 0
        for i in range(9):
            for j in range(9):
                if len(problem[i][j]) == 1:
                    #include row, column and box location
                    listOfLocations = getRowLocations(i) \
                                      + getColumnLocations(j) \
                                      + getBoxLocations((i, j))
                    #eliminate numbers from relative locations
                    removals += eliminate(problem, (i, j), listOfLocations)
        if removals == 0:       #this means no more elimination occur
            return isSolved(problem)

def print_sudoku(problem):
    '''print out current layout of sudoku'''
    boundry = '+-------' * 3 + '+'
    printProblem = copy.deepcopy(problem)
    print(boundry)
    for i in range(9):
        for j in range(3):
            for k in range(3):
                if printProblem[i][k + j * 3] == 0:
                   printProblem[i][k + j * 3] = '.' 
            print('|', printProblem[i][0 + j * 3], printProblem[i][1 + j * 3], 
                  printProblem[i][2 + j * 3], sep = ' ', end = ' ')
        print('|')
        if i % 3 == 2:
            print(boundry)
    return None

def main():
    print('This Sudoku project is presented by Mengyao Chai and Zhou Tan.')
    again = 'yes'
    while again == 'yes':
        fileName = input('Please provide a Sudouku puzzle file:')
        problem = read_sudoku(fileName)
        problemSets = convertToSets(problem) 
        print_sudoku(problem)
        isSolved = solve(problemSets)
        print_sudoku(convertToInts(problemSets))                        
        # sudoku cannot be solved
        if not isSolved:
            #print out unsolved locations and possible candidates
            for i in range(9):
                for j in range(9):
                    if len(problemSets[i][j]) != 1:
                        loc = (i, j)
                        print('Location', loc, 'might be any of', 
                              problemSets[i][j], sep = ' ')
        again = input('Do you want to play another puzzle(yes/no)?')
    return None
