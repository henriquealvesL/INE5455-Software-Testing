import unittest
from src import puzzle_game

class TestBoardCoverage(unittest.TestCase):
    def setUp(self):
        self.puzzle = puzzle_game.PuzzleGame(3)        
   
    def test_get_tile_SCPath_1(self):
        with self.assertRaises(puzzle_game.InvalidPositionException):
            self.puzzle.get_tile(-5, 2)
 
    def test_get_tile_SCPath_2(self):
        tile = self.puzzle.get_tile(2, 3)
        self.assertEqual(tile, 6)
            
    def test_get_tile_SCPath_3(self):
        tile = self.puzzle.get_tile(3, 3)
        self.assertEqual(tile, " ")
        
    def test_get_tile_BCPath_1(self):
        with self.assertRaises(puzzle_game.InvalidPositionException):
            self.puzzle.get_tile(-5, 2)    
        
    def test_get_tile_BCPath_2(self):
        with self.assertRaises(puzzle_game.InvalidPositionException):
            self.puzzle.get_tile(5, 2)  
        
    def test_get_tile_BCPath_3(self):
        with self.assertRaises(puzzle_game.InvalidPositionException):
            self.puzzle.get_tile(3, -5)    
        
    def test_get_tile_BCPath_4(self):
        with self.assertRaises(puzzle_game.InvalidPositionException):
            self.puzzle.get_tile(2, 5)    
        
    def test_get_tile_BCPath_5(self):
        tile = self.puzzle.get_tile(2, 3)
        self.assertEqual(tile, 6)   
        
    def test_get_tile_BCPath_6(self):
        tile = self.puzzle.get_tile(3, 2)
        self.assertEqual(tile, 8)   
        
    def test_get_tile_BCPath_7(self):
        tile = self.puzzle.get_tile(3, 3)
        self.assertEqual(tile, " ")   