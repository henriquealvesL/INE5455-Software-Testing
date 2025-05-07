import unittest
from src import puzzle_game


class TestBoardCoverage(unittest.TestCase):
    def setUp(self):
        self.puzzle = puzzle_game.PuzzleGame(3)

    def test_column_all_c_uses_1(self):
        print("Column all-c-uses 1:")
        line = 3
        column = 2
        tile = self.puzzle.get_tile(line, column)
        self.assertEqual(tile, 8)
        
        
    def test_column_all_p_uses_2(self):
        print("Column all-p-uses 2:")
        line = 3
        column = 3
        tile = self.puzzle.get_tile(line, column)
        self.assertEqual(tile, " ")

    def test_column_all_p_uses_3(self):
        print("Column all-p-uses 3:")
        line = -3
        column = 2
        with self.assertRaises(puzzle_game.InvalidPositionException) as context:
            self.puzzle.get_tile(line, column)

