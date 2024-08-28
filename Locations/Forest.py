

class Forest(object):
    def __init__(self) -> None:
        self.inventory = {
            1: "You have a flashlight",
            2: "You have a camera",
            3: "You have a crowbar"
        }

    def show_messages(self): # welcome messages
        messages = ["Welcome to the Forest map", "You must navigate through this forest", "Find more about the cult revolving in the forest"]
        
        for message in messages:
            print(message)

    def display_inventory(self):
        for item in self.inventory.values():
            print(item)


