

class Forest(object):
    def __init__(self) -> None:
        self.inventory = {
            1: " a flashlight",
            2: " a camera",
            3: " a crowbar"
        }

    def show_messages(self): # welcome messages
        messages = ["Welcome to the Forest map", "You must navigate through this forest", "Find more about the cult revolving in the forest"]
        
        for message in messages:
            print(message)

    def display_inventory(self):
        for item in self.inventory.values():
            print(item)
            
    def display_choices(self):
        print("""
        You're entering into the forest,
        You see a small shed.
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
                    print("Choose a way.")
            except ValueError:
                print("Invalid choice. Please choose again.")
    
        if choice == 1:
            print("You see a weapons stash, you've acquired")
            self.display_inventory()
        elif choice == 2:
            print("You see a dark symbol on a tree")
    

