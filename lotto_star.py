import random


def lotto_star():
    print("🎰 Welcome to Lotto Star! 🎰")
    print("Insert R5 to play.")

    # User must insert exactly R5
    coin = int(input("Enter amount: "))

    if coin != 5:
        print("❌ Invalid amount! You must insert exactly R5.")
        return  # Stop the game if the amount is wrong

    print("\n✅ You inserted R5. Let's play!\n")

    # User selects 5 numbers between 1 and 50
    user_numbers = []
    print("Enter 5 unique numbers between 1 and 50:")

    while len(user_numbers) < 5:
        try:
            num = int(input(f"Enter number {len(user_numbers) + 1}: "))
            if 1 <= num <= 50 and num not in user_numbers:
                user_numbers.append(num)  # Add valid number to the list
            else:
                print("❌ Invalid number! Enter a unique number between 1 and 50.")
        except ValueError:
            print("❌ Invalid input! Please enter a number.")

    # Generate 5 random winning numbers
    winning_numbers = [random.randint(1, 50) for _ in range(5)]

    print("\n🎟 Your numbers:", user_numbers)
    print("🎯 Winning numbers:", winning_numbers)

    # Check for matches
    matches = set(user_numbers) & set(winning_numbers)

    if matches:
        print(f"\n🎉 Congratulations! You matched {len(matches)} numbers: {matches}")
    else:
        print("\n❌ Sorry, no matches. Better luck next time!")

    # Ask if the user wants to try again
    play_again = input("\nDo you want to play again? (yes/no): ").lower()
    if play_again == "yes":
        print("\nRestarting game...\n")
        lotto_star()  # Restart the game
    else:
        print("\nThanks for playing Lotto Star! Goodbye! 🎲")


# Run the Lotto game
lotto_star()
