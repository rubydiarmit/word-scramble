while True:
    print('Welcome to the Word Scrambler!')
    print("This program will allow you to do many different things with different words! Here's what you can do:")
    print("You can choose to translate a word to PIG LATIN, where the first letter will be moved to the end and add 'ay' to the end.")
    print("You can choose to FLIP a word to make it backwards.")
    print("You can choose to SCRAMBLE a 5 letter word, and mix all of the letters around.")
    print("")
    print("")
    user_input = input("What would you like to do? Pig Latin, Flip, or Scramble: ")

    if user_input == "Pig Latin" or user_input == "pig latin" or user_input == "PIG LATIN":
        pyg = 'ay'
        original = input('Enter a word: ')
        if len(original) and original.isalpha() > 0:
            word = original.lower()
            first = word[0]
            new_word = word[1:len(word)] + first + pyg
            print(new_word)
        else:
            print('Cannot Work. Try Again')
    if user_input == "Flip" or user_input == "flip" or user_input == "FLIP":
        while True:
                def reverse(string):
                    return string[::-1]
                print(reverse(str(input("Enter a word: "))))
                break
    if user_input == "Scramble" or user_input == "scramble" or user_input == "SCRAMBLE":
        wrd = input("Enter a 5 letter word: ")
        print(wrd[4], wrd[2], wrd[0], wrd[3], wrd[1])
    print("")
    print("")
    print("")
    userinput = input("Would you like to play again? Y/N: ")
    if userinput == "Y" or userinput == "y":
        continue
    else:
        break
