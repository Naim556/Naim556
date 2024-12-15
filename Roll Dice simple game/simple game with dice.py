import random

def roll_dice():
    """Rolls three dice and returns their values as a list."""
    return [random.randint(1, 6) for _ in range(3)]

def play_game(budget):
    """Main function to handle the game loop."""
    while budget > 0:
        print(f"\nYour current budget: ${budget:.2f}")
        continue_game = input("Do you want to play the game? [Y|N]: ").strip().capitalize()

        if continue_game == "N":
            print(f"Thank you for playing! Final Budget: ${budget:.2f}")
            break
        elif continue_game == "Y":
            try:
                choice = int(input("Please select a number between 1 and 6: "))
                if choice < 1 or choice > 6:
                    raise ValueError("Choice must be between 1 and 6.")

                expense = float(input("How much do you want to play: "))
                if expense <= 0 or expense > budget:
                    raise ValueError("Expense must be a positive number within your budget.")
            except ValueError as e:
                print(e)
                continue

            budget = tas(budget, choice, expense)
        else:
            print("Invalid input. Please enter 'Y' or 'N'.")

    if budget <= 0:
        print("Game over! You ran out of money.")

def tas(budget, choice, expense):
    """Handles the dice roll and updates the budget based on the result."""
    faces = roll_dice()
    print(f"\nDice Rolls: {faces}")

    matches = faces.count(choice)
    if matches == 3:
        winnings = expense * 3
        budget += winnings - expense
        print(f"Jackpot! You matched all three dice. You won ${winnings:.2f}.")
    elif matches == 2:
        winnings = expense * 2
        budget += winnings - expense
        print(f"Great! You matched two dice. You won ${winnings:.2f}.")
    elif matches == 1:
        winnings = expense
        budget += winnings - expense
        print(f"Good! You matched one die. You won back your expense.")
    else:
        budget -= expense
        print(f"Unlucky! No matches. You lost ${expense:.2f}.")

    return budget

if __name__ == "__main__":
    print("Hello! Welcome to the dice game.")
    try:
        initial_budget = float(input("Please enter your initial budget in dollars: "))
        if initial_budget <= 0:
            raise ValueError("You need a positive budget to play.")
        play_game(initial_budget)
    except ValueError as e:
        print(e)
