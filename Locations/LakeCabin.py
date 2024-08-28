
class LakeCabin(object):
  def __init__(self) -> None:
    self.inventory = {
    1:"A knife",
    2:"A flare gun",
    2:"A lighter"
  }
  
  # welcome messages
  def show_messages(self):
    messages = ["You are now in the  lake side cabin" ,"Find the map of the cabin" ,"There seems to have trolls here find more about them"]
    
    for message in messages:
      print(message)
      
  def display_inventory(self):
    
    for item in self.inventory.values():
      print(item)