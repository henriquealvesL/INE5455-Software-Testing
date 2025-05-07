import unittest
import sys
from io import StringIO
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
    
    def test_get_tile_first_line_valid(self):
        """
        Mutant 172:
        Valida que posições na primeira linha sejam aceitas.
        Por exemplo, (1,1) deve retornar 1 e (1,2) retornar 2.
        Esse teste mata o mutant 172, que rejeitaria linhas = 1.
        """
        tile1 = self.puzzle.get_tile(1, 1)
        self.assertEqual(tile1, 1)
        tile2 = self.puzzle.get_tile(1, 2)
        self.assertEqual(tile2, 2)
    
    def test_get_tile_invalid_column_zero(self):
        """
        Mutant 174:
        Testa que uma coluna 0 é inválida.
        Segundo a especificação original, coluna deve ser > 0.
        Esse teste mata o mutant 174, que permitia column >= 0.
        """
        with self.assertRaises(puzzle_game.InvalidPositionException):
            self.puzzle.get_tile(2, 0)
    
    def test_get_tile_first_column_valid(self):
        """
        Mutant 175:
        Testa que posições com coluna igual a 1 são válidas.
        Por exemplo, (2,1) deve retornar 4,
        já que a primeira coluna é válida.
        Esse teste mata o mutant 175, que exigiria column > 1.
        """
        tile = self.puzzle.get_tile(2, 1)
        self.assertEqual(tile, 4)

    def test_get_tile_invalid_line_zero(self):
        """
        Mutant 171:
        Testa que a linha 0 é inválida.
        Segundo a especificação, linha deve ser > 0.
        Esse teste mata o mutant 171, que permitiria line >= 0.
        """
        with self.assertRaises(puzzle_game.InvalidPositionException):
            self.puzzle.get_tile(0, 1)
    
    def test_print_board_output(self):
        """
        Mutant 170:
        Testa a saída da função de impressão do tabuleiro.
        Esse teste mata o mutant 170, que insere 'XXXX' na formatação da saída.
        """
        captured_output = StringIO()
        sys.stdout = captured_output
        
        self.puzzle.__print_board_of_puzzle_game__()
        
        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()

        expected_output = "1 2 3 \n4 5 6 \n7 8 - \n"

        self.assertEqual(output, expected_output, "A saída do print_board não corresponde ao esperado.")

if __name__ == '__main__':
    unittest.main()