
import random
import os
import time

RESET = "\033[0m"
GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
CYAN = "\033[96m"


CATEGORIES = {
    "Animals": [
        "tiger",
        "rabbit",
        "giraffe",
        "elephant",
        "zebra"
    ],
    "Fruits": [
        "apple",
        "banana",
        "orange",
        "mango",
        "grapes"
    ],
    "Countries": [
        "india",
        "canada",
        "brazil",
        "japan",
        "france"
    ],
    "Technology": [
        "python",
        "analytics",
        "cloud",
        "java",
        "database"
    ]
}

HIGH_SCORE_FILE = "highscore.txt"



def clear_screen():
    """Clear terminal screen."""
    os.system("cls" if os.name == "nt" else "clear")


def pause(seconds=1):
    """Pause briefly."""
    time.sleep(seconds)


def load_high_score():
    """Load high score from file."""
    try:
        with open(HIGH_SCORE_FILE, "r") as file:
            return int(file.read())
    except:
        return 0


def save_high_score(score):
    """Save high score."""
    with open(HIGH_SCORE_FILE, "w") as file:
        file.write(str(score))



def show_title():
    clear_screen()
    print(CYAN + "=========================" + RESET)
    print("        HANGMAN")
    print(CYAN + "=========================" + RESET)
    print()


def show_menu():
    print("1. Play Game")
    print("2. View High Score")
    print("3. How To Play")
    print("4. Quit")
    print()


def show_instructions():
    clear_screen()

    print("HOW TO PLAY")
    print("-------------------------")
    print("Guess the hidden word")
    print("one letter at a time.")
    print()
    print("You can make only")
    print("6 incorrect guesses.")
    print()

    input("Press Enter to return...")


def show_high_score():
    clear_screen()

    score = load_high_score()

    print("HIGH SCORE")
    print("-------------------------")
    print("Best Score:", score)
    print()

    input("Press Enter to return...")


def choose_category():
    clear_screen()

    category_names = list(CATEGORIES.keys())

    print("Choose Category")
    print("-------------------------")

    for i in range(len(category_names)):
        print(f"{i + 1}. {category_names[i]}")

    print()

    while True:
        choice = input("Enter choice: ")

        if choice.isdigit():
            choice = int(choice)

            if 1 <= choice <= len(category_names):
                return category_names[choice - 1]

        print(RED + "Invalid choice." + RESET)




def play_game():
    score = 0

    while True:

        category = choose_category()

        word = random.choice(CATEGORIES[category])

        guessed_letters = []
        wrong_letters = []

        wrong_guesses = 0
        max_wrong = 6

    

        while wrong_guesses < max_wrong:

            clear_screen()

            print("Category:", category)
            print("-------------------------")

            # Display word progress
            display_word = ""

            for letter in word:
                if letter in guessed_letters:
                    display_word += letter + " "
                else:
                    display_word += "_ "

            print("Word:", display_word)
            print()

            print("Wrong guesses left:",
                  max_wrong - wrong_guesses)

            print("Wrong letters:",
                  " ".join(wrong_letters))

            print("Score:", score)
            print()

            if "_" not in display_word:

                print(GREEN + "You won!" + RESET)

                points = len(word) * 10
                score += points

                print("Points earned:", points)

                high_score = load_high_score()

                if score > high_score:
                    save_high_score(score)
                    print(GREEN + "New High Score!" + RESET)

                break

            # Get input
            guess = input("\nEnter a letter: ").lower().strip()

            # Input validation
            if len(guess) != 1:
                print(RED + "Enter one letter only." + RESET)
                pause(1)
                continue

            if not guess.isalpha():
                print(RED + "Letters only." + RESET)
                pause(1)
                continue

            if guess in guessed_letters or guess in wrong_letters:
                print(YELLOW + "Already guessed." + RESET)
                pause(1)
                continue

            # Correct guess
            if guess in word:
                guessed_letters.append(guess)
                print(GREEN + "Correct!" + RESET)
                pause(1)

            # Wrong guess
            else:
                wrong_letters.append(guess)
                wrong_guesses += 1

                print(RED + "Wrong guess." + RESET)
                pause(1)

        

        if wrong_guesses >= max_wrong:
            clear_screen()

            print(RED + "You lost." + RESET)
            print("Correct word was:", word)

        else:
            print("Correct word was:", word)

        
        print()

        replay = input("Play again? (y/n): ").lower().strip()

        if replay != "y":
            print("Goodbye!")
            pause(1)
            break



def main():

    while True:

        show_title()
        show_menu()

        choice = input("Enter choice: ")

        if choice == "1":
            play_game()

        elif choice == "2":
            show_high_score()

        elif choice == "3":
            show_instructions()

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print(RED + "Invalid choice." + RESET)
            pause(1)


if __name__ == "__main__":
    main()