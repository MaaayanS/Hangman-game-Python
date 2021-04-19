#Hangman game

#The Boolean function that returns true if all the letters that make up the secret word are included in the list 
#of letters that the user guessed. Otherwise, the function returns a False
def check_win(secret_word, old_letters_guessed):
    hidden_word = ""
    for char in secret_word:
        if char not in old_letters_guessed:
            return False
    return True

#A function that displays the letters the player guessed and the missing places    
def show_hidden_word(secret_word, old_letters_guessed):
    hidden_word = ""
    for char in secret_word:
        if char in old_letters_guessed:
            hidden_word += char + " "
        else:
            hidden_word += "_ "
    print(hidden_word)
    
#func that checks if the input is correct and if they have not guessed this letter before    
def check_valid_input(letter_guessed, old_letters_guessed):
    if len(letter_guessed)>1 :
        return False
    elif not letter_guessed.isalpha():
        return False
    else:
        return not (letter_guessed in old_letters_guessed)
  
#If the character is invalid or the character has been guessed before, the function prints the character X, 
#below it the list of letters that have already been guessed and returns a lie. If the character is correct and 
#has not been guessed before - the function adds the character to the guess list and returns true.  
def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    flag = check_valid_input(letter_guessed, old_letters_guessed)
    
    if flag==True:
        old_letters_guessed += letter_guessed.lower()
        #print(old_letters_guessed)
        return True
    else:
        print("X")
        sorted_list = sorted(old_letters_guessed)
        print_str = ""
        for ch in sorted_list:
            print_str+= ch + " -> "
        print(print_str[:-4])
        return False

#The function returns a word in the position obtained as an argument to the function (index).
def choose_word(file_path, index):
    with open(file_path,'r') as f:
        file_contents = f.read()
        words_list = file_contents.split()
    list_index = (index-1)%len(words_list)
    return words_list[list_index] # -> ?

#Print the front page
def print_front_page():
    print("""
      _    _                                         
     | |  | |                                        
     | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
     |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
     | |  | | (_| | | | | (_| | | | | | | (_| | | | |
     |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                          __/ |                      
                         |___/ \n""")

HANGMAN_PHOTOS = {
"picture 1": """
    x-------x""", 
    "picture 2": """
    x-------x
    |
    |
    |
    |
    |""", 
    "picture 3": """
    x-------x
    |       |
    |       0
    |
    |
    |""", 
    "picture 4": """
    x-------x
    |       |
    |       0
    |       |
    |
    |""", 
    "picture 5": """
    x-------x
    |       |
    |       0
    |      /|\\
    |
    |
    """,
    "picture 6": """
    x-------x
    |       |
    |       0
    |      /|\\
    |      /  
    |""",
    "picture 7": """
    x-------x
    |       |
    |       0
    |      /|\\
    |      / \\
    |""" }

def print_hangman(num_of_tries):
    picture_str = "picture " + str(num_of_tries)
    print(HANGMAN_PHOTOS[picture_str]+"\n")

def main():
    secret_word = "" # This is the word the user needs to guess
    old_letters_guessed = [] # The list holds the letters the player guessed
    MAX_TRIES = 6 # The variable holds the maximum number of failed attempts allowed in the game
    num_of_tries = 1 # The number represents the number of failed attempts by the user
    
    print_front_page()
    
    input_file_path = input("Enter file path: ")
    input_index = input("Enter index: ")
    
    secret_word = choose_word(input_file_path, int(input_index))

    print("Let’s start!")
    print_hangman(num_of_tries)
    show_hidden_word(secret_word, old_letters_guessed)

    while (num_of_tries <= MAX_TRIES) and check_win(secret_word, old_letters_guessed)==False :
        
        letter_guessed = input("Guess a letter: ")
        
        if(try_update_letter_guessed(letter_guessed, old_letters_guessed)):
            if(letter_guessed.lower() not in secret_word):
                print(":(")
                num_of_tries+=1
                print_hangman(num_of_tries)
        
            show_hidden_word(secret_word, old_letters_guessed)
    
    if check_win(secret_word, old_letters_guessed) :
        print("WIN")
    else:
        print("LOSE")    

if __name__ == "__main__":
    main()
    
    
  
   
