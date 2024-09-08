class Forest(object):
    def __init__(self) -> None:
        self.inventory = {
            1: "A flashlight",
            2: "A camera",
            3: "A crowbar"
        }

    def show_messages(self):  # Welcome messages
        messages = [
            "\n\tWelcome to the Forest map",
            "You must navigate through this forest",
            "Find more about the cult revolving in the forest\n\t"
        ]
        
        for message in messages:
            print(message)

    def display_inventory(self):
        print("Your inventory contains:")
        for item in self.inventory.values():
            print(item)
            
    def display_choices(self):
        print("""
        You're entering into the forest,
        \tYou see a small shed.\n
        """)
    
        choices = {
            1: "Go in the shed.",
            2: "Keep walking."
        }
    
        for key, value in choices.items():
            print(f"{key}: {value}")
    
        while True:
            try:
                choice = int(input("> "))
                if choice in choices:
                    break
                else:
                    print("Choose a valid option.")
            except ValueError:
                print("Invalid choice. Please choose again.")
    
        if choice == 1:
            print("You see a stash of weapons, you've acquired:")
            self.display_inventory()
        elif choice == 2:
            self.core_gameplay()
            
    def core_gameplay(self):
        print("You see a dark symbol on a tree.")
        print("What would you do?")
        print("1. Investigate the symbol.")
        print("2. Keep moving through the forest.")
         
        choice = input("> ")
         
        if choice == "1":
            self.cult_scene()
        elif choice == "2":
            self.ending_scene()
        else:
            print("Invalid choice. Please try again.")
            self.core_gameplay()
             
    def cult_scene(self):
        print("You approach the dark symbol and feel a strange energy...")
        print("You feel someone approaching towards you.")
        print("1.See who they are.")
        print("2.Hide from them.")
        
        choice = input("> ")
        
        if choice == "1":
            print("The cult members slashed your throat.")
        elif choice == "2":
            print("You see a road to the highway...")
        else :
            self.cult_scene()
            
        
            
        
        
    def ending_scene(self):
        print("You decide to keep moving; the forest feels eerie...")
        print("You hear someone screaming.")
        print("1. Get out of there.")
        print("2. Investigate the scream.")
        print("3. Cover your ears and run.")
    
        choice = input("> ")
    
        if choice == "1":
            print("You run away but bump into a cult member. You were killed.")
        elif choice == "2":
            print("You move cautiously towards the scream, only to find a mysterious figure...")
            print("They plead for help, but are they a trap?")
        # Call a function to decide the next action
            self.decide_help_or_run()
        elif choice == "4":
            print("Ignoring the scream, you push through the trees and escape the forest.")
            print("You find yourself back at the road, but the cult is close behind!")
        # Call a function to escape
            self.escape_from_cult()
        else:
            print("Invalid choice, try again.")
            self.ending_scene()