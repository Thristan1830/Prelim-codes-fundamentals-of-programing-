import random

def play_game():
    colors = ['Red', 'White', 'Blue']
    choice_map = {'R': 'Red', 'W': 'White', 'B': 'Blue'}
    gcash = 1000

    print(" Welcome to the Color Match Game!")
    print("You start with ₱1000 Gcash.")
    print("If you WIN: You earn double your bet.")
    print("If you LOSE: You lose your bet.\n")
    
    while gcash > 0:
        print(f"\n Current Gcash: ₱{gcash}")
        
        # Get the bet amount
        while True:
            try:
                bet = int(input("Enter your bet amount: ₱"))
                if bet <= 0:
                    print(" Bet must be more than 0.")
                elif bet > gcash:
                    print(" You don't have enough Gcash for that bet.")
                else:
                    break
            except ValueError:
                print(" Please enter a valid number.")

        # Get user color choice
        print("\n Choose a color:")
        print("R - Red\nW - White\nB - Blue\nQ - Quit")
        choice = input("Your choice: ").strip().upper()

        if choice == 'Q':
            print(" Goodbye!")
            break

        if choice not in choice_map:
            print(" Invalid choice.")
            continue

        user_color = choice_map[choice]
        comp_color = random.choice(colors)
        print(f" Computer chose: {comp_color}")

        if user_color == comp_color:
            gcash += bet
            print(f" YOU WIN! You earned ₱{bet}. New Gcash: ₱{gcash}")

        else:
            gcash -= bet
            print(f" You lose ₱{bet}. New Gcash: ₱{gcash}")

        if gcash <= 0:
            print(" You're out of Gcash! Game over.")
            break

        again = input("Play again? (Y/N): ").strip().upper()
        if again != 'Y':
            print(f" Thanks for playing! Final Gcash: ₱{gcash}")
            break

play_game()
