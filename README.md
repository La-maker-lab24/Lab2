![example workflow](https://github.com/La-maker-lab24/Lab2/actions/workflows/python-tests.yml/badge.svg)
[![Coverage Status](https://coveralls.io/repos/github/La-maker-lab24/Lab2/badge.svg?branch=main)](https://coveralls.io/github/La-maker-lab24/Lab2?branch=main)
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=La-maker-lab24_Lab2&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=La-maker-lab24_Lab2)
[![Bugs](https://sonarcloud.io/api/project_badges/measure?project=La-maker-lab24_Lab2&metric=bugs)](https://sonarcloud.io/summary/new_code?id=La-maker-lab24_Lab2)
[![Code Smells](https://sonarcloud.io/api/project_badges/measure?project=La-maker-lab24_Lab2&metric=code_smells)](https://sonarcloud.io/summary/new_code?id=La-maker-lab24_Lab2)
# План тестирования

Тест Б1
 - Тест проверяет: Начальные очки пользователя и компьютера.
 - Тип: Позитивный
 - Тип теста: Блочный
 - Ввод: -
 - Ожидаемый результат: user_score равен 0, computer_score равен 0.

Тест Б2
 - Тест проверяет: Процесс игры в раунд с различными выбором пользователя.
 - Тип: Позитивный
 - Тип теста: Блочный
 - Ввод: 'rock', 'paper', 'rock'
 - Ожидаемый результат: computer_choice входит в список доступных ходов, результат раунда - 'user', 'computer' или 'draw'.

Тест Б3
 - Тест проверяет: Выбор компьютера на основе последнего выбора пользователя.
 - Тип: Позитивный
 - Тип теста: Блочный
 - Ввод: 'rock', 'rock' (последовательно), затем 'paper', 'paper', 'paper' (последовательно), затем 'scissors', 'scissors', 'scissors' (последовательно)
 - Ожидаемый результат: computer_choice равен 'paper', 'scissors', 'rock' соответственно.

Тест Б4
 - Тест проверяет: Начальные значения статистики.
 - Тип: Позитивный
 - Тип теста: Блочный
 - Ввод: -
 - Ожидаемый результат: games_played, user_wins, computer_wins равны 0.

Тест И1
 - Тест проверяет: Определение победителя на основе ходов.
 - Тип: Позитивный
 - Тип теста: Интеграционный
 - Ввод: 'rock' и 'scissors', 'scissors' и 'rock', 'paper' и 'paper'
 - Ожидаемый результат: Результат - 'user', 'computer', 'draw' соответственно.

Тест И2
 - Тест проверяет: Обновление счетов после раунда.
 - Тип: Позитивный
 - Тип теста: Интеграционный
 - Ввод: 'user' и 'computer'
 - Ожидаемый результат: user_score равен 1, computer_score равен 1.

Тест И3
 - Тест проверяет: Завершение игры при достижении 8 очков.
 - Тип: Позитивный
 - Тип теста: Интеграционный
 - Ввод: Установка user_score в 8
 - Ожидаемый результат: is_game_over() возвращает True.

Тест И2
 - Тест проверяет: Сброс статистики.
 - Тип: Позитивный
 - Тип теста: Интеграционный
 - Ввод: Запись игры с результатом 'user', затем сброс статистики
 - Ожидаемый результат: games_played, user_wins, computer_wins равны 0.

Тест И3
 - Тест проверяет: Выбор компьютера, когда нет предыдущих выборов.
 - Тип: Позитивный
 - Тип теста: Интеграционный
 - Ввод: -
 - Ожидаемый результат: computer_choice входит в список доступных ходов.

Тест И4
 - Тест проверяет: Запись статистики игр.
 - Тип: Позитивный
 - Тип теста: Интеграционный
 - Ввод: Запись игр с результатами 'user', 'computer', 'user'
 - Ожидаемый результат: games_played равен 3, user_wins равен 2, computer_wins равен 1.

Тест А1
 - Тест проверяет: Полный процесс игры.
 - Тип: Позитивный
 - Тип теста: Аттестационный
 - Ввод: 'rock', 'paper', 'scissors'
 - Ожидаемый результат: Игра не завершена, пока user_score не равно 8.
