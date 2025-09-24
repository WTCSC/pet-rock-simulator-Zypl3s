name = str(input("Enter pet rock name: "))
stats = {"Health": 10, "Energy": 10, "Happiness": 10, "Hygiene": 10, "Hunger": 10}
        
def game():
    global stats
    
    while True:
        print("\n Options: \n 1. feed \n 2. play \n 3. clean \n 4. rest \n 5. stats \n 6. hosptial \n 7. exit \n")
        
        if stats['Hunger'] == 15:
            print(f"{name} has blown up due to over feeding. womp womp.")
            break
        elif stats['Health'] <= 0:
            print(f"{name} has died due to poor health. womp womp.")
            break
        elif stats['Happiness'] <= 0:
            print(f"{name} has run away due to unhappiness. womp womp.")
            break
        elif stats['Hygiene'] <= 0:
            print(f"{name} has died due to poor hygiene. womp womp.")
            break
        elif stats['Energy'] <= 0:
            print(f"{name} has died due to lack of energy. womp womp.")
            break
        
        command = str(input(f"What would you like to do with {name}? ")).lower()
    
        if command == "feed" or command == "1":
            if int(stats['Hunger']) < 10:
                stats['Hunger'] += 1
                print(f"You fed {name}. Hunger is now {stats['Hunger']}.")
            else:
                print(f"{name} is getting close to blowing up.")
                stats['Hunger'] += 1
                stats['Health'] -= 1
                print(f"{name}'s hunger is now {stats['Hunger']}.")
                print(f"{name}'s health is now {stats['Health']}.")
        elif command == "play" or command == "2":
            if int(stats['Happiness']) < 10:
                stats['Happiness'] += 1
                stats['Energy'] -= 1
                print(f"You played with {name}. Happiness is now {stats['Happiness']}, Energy is now {stats['Energy']}.")
            else:
                print(f"{name} is getting angry.")
                stats['Happiness'] -= 1
                stats['Energy'] -= 1
                print(f"{name}'s happiness is now {stats['Happiness']}, Energy is now {stats['Energy']}.")
        elif command == "clean" or command == "3":
            if int(stats['Hygiene']) < 10:
                stats['Hygiene'] += 1
                print(f"You cleaned {name}. Hygiene is now {stats['Hygiene']}.")
            else:
                print(f"{name} is already clean, and is now missing skin becuase you scrubbed too hard.")
                stats['Hygiene'] -= 1
                stats['Health'] -= 1
                print(f"{name}'s hygiene is now {stats['Hygiene']}, Health is now {stats['Health']}.")
        elif command == "rest" or command == "4":
            if int(stats['Energy']) < 10:
                stats['Energy'] += 1
                print(f"{name} is resting. Energy is now {stats['Energy']}.")
            else:
                print(f"{name} is already fully rested and is now bored.")
                stats['Energy'] -= 1
                stats['Happiness'] -= 1
                print(f"{name}'s energy is now {stats['Energy']}, Happiness is now {stats['Happiness']}.")
        elif command == "stats" or command == "5":
            print(f"\n {name}'s Stats: \n Health: {stats['Health']} \n Energy: {stats['Energy']} \n Happiness: {stats['Happiness']} \n Hygiene: {stats['Hygiene']} \n Hunger: {stats['Hunger']} \n")
        elif command == "hospital" or command == "6":
            if stats['Health'] < 10:
                stats['Health'] = 10
                print(f"{name} has been healed to full health.")
            else:
                print(f"{name} is getting many contagious diseases.")
                stats['Health'] -= 1
                stats['Hygiene'] -= 1
                print(f"{name}'s health is now {stats['Health']}, Hygiene is now {stats['Hygiene']}.")
        elif command == "exit" or command == "7":
            print("Exiting the game.")
            break
      
    print(f"Your final stats were: {stats}")
    again = input("Would you like to play again? (yes/no): ").lower()
    if again == "yes":
        print("Restarting the game...")
        stats = {"Health": 10, "Energy": 10, "Happiness": 10, "Hygiene": 10, "Hunger": 10}
        game()
    elif again == "no":
        print("Thanks for playing!")
        exit()
    else:
        print("Invalid input. Exiting the game.")
        exit()
    
game()