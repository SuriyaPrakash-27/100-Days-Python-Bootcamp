import random
import Hangman_words
import Hangman_art
print(Hangman_art.logo)

chosen_word = Hangman_words.wordlist[random.randint(0, len(Hangman_words.wordlist) - 1)] # or chosen_word = random.choice(Hangman_words.wordlist)
list1 = list(chosen_word)
b = len(chosen_word)

answer = ''
for n in range(0, b):
    answer+='_'
answer = list(answer)

life = 7


while not answer == chosen_word or life == 0:
    print(''.join(answer))
    player_input = input("Enter a letter: ").lower()
    count1 = 0

    if player_input in answer:
        print(f"You have already guessed the letter: {player_input}")
    else:
        count = 0
        for n in range(0, b):
            if player_input == list1[n]:
                answer[n] = player_input
                count += 1
        if count == 0:
            print(f"You guessed {player_input}, that's not in the word. You lose a life.")
            life-=1
            if life == 6:
                print(Hangman_art.hangman_stages[0])
            elif life == 5:
                print(Hangman_art.hangman_stages[1])
            elif life == 4:
                print(Hangman_art.hangman_stages[2])
            elif life == 3:
                print(Hangman_art.hangman_stages[3])
            elif life == 2:
                print(Hangman_art.hangman_stages[4])
            elif life == 1:
                print(Hangman_art.hangman_stages[5])
            else:
                print(Hangman_art.hangman_stages[6])
                print("Game Over! You Lose.")
                break

    if answer == list1:
        print(''.join(answer))
        print("You Won!")
        break

