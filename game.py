def start_game():
    print("Welcome to the Adventure Game!")
    print("You find yourself in a dark forest. Do you go left or right?")
    choice = input("Type 'left' or 'right': ")
    
    if choice == "left":
        print("You encounter a bear! Quick, do you run, play dead, or climb a tree?")
        action = input("Type 'run', 'play dead', or 'climb': ")
        
        if action == "run":
            print("You escape the bear and find a treasure chest. You win!")
        elif action == "play dead":
            print("The bear sniffs you and walks away. You're safe, but no treasure.")
        elif action == "climb":
            print("You climb a tree, but the bear knocks it over. Game over!")
        else:
            print("Invalid choice. The bear attacks. Game over!")
    elif choice == "right":
        print("You come across a river. Do you swim across or look for a bridge?")
        action = input("Type 'swim' or 'bridge': ")
        
        if action == "swim":
            print("You swim across successfully and find a magical potion. You win!")
        elif action == "bridge":
            print("You find a bridge guarded by trolls. Do you fight or bribe them?")
            troll_action = input("Type 'fight' or 'bribe': ")
            
            if troll_action == "fight":
                print("You defeat the trolls and cross the bridge. You find hidden treasure. You win!")
            elif troll_action == "bribe":
                print("You give the trolls some gold and cross the bridge. You find a cave. Game over!")
            else:
                print("Invalid choice. The trolls attack. Game over!")
        else:
            print("Invalid choice. You're swept away by the river. Game over!")
    else:
        print("Invalid choice. You're lost in the forest. Game over!")

if __name__ == "__main__":
    start_game()
