import random


class Game:
    def __init__(self, finish_score=8):
        self.user_score = 0
        self.computer_score = 0
        self.finish_score = finish_score
        self.choices = ['rock', 'paper', 'scissors']
        self.user_choices_history = {'rock': 0, 'paper': 0, 'scissors': 0}
        self.previous_choices = []

    def play_round(self, user_choice):
        self.user_choices_history[user_choice] += 1
        self.previous_choices.append(user_choice)
        if len(self.previous_choices) > 3:
            self.previous_choices.pop(0)
        computer_choice = self.get_computer_choice()
        result = self._determine_winner(user_choice, computer_choice)
        self._update_scores(result)
        return result, computer_choice

    def get_computer_choice(self):
        total_choices = sum(self.user_choices_history.values())
        if total_choices == 0:
            return random.choice(self.choices)
        last_choice = self.previous_choices[-1] if self.previous_choices else None
        second_last_choice = self.previous_choices[-2] if len(self.previous_choices) > 1 else None
        if last_choice == second_last_choice:
            if last_choice == 'rock':
                return 'paper'
            elif last_choice == 'paper':
                return 'scissors'
            elif last_choice == 'scissors':
                return 'rock'

        probabilities = {choice: count / total_choices for choice, count in self.user_choices_history.items()}
        user_probable_choice = max(probabilities, key=probabilities.get)

        if user_probable_choice == "rock":
            return "paper"
        elif user_probable_choice == "paper":
            return "scissors"
        else:
            return "rock"

    def _determine_winner(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            return 'draw'
        elif (user_choice == 'rock' and computer_choice == 'scissors') or \
                (user_choice == 'paper' and computer_choice == 'rock') or \
                (user_choice == 'scissors' and computer_choice == 'paper'):
            return 'user'
        else:
            return 'computer'

    def _update_scores(self, result):
        if result == 'user':
            self.user_score += 1
        elif result == 'computer':
            self.computer_score += 1

    def is_game_over(self):
        return self.user_score >= self.finish_score or self.computer_score >= self.finish_score

    def reset_game(self):
        self.user_score = 0
        self.computer_score = 0
        self.user_choices_history = {'rock': 0, 'paper': 0, 'scissors': 0}
        self.previous_choices = []


class GameStatistics:
    def __init__(self):
        self.games_played = 0
        self.user_wins = 0
        self.computer_wins = 0

    def record_game(self, winner):
        self.games_played += 1
        if winner == 'user':
            self.user_wins += 1
        elif winner == 'computer':
            self.computer_wins += 1

    def get_statistics(self):
        return {
            'games_played': self.games_played,
            'user_wins': self.user_wins,
            'computer_wins': self.computer_wins
        }

    def reset_statistics(self):
        self.games_played = 0
        self.user_wins = 0
        self.computer_wins = 0
