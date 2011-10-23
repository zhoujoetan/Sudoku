# CIT 591 Lab 4 assignment
# test for sudoku
# Zhou Tan and Mengyao Chai

import unittest
import sudoku

class test_sudoku(unittest.TestCase):

    def test_convertToSets(self):
        problem = sudoku.read_sudoku("./data/data1.txt")  #read the puzzle
        sets = sudoku.read_sudoku("./data/convertToSetsTest.txt")  #read the coverted sets
        emptySets = sudoku.read_sudoku("./data/emptySets.txt")
        self.assertEqual(emptySets, sudoku.convertToSets([[0] * 9] * 9))
        self.assertEqual([sets[0]], sudoku.convertToSets([problem[0]]))
        self.assertEqual(sets, sudoku.convertToSets(problem))

    def test_convertToInt(self):
        sets = sudoku.read_sudoku("./data/convertToSetsTest.txt")     #read the coverted sets
        problem = sudoku.read_sudoku("./data/data1.txt")  #read the puzzle
        emptySets = sudoku.read_sudoku("./data/emptySets.txt")
        self.assertEqual([[0] * 9] * 9, sudoku.convertToInts(emptySets))
        self.assertEqual(problem, sudoku.convertToInts(sets))
        self.assertEqual([problem[0]], sudoku.convertToInts([sets[0]]))

    def test_getRowLocations(self):
        row0 = [(0, 0), (0, 1), (0, 2), (0, 3), 
                (0, 4), (0, 5), (0, 6), (0, 7), (0, 8)]
        self.assertEqual(row0, sudoku.getRowLocations(0))

    def test_getColumnLocations(self):
        column0 = [(0, 0), (1, 0), (2, 0), (3, 0), 
                   (4, 0), (5, 0), (6, 0), (7, 0), (8, 0)]
        self.assertEqual(column0, sudoku.getColumnLocations(0))

    def test_getBoxLocations(self): 
        box0 = [(0, 0), (0, 1), (0, 2), (1, 0), 
                (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
        getBox = sudoku.getBoxLocations((1, 2))
        for coordinate in box0:
            self.assertTrue(coordinate in getBox)
        self.assertTrue(len(box0) == len(getBox))

    def test_eliminate(self):
        loc0 = (0,1)
        eliminate = sudoku.read_sudoku("./data/eliminateTest.txt")    #read the eliminate result
        problem = sudoku.read_sudoku("./data/data1.txt")  #read the puzzle
        problemSets = sudoku.convertToSets(problem)
        listOfLocation = sudoku.getRowLocations(loc0[0]) + sudoku.getColumnLocations(loc0[1]) \
                            + sudoku.getBoxLocations(loc0) 
        self.assertEqual(12, sudoku.eliminate(problemSets, loc0, listOfLocation))
        self.assertEqual(eliminate, problemSets)

    def test_isSolved(self):
        problem = sudoku.read_sudoku("./data/data1.txt")  #read the puzzle
        result = sudoku.read_sudoku("./data/result.txt")   #read the result 
        emptySets = sudoku.read_sudoku("./data/emptySets.txt")
        self.assertFalse(sudoku.isSolved(emptySets))
        self.assertFalse(sudoku.isSolved(sudoku.convertToSets(problem)))
        self.assertTrue(sudoku.isSolved(sudoku.convertToSets(result)))

    def test_solve(self):        
        result = sudoku.read_sudoku("./data/result.txt")   #read the result 
        problem = sudoku.read_sudoku("./data/data1.txt")  #read the puzzle
        problemSets = sudoku.convertToSets(problem)
        self.assertTrue(sudoku.solve(problemSets))
        self.assertEqual(result, sudoku.convertToInts(problemSets))

unittest.main()
