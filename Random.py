import random 
def play_game():
    colors = ['red','white','blue']
    while True:
        print("\nR - Red\nW - White\nB - Blue\nQ - Quit")
        choice = input("your choice: ").strip().upper()
        if choice == 'Q':
            print("Goodbye!")
            break 

        if choice not in ['R','W','B']:
            print("invalid choice.")
        
        continue
    user_color = {'R:': 'Red' ,'W': 'White','B': 'Blue'}[choice]
    comp_color = random.choice(colors)
    print("computer chose:", comp_color)
    if user_color == comp_color:
        print("YOU WIN")
    else:
        print("you lose.")

        again = input ("play again? (Y/N): ").strip().upper()
        if again != 'Y':
            print("thanks for playing!")
            
        

play_game()

        


