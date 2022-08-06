import hangman_01


#head of the game
HANGMAN_ASCII_ART = hangman_01.game_addline()
MAX_TRIRES = 6
print (HANGMAN_ASCII_ART)

word = hangman_01.word_enter_guess()  #word in the game
i = 0
while i< MAX_TRIRES:
    print("guess the letter: ")
    letter = input()
    if letter in word:
        print("you guessed: " + letter)
    else:
        print("you guessed: " + letter)
        if i==0:
            hangman_01.picture_1()
            i+=1
        elif i==1:
            hangman_01.picture_2()
            i+=1
        elif i==2:
            hangman_01.picture_3()
            i+=1
        elif i==3:
            hangman_01.picture_4()
            i+=1
        elif i==4:
            hangman_01.picture_5()
            i+=1
        elif i==5:
            hangman_01.picture_6()
            i+=1
        elif i==6:
            hangman_01.picture_7()
            print("you lose")
            break
