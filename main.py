from game import Game, GameStatistics
def main():
    game = Game()
    stats = GameStatistics()
    print("Добро пожаловать в игру 'Камень, Ножницы, Бумага'!")
    print(f"Первый игрок, который наберет 8 очков, выигрывает!")

    while not game.is_game_over():
        user_choice = input("Введите ваш выбор (rock, paper, scissors): ").lower()
        if user_choice not in game.choices:
            print("Неверный выбор. Пожалуйста, попробуйте еще раз.")
            continue

        result, computer_choice = game.play_round(user_choice)
        print(f"Компьютер выбрал: {computer_choice}")

        if result == 'draw':
            print("Ничья!")
        elif result == 'user':
            print("Вы выиграли раунд!")
        else:
            print("Компьютер выиграл раунд!")

        print(f"Счет: Вы {game.user_score} - Компьютер {game.computer_score}")

    if game.user_score >= 8:
        print("Поздравляем! Вы выиграли игру!")
        stats.record_game('user')
    else:
        print("Компьютер выиграл игру!")
        stats.record_game('computer')
    print(
        f"Сыграно партий {stats.games_played}, Выигрыши пользователя: {stats.user_wins}, Выигрыши компьютера: {stats.computer_wins}")


if __name__ == "__main__":
    main()
