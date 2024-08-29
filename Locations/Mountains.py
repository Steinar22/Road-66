
class Mountains(object):
  def __init__(self) -> None:
    self.inventory = {
    1:" woolen gloves",
    2:"A lantern",
    3:"An adernaline injection"
  }
  
  # welcome messages
  def show_messages(self):
    messages = ["You are now at the mountains" , "You must find the mines" , "Find more about the bear and kill it"]
    
    for message in messages:
      print(message)
      
      
  def display_inventory(self):
    
    for item in self.inventory.values():
      print(item)
      
  def display_choices(self):
        print("""
        You're entering into a cave,
        You see a fireplace.
        """)
    
        choices = {
            1: "Check the fireplace.",
            2: "Keep walking into the the cave."
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
            print("You see a big grizzly bear eating a fish.")