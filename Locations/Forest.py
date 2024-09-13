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
            print("You see a stash of weapons.")
            self.display_inventory()
            self.core_gameplay()
        elif choice == 2:
            print("")
            
    def core_gameplay(self):
        print("\tYou see a dark symbol on a tree.\n")
        print("What would you do?")
        print("1. Investigate the symbol.")
        print("2. Keep moving through the forest.")
         
        choice = input("> ")
         
        if choice == "1":
            self.cult_scene()
            self.use_inventory()
        elif choice == "2":
            self.ending_scene()
        else:
            print("Invalid choice. Please try again.")
            self.core_gameplay()
             
    def cult_scene(self):
        print("\tYou approach the dark symbol and feel a strange energy...")
        print("You feel someone approaching towards you.")
        print("1.See who they are.")
        print("2.Hide from them.")
        
        choice = input("> ")
        
        if choice == "1":
            print("The cult members are approaching towards you.")
        elif choice == "2":
            print("You see a road to the highway...")
        else :
            self.cult_scene()
            
        
            
    def ending_scene(self):
        print("\tYou decide to keep moving; the forest feels eerie...\n")
        print("You hear someone screaming.")
        print("1. Get out of there.")
        print("2. Investigate the scream.")
       
        choice = input("> ")
    
        if choice == "1":
            print("You run away but bump into a cult member. You were killed.")
        elif choice == "2":
            print("You move cautiously towards the scream, only to find a mysterious figure...")
            print("They plead for help, but are they a trap?")
        else:
            print("Invalid choice, try again.")
            self.ending_scene()
            
    def use_inventory(self):
        print("\nWhich item do you want to use?")
        print("flashlight ,  camera or crowbar?")
        
        choice = input("> ").lower()
        
        if choice == "flashlight":
            print("You've scared the cult members , they ran away.")
        elif choice == "camera":
            print("You were killed by the cult members")
        elif choice == "crwobar":
            print("The cult members slashed your throat.")
        else:
            self.use_inventory()