#Define the base class player
class player:
  def play(self):
    print("The player is playing cricket.")
#Define the derived class Batsman
class Batsman(player):
  def play(self):
    print("the batsman is batting.")
#Define the detived class Bowler
class Bowler(player):
  def play(self):
    print("the bowler is bowling.")
#create object of Batsman and object
batsman=Batsman()
bowler=Bowler()
#call the play()method for each object
batsman.play()
bowler.play()
