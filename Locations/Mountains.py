
import random

class Mountains(object):
    def __init__(self) -> None:
        self.inventory = {
            1: "Woolen gloves",
            2: "A lantern",
            3: "An adrenaline injection"
        }
        
        self.deathMessages = [
        "The world is unfair.",
        "Maybe next time  use some brains!",
        "Admit it YOU'RE WEAK!",
        "Do you still believe in Santa?"
    ]
  
    # Welcome messages
    def show_messages(self):
        messages = [
            "\n\tYou are now at the mountains.",
            "You must find the mines.",
            "Find more about the bear and kill it.\n\t"
        ]
        
        for message in messages:
            print(message)
      
    def display_inventory(self):
        print("Your inventory contains:")
        for item in self.inventory.values():
            print(item)
      
    def display_choices(self):
        print("""
        You're entering into a cave,
        \tYou see a fireplace.\n
        """)
    
        choices = {
            1: "Check the fireplace.",
            2: "Keep walking into the cave."
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
            self.core_gameplay()
        elif choice == 2:
            print("A big stone fell onto  your head , you're dead.")
            self.show_death_messages()
            
            
    def core_gameplay(self):
        print("You see a big grizzly bear eating a fish.")
        print("What would you do?")
        print("1. Attack the bear.")
        print("2. Keep moving through the cave.")
         
        choice = input("> ")
         
        if choice == "1":
            self.bear_scene()
            self.use_inventory()
        elif choice == "2":
            self.ending_scene()
        else:
            print("Invalid choice. Please try again.")
            self.core_gameplay()
             
    def bear_scene(self):
        print("You're approaching the bear...")
        print("1.Kill the bear.")
        print("2.Distract the bear.")
        
        choice = input("> ")
        
        if choice == "1":
            self.use_inventory()
        elif choice == "2":
            print("The bear tore you apart.")
            self.show_death_messages()
        
        
    def ending_scene(self):
        print("You decide to keep moving though the cave...")
        print("You saw soemthing glowing.")
        print("1.Check what is it.")
        print("2.Continue your way to exit.")
        
        choice = input("> ")
    
        if choice == "1":
            print("You found the key to the mines.")
        elif choice == "2":
            print("You saw the bear...")
            print("You have to climb though another way out?")
            self.exit_climb()
        else:
            print("Invalid choice, try again.")
            self.ending_scene()
            
    def exit_climb(self):
        print("You start climbing to find a way out of the cave...")
        print("1. Look for handholds.")
        print("2. Climb quickly to escape the bear.")
        
        choice = input("> ")
        
        if choice == "1":
            print("You found a safe route and escaped successfully!")
            print("You made it out of the cave and are safe!")
        elif choice == "2":
            print("You climbed too fast and lost your grip!")
            print("You fell into the bear's den...")
            self.show_death_messages()
        else:
            self.exit_climb()
            
            
    def use_inventory(self):
        print("\nWhich item do you want to use?\n")
        print("Woolen gloves,  lantern or  adrenaline injection")
        
        choice = input("> ").lower()
        
        if choice == "woolen gloves":
            print("")
        elif choice == "lantern":
            print("You scared the bear.")
        elif choice == "adrenaline injection":
            print("")
        else:
            self.use_inventory()
            
    def show_death_messages(self):
        print(random.choice(self.deathMessages))
        