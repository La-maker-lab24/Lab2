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
- Ввод: user_choice = 'rock' (выбор игрока)
- Ожидаемый результат: Возвращает результат, который может быть 'user', 'computer' или 'draw', и выбор компьютера должен быть одним из ['rock', 'paper', 'scissors'].

Тест Б2
- Тест проверяет: Правильность определения победителя.
- Тип: Позитивный
- Тип теста: Блочный
- Ввод: user_choice = 'rock', computer_choice = 'scissors' (выборы игрока и компьютера)
- Ожидаемый результат: Возвращает 'user' (победитель).

Тест Б3
- Тест проверяет: Корректное обновление счета.
- Тип: Позитивный
- Тип теста: Блочный
- Ввод: result = 'user' и result = 'computer' (результат раунда)
- Ожидаемый результат: Счет игрока увеличивается на 1 при результате 'user', и счет компьютера увеличивается на 1 при результате 'computer'.

Тест А1
- Тест проверяет: Завершение игры при достижении финишного счета.
- Тип: Позитивный
- Тип теста: Аттестационный
- Ввод: user_score = 8 и computer_score = 8 (счет игрока и компьютера)
- Ожидаемый результат: Метод is_game_over() возвращает True, если любой из счетов достигает 8.

Тест А2
- Тест проверяет: Сброс счета игры.
- Тип: Позитивный
- Тип теста: Аттестационный
- Ввод: user_score = 5, computer_score = 3 (счет до сброса)
- Ожидаемый результат: После вызова reset_game(), оба счета должны быть равны 0.

Тест И1
- Тест проверяет: Корректное обновление статистики игры.
- Тип: Позитивный
- Тип теста: Интеграционный
- Ввод: winner = 'user' и winner = 'computer' (результаты игр)
- Ожидаемый результат: Общее количество игр увеличивается на 2, количество побед игрока равно 1, количество побед компьютера равно 1.

Тест И2
- Тест проверяет: Сброс статистики игры.
- Тип: Позитивный
- Тип теста: Интеграционный
- Ввод: После записи одной игры для игрока и одной для компьютера.
- Ожидаемый результат: После вызова reset_statistics(), все счетчики статистики должны быть равны 0.
