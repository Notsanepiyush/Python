
import random, requests

def fetch_words():
    url = "https://random-word-api.herokuapp.com/word"
    querystring = {"number": "10"}  # Adjust the number of words as needed
    response = requests.get(url, params=querystring)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print('Unable to fetch word')
        exit()

def choose_word(words):
    hard_words = [word for word in words if len(word) == 5]    
    return random.choice(hard_words)

def display_word(word, guessed_letters):
    displayed_word = ""
    for letter in word:
        if letter in guessed_letters:
            displayed_word += letter
        else:
            displayed_word += "_"
    return displayed_word

def display_hangman(incorrect_attempts):
    stages = [
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / \\
          ---
        """,
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / 
          ---
        """,
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |      
          ---
        """,
        """
           --------
           |      |
           |      O
           |     \\|
           |      |
           |     
          ---
        """,
        """
           --------
           |      |
           |      O
           |      |
           |      |
           |     
          ---
        """,
        """
           --------
           |      |
           |      O
           |     
           |      
           |     
          ---
        """,
        """
           --------
           |      |
           |      
           |     
           |      
           |     
          ---
        """
    ]
    return stages[incorrect_attempts]

def hangman():
    
    word = choose_word(fetch_words())
    guessed_letters = []
    incorrect_attempts = 0

    print("Welcome to Hangman!")
    print(display_word(word, guessed_letters))
    print(display_hangman(-1))
    score = 0

    while incorrect_attempts < 6:
        guess = input("Guess a letter: ").lower()
        if guess in guessed_letters:
            print("You already guessed that letter!")
        elif guess in word:
            guessed_letters.append(guess)
            print(display_word(word, guessed_letters))
            if "_" not in display_word(word, guessed_letters):
                score += 10
                print("Congratulations! You guessed the word:", word)
                print("Your score:", score)
                break
        else:
            incorrect_attempts += 1
            print("Wrong guess! You have", 6 - incorrect_attempts, "attempts left.")
            print(display_hangman(-incorrect_attempts-1))
            if incorrect_attempts == 6:
                print("Sorry, you lost! The word was:", word)
                break

hangman()
