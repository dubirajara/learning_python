import random

jokenpo = ['rock', 'paper', 'scissors']
random.shuffle(jokenpo)


def select():
    print('\nSelect: "Rock, Paper or Scissors"')
    player = input('> ').lower()
    enemy = random.choice(jokenpo)

    if player in jokenpo:

        if player == enemy:
            print('\nDraw!!!')

        elif player == 'rock' and enemy == 'scissors':
            print(f'\nYou Win, {player} breaks {enemy}')

        elif player == 'paper' and enemy == 'rock':
            print(f'\nYou Win, {player} covers {enemy}')

        elif player == 'scissors' and enemy == 'paper':
            print(f'\nYou Win, {player} cuts {enemy}')

        else:
            print(f'\nYou lose!!! you: {player} and the machine win: {enemy}')

        try_again()

    else:
        select()


def try_again():
    a = input("\nDo you want to keep playing y/n ? ")

    while a.lower() != 'y' and a.lower() != 'n':
        a = input("\nDo you want to keep playing y/n ? ")

    if a.lower() == ("y"):
        select()

    else:
        print("\nGame Over!!!")


if __name__ == "__main__":
    select()