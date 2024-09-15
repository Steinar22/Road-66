from Locations.Forest import Forest
from Locations.LakeCabin import LakeCabin
from Locations.Mountains import Mountains
import Player

class Start(object):
    def __init__(self) -> None:
        pass

    def choose_map(self):
        print("Choose the next route traveller:")
        print("1. To the Forest")
        print("2. To the Lake Cabin")
        print("3. To the Mountains")

        choice = input("> ").lower()  

        if choice == "1" or choice == "the forest":
            forest = Forest()
            forest.show_messages()
            forest.display_choices()  
        elif choice == "2" or choice == "the lake cabin":
            lake_cabin = LakeCabin()
            lake_cabin.show_messages()
            lake_cabin.display_choices()  
        elif choice == "3" or choice == "the mountains":
            mountains = Mountains()
            mountains.show_messages()
            mountains.display_choices()  
        else:
            print("You have to choose a map to continue!")
            self.choose_map()


start = Start()
start.choose_map()