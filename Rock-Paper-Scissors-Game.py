import random

choices = {
    '1': 'Sang',
    '2': 'Kaghaz',
    '3': 'Gheichi'
}

while True:
    user_operator = input("Please enter your operator (1:Sang, 2:Kaghaz, 3:Gheichi, 4:Exit): ")

    if user_operator == '4':
        print("The game is end, Thank you")
        break

    if user_operator not in choices:
        print("Please enter your choice from the list -> 1:Sang, 2:Kaghaz, 3:Gheichi, 4:Exit")
        continue

    user_choice = choices[user_operator]
    ai_choice = random.choice(list(choices.values()))

    print(f"Your choice: {user_choice}")
    print(f"AI choice: {ai_choice}")

    if user_choice == ai_choice:
        print("Equal")
    elif (
        (user_choice == 'Sang' and ai_choice == 'Gheichi') or
        (user_choice == 'Kaghaz' and ai_choice == 'Sang') or
        (user_choice == 'Gheichi' and ai_choice == 'Kaghaz')
    ):
        print("You win")
    else:
        print("You lost")