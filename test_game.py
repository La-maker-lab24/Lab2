import unittest
from game import Game, GameStatistics

class TestGame(unittest.TestCase):

    def setUp(self):
        self.game = Game()
        self.stats = GameStatistics()

    def test_play_round(self):
        result, computer_choice = self.game.play_round('rock')
        self.assertIn(computer_choice, ['rock', 'paper', 'scissors'])
        self.assertIn(result, ['user', 'computer', 'draw'])

    def test_determine_winner(self):
        self.assertEqual(self.game._determine_winner('rock', 'scissors'), 'user')
        self.assertEqual(self.game._determine_winner('paper', 'rock'), 'user')
        self.assertEqual(self.game._determine_winner('scissors', 'paper'), 'user')
        self.assertEqual(self.game._determine_winner('rock', 'paper'), 'computer')
        self.assertEqual(self.game._determine_winner('paper', 'scissors'), 'computer')
        self.assertEqual(self.game._determine_winner('scissors', 'rock'), 'computer')
        self.assertEqual(self.game._determine_winner('rock', 'rock'), 'draw')

    def test_update_scores(self):
        self.game._update_scores('user')
        self.assertEqual(self.game.user_score, 1)
        self.assertEqual(self.game.computer_score, 0)

        self.game._update_scores('computer')
        self.assertEqual(self.game.user_score, 1)
        self.assertEqual(self.game.computer_score, 1)

    def test_is_game_over(self):
        self.game.user_score = 8
        self.assertTrue(self.game.is_game_over())
        self.game.user_score = 7
        self.game.computer_score = 8
        self.assertTrue(self.game.is_game_over())
        self.game.user_score = 7
        self.game.computer_score = 7
        self.assertFalse(self.game.is_game_over())

    def test_reset_game(self):
        self.game.user_score = 5
        self.game.computer_score = 3
        self.game.reset_game()
        self.assertEqual(self.game.user_score, 0)
        self.assertEqual(self.game.computer_score, 0)

    def test_game_statistics(self):
        self.stats.record_game('user')
        self.stats.record_game('computer')
        self.assertEqual(self.stats.games_played, 2)
        self.assertEqual(self.stats.user_wins, 1)
        self.assertEqual(self.stats.computer_wins, 1)

    def test_reset_statistics(self):
        self.stats.record_game('user')
        self.stats.record_game('computer')
        self.stats.reset_statistics()
        self.assertEqual(self.stats.games_played, 0)
        self.assertEqual(self.stats.user_wins, 0)
        self.assertEqual(self.stats.computer_wins, 0)

if __name__ == '__main__':
    unittest.main()
