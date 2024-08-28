from Locations.Forest import Forest
from Locations.LakeCabin import LakeCabin
from Locations.Mountains import Mountains
import Player

class Start(object):
    def __init__(self) -> None:
        pass

    def choose_map(self):
        print("You are on Road 66. Choose the route:")
        print("1. To the Forest")
        print("2. To the Lake Cabin")
        print("3. To the Mountains")

        choice = input("> ").lower()  

        if choice == "1" or choice == "the forest":
            forest = Forest()
            forest.show_messages()  
        elif choice == "2" or choice == "the lake cabin":
            lake_cabin = LakeCabin()
            lake_cabin.show_messages()  
        elif choice == "3" or choice == "the mountains":
            mountains = Mountains()
            mountains.show_messages()  
        else:
            print("You have to choose a map to continue!")


start = Start()
start.choose_map()