hang_word = "ab"
list_word = list(hang_word)
start_list = ""
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
guessed_letters = []
lives = 6

for i in hang_word:
    start_list+= "_"

play_list = list(start_list)

while True:
    invalid = True
    while invalid:
        if guessed_letters:
            print(f"Your guessed letters are: {guessed_letters}")
        guess = input("Please guess a letter:\n")
        correct = 0
        if guess == "exit":
            break
        elif guess in letters and guess not in guessed_letters:
            invalid = False
        else:
            invalid = True
    
    guessed_letters.append(guess)
    if guess == "exit":
        break
    else:
        for index, item in enumerate(list_word):
            if item == guess:
                play_list[index] = guess
                correct += 1
        if correct > 0:
            print(f"A correct choice. Your friend has {lives} lives left")
            correct = 0
        elif correct == 0:
            lives -= 1
            print(f"An incorrect choice. Your friend has {lives} lives left")
        print("".join(play_list))
    if "_" not in play_list:
        print("epic")
        break
    elif lives == 0:
        print("murderer")
        break
    else:
        continue