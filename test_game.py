import unittest, random
from game import Game, GameStatistics
import unittest

class TestGame(unittest.TestCase):

    def setUp(self):
        self.game = Game()

    def test_initial_scores(self):
        self.assertEqual(self.game.user_score, 0)
        self.assertEqual(self.game.computer_score, 0)

    def test_play_round(self):
        result, computer_choice = self.game.play_round('rock')
        self.assertIn(computer_choice, self.game.choices)
        self.assertIn(result, ['user', 'computer', 'draw'])

    def test_determine_winner(self):
        self.assertEqual(self.game._determine_winner('rock', 'scissors'), 'user')
        self.assertEqual(self.game._determine_winner('scissors', 'rock'), 'computer')
        self.assertEqual(self.game._determine_winner('paper', 'paper'), 'draw')

    def test_update_scores(self):
        self.game._update_scores('user')
        self.assertEqual(self.game.user_score, 1)
        self.game._update_scores('computer')
        self.assertEqual(self.game.computer_score, 1)

    def test_game_over(self):
        self.game.user_score = 8
        self.assertTrue(self.game.is_game_over())
        self.game.reset_game()
        self.assertFalse(self.game.is_game_over())


class TestGameIntegration(unittest.TestCase):

    def setUp(self):
        self.game = Game()

    def test_full_game_flow(self):
        self.game.play_round('rock')
        self.game.play_round('paper')
        self.game.play_round('scissors')

        self.assertFalse(self.game.is_game_over())

        self.game.user_score = 8
        self.assertTrue(self.game.is_game_over())


class TestGameStatisticsIntegration(unittest.TestCase):

    def setUp(self):
        self.game = Game()
        self.stats = GameStatistics()

    def test_record_game_statistics(self):
        for _ in range(5):
            result, _ = self.game.play_round('rock')
            self.stats.record_game(result)

        self.assertEqual(self.stats.games_played, 5)
        self.assertTrue(self.stats.user_wins + self.stats.computer_wins <= 5)

    def test_reset_statistics(self):
        self.stats.record_game('user')
        self.stats.reset_statistics()
        self.assertEqual(self.stats.games_played, 0)
        self.assertEqual(self.stats.user_wins, 0)
        self.assertEqual(self.stats.computer_wins, 0)


if __name__ == '__main__':
    unittest.main()
