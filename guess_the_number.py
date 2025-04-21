import random

def guess_the_number():
    number_to_guess = random.randint(1, 100)
    attempts = 0
    guessed = False

    print("Добро пожаловать в игру 'Угадай число'!")
    print("Я загадал число от 1 до 100. Попробуй угадать его!")

    while not guessed:
        try:
            player_guess = int(input("Введите ваше предположение: "))
            attempts += 1
            
            if player_guess < number_to_guess:
                print("Слишком мало! Попробуйте еще раз.")
            elif player_guess > number_to_guess:
                print("Слишком много! Попробуйте еще раз.")
            else:
                guessed = True
                print(f"Поздравляю! Вы угадали число {number_to_guess} за {attempts} попыток.")
        except ValueError:
            print("Пожалуйста, введите корректное число.")

if __name__ == "__main__":
    guess_the_number()
