import random

# 1. Setup lookup tables (Dictionaries)
youDict = {"s": 1, "w": -1, "g": 0}
reverseDict = {1: "Snake", -1: "Water", 0: "Gun"}

# 2. Computer makes a random choice (1, -1, or 0)
computer = random.choice([1, -1, 0])

# 3. Get user input and convert to lowercase
youstr = input("Enter your choice (s for Snake, w for Water, g for Gun): ").strip().lower()

# 4. Check if the user input exists in our dictionary
if youstr not in youDict:
    print("Invalid input! Please enter only 's', 'w', or 'g'.")
else:
    # Get the number corresponding to user's choice
    you = youDict[youstr]

    # Show what both players picked using reverseDict
    print(f"\nYou chose: {reverseDict[you]}")
    print(f"Computer chose: {reverseDict[computer]}")

    # 5. Determine the winner
    if computer == you:
        print("It's a Draw!")
    elif (you == 1 and computer == -1) or (you == -1 and computer == 0) or (you == 0 and computer == 1):
        print("You win!")
    else:
        print("You lose!")