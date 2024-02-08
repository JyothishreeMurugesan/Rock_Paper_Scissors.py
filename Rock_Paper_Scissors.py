import random

def get_user_choice():
    user_choice = input("Enter rock, paper, or scissors: ").lower()
    while user_choice not in ['rock', 'paper', 'scissors']:
        print("Invalid choice. Please enter rock, paperrock, or scissors.")
        user_choice = input("Enter rock, paper, or scissors: ").lower()
    return user_choice

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user_choice, computer_choice):
    print(f"You chose {user_choice}.")
    print(f"Computer chose {computer_choice}.")

    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        print("You win!")
    else:
        print("You lose!")

if __name__ == "__main__":
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        determine_winner(user_choice, computer_choice)

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            break
    print("Thanks for playing")
