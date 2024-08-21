from Locations import Forest
from Locations import LakeCabin
from Locations import Mountains


class Map(object):
  location = {
    "The Forest": Forest() ,
    "The Lake Cabin": LakeCabin() ,
    "The Mountains": Mountains()
  }
    
    
  def choose_map():
    print("You are on Road 66 choose the route")
    print("1. To the Forest")
    print("2. To the Lake Cabin")
    print("3. To the Mountains")
 
    