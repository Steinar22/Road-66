class LakeCabin(object):
    def __init__(self) -> None:
        self.inventory = {
            1: "A knife",
            2: "A flare gun",
            3: "A lighter"  # Changed key 2 to 3 for unique keys
        }
  
    # Welcome messages
    def show_messages(self):
        messages = [
            "You are now at the lake side cabin",
            "Find the map of the cabin",
            "There seems to have trolls here; find more about them"
        ]
        
        for message in messages:
            print(message)
      
    def display_inventory(self):
        for item in self.inventory.values():
            print(item)
      
    def display_choices(self):
        print("""
        You're entering into the cabin,
        You see something on the table.
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
        elif choice == 2:
            self.core_gameplay()
            
    def core_gameplay(self):
        print("You see a giant woman cooking.")
        print("What would you do?")
        print("1. Get close to her.")
        print("2. Move through the hallway.")
         
        choice = input("> ")
         
        if choice == "1":
            self.trolls_scene()
        elif choice == "2":
            self.ending_scene()
        else:
            self.core_gameplay()
             
    def trolls_scene(self):
        print("You approach the giant woman cautiously...")
        # Add more gameplay logic here
        
    def ending_scene(self):
        print("You decide to move through the hallway...")
        # Add more gameplay logic here