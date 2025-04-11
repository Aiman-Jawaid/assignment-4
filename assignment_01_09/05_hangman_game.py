import random

def hangman():
    
    word_list = ['python', 'java', 'javascript', 'hangman', 'computer', 'programming']
    
   
    chosen_word = random.choice(word_list)
    

    word_display = ['_'] * len(chosen_word)
    
    attempts = 6 
    guessed_letters = []  
    
    print("Welcome to Hangman!")
    print(f"The word has {len(chosen_word)} letters.")
    
    while attempts > 0:
        print(f"\nCurrent word: {' '.join(word_display)}")
        print(f"Attempts left: {attempts}")
        print(f"Guessed letters: {', '.join(guessed_letters)}")
        
        
        guess = input("Guess a letter: ").lower()
        
       
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue
        
        if guess in guessed_letters:
            print(f"You already guessed the letter '{guess}'. Try again.")
            continue
        
        guessed_letters.append(guess)
        

        if guess in chosen_word:
            print(f"Good guess! '{guess}' is in the word.")
            
            for i in range(len(chosen_word)):
                if chosen_word[i] == guess:
                    word_display[i] = guess
        else:
            attempts -= 1
            print(f"Oops! '{guess}' is not in the word.")
        

        if '_' not in word_display:
            print("\nCongratulations, you guessed the word!")
            break
    
    if attempts == 0:
        print(f"\nSorry, you lost! The word was '{chosen_word}'.")


hangman()
