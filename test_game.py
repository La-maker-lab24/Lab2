import unittest, random
from game import Game, GameStatistics
import unittest

class TestGame(unittest.TestCase):

    def setUp(self):
        self.game = Game()
        self.stats = GameStatistics()

    def test_initial_scores(self):
        self.assertEqual(self.game.user_score, 0)
        self.assertEqual(self.game.computer_score, 0)

    def test_play_round(self):
        result, computer_choice = self.game.play_round('rock')
        self.assertIn(computer_choice, self.game.choices)
        self.assertIn(result, ['user', 'computer', 'draw'])
        result, computer_choice = self.game.play_round('paper')
        self.assertIn(computer_choice, self.game.choices)
        self.assertIn(result, ['user', 'computer', 'draw'])
        result, computer_choice = self.game.play_round('rock')
        self.assertIn(computer_choice, self.game.choices)
        self.assertIn(result, ['user', 'computer', 'draw'])

    def test_computer_choice_based_on_last_user_choice(self):
        self.game.play_round('rock')
        self.game.play_round('rock')
        computer_choice = self.game.get_computer_choice()
        self.assertEqual(computer_choice, 'paper')

        self.game.play_round('paper')
        self.game.play_round('paper')
        self.game.play_round('paper')
        computer_choice = self.game.get_computer_choice()
        self.assertEqual(computer_choice, 'scissors')

        self.game.play_round('scissors')
        self.game.play_round('scissors')
        self.game.play_round('scissors')
        computer_choice = self.game.get_computer_choice()
        self.assertEqual(computer_choice, 'rock')

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

    def test_full_game_flow(self):
        self.game.play_round('rock')
        self.game.play_round('paper')
        self.game.play_round('scissors')

        self.assertFalse(self.game.is_game_over())

        self.game.user_score = 8
        self.assertTrue(self.game.is_game_over())

    def test_reset_statistics(self):
        self.stats.record_game('user')
        self.stats.reset_statistics()
        self.assertEqual(self.stats.games_played, 0)
        self.assertEqual(self.stats.user_wins, 0)
        self.assertEqual(self.stats.computer_wins, 0)

    def test_computer_choice_when_no_previous_choices(self):
        computer_choice = self.game.get_computer_choice()
        self.assertIn(computer_choice, self.game.choices)
        self.game.play_round('rock')
        computer_choice = self.game.get_computer_choice()
        self.assertIn(computer_choice, self.game.choices)

    def test_get_statistics_initial(self):
        statistics = self.stats.get_statistics()
        self.assertEqual(statistics['games_played'], 0)
        self.assertEqual(statistics['user_wins'], 0)
        self.assertEqual(statistics['computer_wins'], 0)

    def test_record_game_statistics(self):
        self.stats.record_game('user')
        self.stats.record_game('computer')
        self.stats.record_game('user')
        statistics = self.stats.get_statistics()
        self.assertEqual(statistics['games_played'], 3)
        self.assertEqual(statistics['user_wins'], 2)
        self.assertEqual(statistics['computer_wins'], 1)


if __name__ == '__main__':
    unittest.main()
