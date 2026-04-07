import random

chances = ["000001", "00001", "0001", "001", "01"]

response = input("Spin the wheel? (y/n)  ").lower()

if response == "n":
    print("Game over. You chose not to take the risk.")
elif response == "y":
    print("Chance of success: 5 of 6")
    print("Spinning...")
    print("FIRE!")

    is_dead = random.choice(chances[0])

    if is_dead == '1':
        print("YOU ARE DEAD!!!")
    else:
        survived_all = True
        for i in range(1, len(chances)):
            print(f"Still alive! Odds are now 1 in {len(chances[i]) + 1}.")
            response = input("Spin again? (y/n)  ").lower()
            
            if response == "n":
                print("You're such a loser. Take some risks")
                survived_all = False
                break
                
            print("Spinning...")
            print("FIRE!")
            is_dead = random.choice(chances[i])
            
            if is_dead == '1':
                print("YOU ARE DEAD!!!")
                survived_all = False
                break

        if survived_all:
            print("Still alive! You are incredibly lucky!")
            print("If you spin again, the odds are almost zero. Spin again? (y/n)")
            response = input().lower()
            
            if response == "n":
                print("Game over. You don't even wanna take risks")
            else:
                print("You really want to push your luck!")
                last_chance = random.randint(1, 500)
                
                if last_chance == 1:
                    print("MECHANICAL ERROR! You are STILL ALIVE!")
                    print("That was a 1/500 chance!")
                    user_guess = input("Guess the secret passcode for a message: ").lower()
                    
                    if user_guess == "popcorn":
                        print("You guessed right!")
                        print("The secret message is: Cat boy likes to run!")
                    else:
                        print("Wrong passcode.")
                else:
                    print("YOU ARE DEAD!!!")