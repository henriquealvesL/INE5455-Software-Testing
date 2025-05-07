import unittest
from unittest.mock import patch
from src import puzzle_game
from src.puzzle_game_with_mock import PuzzleGameWithPlayer
from tests.shufflers_for_testing_puzzles import TestingShufflerPuzzleGame3x3To123456X78

class TestBoard(unittest.TestCase):
    def setUp(self):
        self.puzzle = puzzle_game.PuzzleGame(3)
        self.puzzle_with_player = PuzzleGameWithPlayer(3, "Player1")

    def test_get_tile_without_mock1(self):
        tile = self.puzzle.get_tile(3, 3)
        self.assertEqual(tile, " ")
 
    def test_get_tile_without_mock2(self):
        tile = self.puzzle.get_tile(2, 3)
        self.assertEqual(tile, 6)
        
    @patch('src.puzzle_game.PuzzleGame.get_tile')
    def test_get_tile_with_mock1(self, mock_get_tile):
        mock_get_tile.return_value = 3
        tile = self.puzzle.get_tile(3, 3)
        self.assertNotEqual(tile, " ")

    @patch('src.puzzle_game.PuzzleGame.get_tile')
    def test_get_tile_with_mock2(self, mock_get_tile):
        mock_get_tile.return_value = 5
        tile = self.puzzle.get_tile(2, 3)
        self.assertNotEqual(tile, 6)
        
    def test_end_of_the_game_without_mock_saved(self):
        result = self.puzzle_with_player.end_of_the_game()
        self.assertEqual(result, "Saved")

    def test_end_of_the_game_without_mock_not_finished(self):
        TestingShufflerPuzzleGame3x3To123456X78.shuffle(self, self.puzzle_with_player)
        result = self.puzzle_with_player.end_of_the_game()
        self.assertEqual(result, "Game not finished")
        
    @patch('src.puzzle_game_with_mock.PuzzleGameWithPlayer.save_game_to_file')
    def test_end_of_the_game_with_mock_saved(self, mock_save_game_to_file):
        mock_save_game_to_file.return_value = "Saved"
        result = self.puzzle_with_player.end_of_the_game()
        self.assertEqual(result, "Saved")
        mock_save_game_to_file.assert_called_once()
        
    @patch('src.puzzle_game_with_mock.PuzzleGameWithPlayer.save_game_to_file')
    def test_end_of_the_game_with_mock_not_finished(self, mock_save_game_to_file):
        TestingShufflerPuzzleGame3x3To123456X78.shuffle(self, self.puzzle_with_player)
        mock_save_game_to_file.return_value = "Game not finished"
        result = self.puzzle_with_player.end_of_the_game()
        self.assertNotEqual(result, "Saved")
        mock_save_game_to_file.assert_not_called()


if __name__ == '__main__':
    unittest.main()