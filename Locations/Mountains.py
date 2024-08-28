
class Mountains(object):
  def __init__(self) -> None:
    self.inventory = {
    1:"A woolen gloves",
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