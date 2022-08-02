comp_number = 4
user_lifes = 3
while user_lifes > 0:
    user_lifes -= 1
    user_number = int(input("Введите число: "))
    if user_number == comp_number:
        print("Win!")
        break
    elif user_number > comp_number:
        print("Моё число меньше!")
    elif user_number < comp_number:
        print("Моё число больше!")
else:
    print("Lose!")
print("Game Over")