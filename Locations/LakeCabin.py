
import random


class LakeCabin(object):
    def __init__(self) -> None:
        self.inventory = {
            1: "A knife",
            2: "A flare gun",
            3: "A lighter"  
        }
        
        self.deathMessages = [
        "The world is unfair.",
        "Maybe next  time  use some brains!",
        "Admit it YOU'RE WEAK!",
        "Do you still believe in Santa?"
    ]
  
    # Welcome messages
    def show_messages(self):
        messages = [
            "\n\tYou are now at the lake side cabin",
            "Find the map of the cabin",
            "There seems to have trolls here; find more about them\n\t"
        ]
        
        for message in messages:
            print(message)
      
    def display_inventory(self):
        for item in self.inventory.values():
            print(item)
      
    def display_choices(self):
        print("""
        You're entering into the cabin,
        \tYou see something on the table.\n
        """)
        
        choices = {
            1: "See if there is something.",
            2: "Or enter to the next room."
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
            print("You see a weapons stash, you've acquired:")
            self.display_inventory()
            self.core_gameplay()
        elif choice == 2:
            print("You were eaten by a giant mouse")
            self.show_death_messages()
            
            
    def core_gameplay(self):
        print("\tYou see a giant woman cooking.\n")
        print("What would you do?")
        print("1. Get close to her.")
        print("2. Move through the hallway.")
         
        choice = input("> ")
         
        if choice == "1":
            self.trolls_scene()
            self.use_inventory()
        elif choice == "2":
            self.ending_scene()
        else:
            self.core_gameplay()
             
    def trolls_scene(self):
        print("\tYou approach the giant woman cautiously...\n")
        print("1.Distract her.")
        print("2.Confront her.")
        
        choice = input("> ")
        
        if choice == "1":
            print("How would you distract her?")
            self.use_inventory()
        elif choice == "2":
            print("She ate you.")
            self.show_death_messages()
        else:
            self.trolls_scene()
        
    def ending_scene(self):
        print("\tYou decide to keep moving though the hallway...\n")
        print("A giant troll is aproaching towards you.")
        print("1. Get out of the way.")
        print("2.Ask the troll for help.")
    
        choice = input("> ")
    
        if choice == "1":
            print("You found the way to the basement.")
        elif choice == "2":
            print("The troll ate you...")
            self.show_death_messages()
        else:
            print("Invalid choice, try again.")
            self.ending_scene()
            
    def use_inventory(self):
        print("\nWhich item do you want to use?")
        print("knife,  flare gun or lighter?")
        
        choice = input("> ").lower()
        
        if choice == "knife":
            print("The trolls ate you")
        elif choice == "flare gun":
            print("You scared the trolls.")
        elif choice == "lighter":
            print("They put you into their stew.")
        else:
            self.use_inventory()
            
    def show_death_messages(self):
        print(random.choice(self.deathMessages))
        

   