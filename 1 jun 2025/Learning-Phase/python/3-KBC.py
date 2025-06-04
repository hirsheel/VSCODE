# An inspired code from @codewithharry KBC exercise

# List of questions, each containing:
# [Question, Option1, Option2, Option3, Option4, CorrectAnswerIndex]
que = [
    ["Who is the main character in the 'Iron Man' movies?", "Tony Stark", "Steve Rogers", "Bruce Wayne", "Clark Kent", 1],
    ["Which video game features the character Mario?", "Minecraft", "Call of Duty", "Super Mario Bros.", "Fortnite", 3],
    ["What is the name of Harry Potter's pet owl?", "Scabbers", "Hedwig", "Fawkes", "Crookshanks", 2],
    ["Which superhero is known as the 'Dark Knight'?", "Iron Man", "Spider-Man", "Batman", "Superman", 3],
    ["Which game popularized the battle royale genre?", "Valorant", "Minecraft", "Overwatch", "PUBG", 4],
    ["What movie is the quote 'I'll be back' from?", "The Terminator", "Die Hard", "Rambo", "Predator", 1],
    ["Which game studio created 'The Legend of Zelda'?", "Ubisoft", "Rockstar Games", "Nintendo", "EA", 3],
    ["In which movie does the character Jack Dawson appear?", "Titanic", "Inception", "The Notebook", "Twilight", 1],
    ["Which series features a floating city called Columbia?", "Half-Life", "Bioshock Infinite", "Mass Effect", "Fallout", 2],
    ["Which Marvel movie was the first to earn over $2 billion?", "Iron Man", "Avengers: Endgame", "Black Panther", "Avengers: Infinity War", 2],
    ["What is the name of the AI in the 'Portal' video game series?", "Cortana", "GLaDOS", "EVA", "Siri", 2],
    ["In 'The Matrix', what color is the pill Neo takes?", "Blue", "Red", "Green", "White", 2],
    ["Who directed 'Pulp Fiction'?", "Steven Spielberg", "Christopher Nolan", "Martin Scorsese", "Quentin Tarantino", 4],
    ["Which game holds the record for highest-grossing media franchise?", "Call of Duty", "FIFA", "Mario", "Pokémon", 4]
]

# Prize money for each question level (increasing order)
lvl = [5000, 10000, 20000, 40000, 80000, 160000, 320000, 640000, 1250000, 2500000, 5000000, 10000000, 30000000, 70000000]

# Safe points where money is guaranteed even if the player loses later
safe = [40000, 320000, 5000000, 70000000]

money_won = 0       # Tracks current winnings
safe_money = 0      # Tracks the last safe milestone reached

# Loop through each question
for i in range(len(que)):
    q = que[i]  # Current question
    
    # Display question and options
    print(f"\nQuestion {i+1} for ₹{lvl[i]:,}")
    print(q[0])  # Question text
    print(f"1. {q[1]}     2. {q[2]}")  # Options 1 & 2
    print(f"3. {q[3]}     4. {q[4]}")  # Options 3 & 4
    
    ans = input("Your answer (1-4) or Q to quit: ").strip().upper()

    # Check if answer is valid (1-4)
    if ans in ("1", "2", "3", "4"):
        ans_num = int(ans)
        if ans_num == q[-1]:  # Check if correct
            print(" Correct!")
            money_won = lvl[i]  # Update winnings
            if money_won in safe:  # Update safe milestone
                safe_money = money_won
        else:
            print(" Wrong answer!")
            break  # End game if wrong
    
    # Allow quitting early
    elif ans == "Q":
        print("Thanks For Playing The Game.")
        # Handle edge case (no questions answered)
        if i < 1:
            print("You haven't won anything, how sad lol..")
        else:
            print(f"You have won ₹{lvl[i-1]:,}")  # Last secured amount
        break
    
    # Invalid input handling
    else:
        print("Invalid input! Exiting.")
        break

# Final output (shows guaranteed safe money)
print(f"\nYou won ₹{safe_money:,} (guaranteed, lol)!")