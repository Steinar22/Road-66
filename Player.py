
class Player(object):
  def __init__(self , Male , Female):
    self.Male = Male
    self.Female = Female
    
    
    class Male(Player):
      def __init__(self, name , age , nationality):
        self.name = name
        self.age = age 
        self.nationality = nationality
        
        