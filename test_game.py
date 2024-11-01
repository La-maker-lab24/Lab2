import unittest
from game import Game, GameStatistics

class TestGame(unittest.TestCase):

    def setUp(self):
        self.game = Game()
        self.statistics = GameStatistics()

    def test_play_round_user_wins(self):
        self.game._get_computer_choice = lambda: 'scissors'
        result, computer_choice = self.game.play_round('rock')
        self.assertEqual(result, 'user')
        self.assertEqual(computer_choice, 'scissors')

    def test_play_round_computer_wins(self):
        self.game._get_computer_choice = lambda: 'rock'
        result, computer_choice = self.game.play_round('scissors')
        self.assertEqual(result, 'computer')
        self.assertEqual(computer_choice, 'rock')

    def test_play_round_draw(self):
        self.game._get_computer_choice = lambda: 'rock'
        result, computer_choice = self.game.play_round('rock')
        self.assertEqual(result, 'draw')
        self.assertEqual(computer_choice, 'rock')

    def test_game_statistics(self):
        self.statistics.record_game('user')
        self.statistics.record_game('computer')
        self.statistics.record_game('user')

        stats = self.statistics.get_statistics()
        self.assertEqual(stats['games_played'], 3)
        self.assertEqual(stats['user_wins'], 2)
        self.assertEqual(stats['computer_wins'], 1)

    def test_reset_statistics(self):
        self.statistics.record_game('user')
        self.statistics.reset_statistics()
        stats = self.statistics.get_statistics()
        self.assertEqual(stats['games_played'], 0)
        self.assertEqual(stats['user_wins'], 0)
        self.assertEqual(stats['computer_wins'], 0)

    def test_is_game_over(self):
        self.game.user_score = 8
        self.assertTrue(self.game.is_game_over())

    def test_reset_game(self):
        self.game.user_score = 5
        self.game.computer_score = 3
        self.game.reset_game()
        self.assertEqual(self.game.user_score, 0)
        self.assertEqual(self.game.computer_score, 0)

if __name__ == '__main__':
    unittest.main()
