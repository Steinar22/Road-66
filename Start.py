from Locations import Forest
from Locations import LakeCabin
from Locations import Mountains
import Player




class Start(object):
   def choose_map():
    print("You are on Road 66 choose the route")
    print("1. To the Forest")
    print("2. To the Lake Cabin")
    print("3. To the Mountains")
   
    choice = input(">") 
    
    if choice == "1" or "the Forest":
      Forest()
    elif choice == "2" or "the Lake Cabin":
      LakeCabin()
    elif choice == "3" or " the Mountains":
      Mountains()
    else :
      Start.choose_map()
      
      
Start.choose_map()

new_game = Player("Male")
