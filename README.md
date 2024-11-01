![example workflow](https://github.com/La-maker-lab24/Lab2/actions/workflows/python-tests.yml/badge.svg)
[![Coverage Status](https://coveralls.io/repos/github/La-maker-lab24/Lab2/badge.svg?branch=main)](https://coveralls.io/github/La-maker-lab24/Lab2?branch=main)
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=La-maker-lab24_Lab2&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=La-maker-lab24_Lab2)
[![Bugs](https://sonarcloud.io/api/project_badges/measure?project=La-maker-lab24_Lab2&metric=bugs)](https://sonarcloud.io/summary/new_code?id=La-maker-lab24_Lab2)
[![Code Smells](https://sonarcloud.io/api/project_badges/measure?project=La-maker-lab24_Lab2&metric=code_smells)](https://sonarcloud.io/summary/new_code?id=La-maker-lab24_Lab2)
# План тестирования
Тест Б1
- Тест проверяет: Игрок выигрывает раунд.
- Тип: Позитивный
- Тип теста: Блочный
- Ввод: 'rock' (выбор игрока), компьютер выбирает 'scissors'
- Ожидаемый результат: Результат user, выбор компьютера scissors.

Тест Б2
- Тест проверяет: Компьютер выигрывает раунд.
- Тип: Позитивный
- Тип теста: Блочный
- Ввод: 'scissors' (выбор игрока), компьютер выбирает 'rock'
- Ожидаемый результат: Результат computer, выбор компьютера rock.

Тест Б3
- Тест проверяет: Ничья в раунде.
- Тип: Позитивный
- Тип теста: Блочный
- Ввод: 'rock' (выбор игрока), компьютер выбирает 'rock'
- Ожидаемый результат: Результат draw, выбор компьютера rock.

Тест Б4
- Тест проверяет: Проверка завершения игры.
- Тип: Позитивный
- Тип теста: Блочный
- Ввод: user_score = 8
- Ожидаемый результат: True (игра завершена).

Тест Б5
- Тест проверяет: Сброс игры.
- Тип: Позитивный
- Тип теста: Блочный
- Ввод: user_score = 5, computer_score = 3
- Ожидаемый результат: user_score = 0, computer_score = 0

Тест И1
- Тест проверяет: Запись статистики игры.
- Тип: Позитивный
- Тип теста: Интеграционный
- Ввод: Игрок выигрывает 2 раза, компьютер выигрывает 1 раз.
- Ожидаемый результат: {'games_played': 3, 'user_wins': 2, 'computer_wins': 1}.

Тест И2
- Тест проверяет: Сброс статистики игры.
- Тип: Позитивный
- Тип теста: Интеграционный
- Ввод: Игрок выигрывает 1 раз, затем статистика сбрасывается.
- Ожидаемый результат: {'games_played': 0, 'user_wins': 0, 'computer_wins': 0}.
