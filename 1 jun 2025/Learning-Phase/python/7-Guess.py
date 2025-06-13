import random
num = random.randint(1, 100)
print("Welcome to Number Guessing Game!")
print("How to play: A random number is choosed by computer \nbetween 1-100 and hints are given to guess. \nIf You guess it in 10 times, You WIN!")
i = 0
while i <= 10:                                                                   # 10+1(trial) chance loop
    guess = input(f"Enter Your Guess or Q to Quit (chance {i}): ").strip()           
    try:                                                                         # checks if guess is a number
        guess = float(guess)
        if guess <= 100 and guess >= 1:
            if guess < num:
                print("Guess Higher Value...")
            elif guess > num:
                print("Guess Lower...")
            elif guess == num:
                print("THATS THE EXACT NUMBER!")
                print("Congratulations You Won!")
                break
        else:
            print("Guess a number between 1-100 (1 and 100 included)")
    except:                                                                       # Handles if guess isnt a number
        if guess.upper() == "Q":
            print("Thanks for playing")
            break
        else:
            print("Give a Valid Number...")
    i += 1
else:
    print(f"\nGame OVER! The Number was {num} \n Better LucK next Time!")