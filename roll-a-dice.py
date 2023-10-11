import random
response = "y"
while response == "y":
    # Generate a random number between 1 and 6 for simulating a dice roll
    no = random.randint(1, 6)

    # Represent the dice with print statements
    print("---------")
    print(f"|       |")
    print(f"|   {no}   |")
    print(f"|       |")
    print("---------")

    response = input("Please enter 'y' to continue or 'n' to exit.")  # Prompt the user to continue

print("Stopped! Goodbye!")   