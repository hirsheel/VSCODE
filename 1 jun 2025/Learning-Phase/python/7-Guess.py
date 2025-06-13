import random 
num = random.randint(1, 100)
print("Welcome to Number Guessing Game!")
print("How to play: A random number is choosed between 1-100 and hints are given to guess. \nIf user Fails to guess it in 15 times, You LOSE!")
i=1
while i <= 15:
    guess = input(f"Enter Your Guess(chance {i}): ")
    try:
        guess = float(guess)
        if guess <= 100 and guess >= 1:
            if guess < num:
                print("Guess Higher Value...")
            elif guess > num:
                print("Guess Lowerer...")
            elif guess == num:
                print("THATS THE EXACT NUMBER!")
                print("Congratulations You Won!")
                break
        else:
            print("Guess a number between 1-100 (1 and 100 included)")
    except:
        if guess.uppper == "Q":
            print("Thanks for playing")
            break
        else:
            print("Give a Valid Number...")
    i += 1