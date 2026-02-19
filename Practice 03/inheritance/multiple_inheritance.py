# Multiple Inheritance Examples 
class Camera:
    def take_photo(self):
        print("Photo taken")

class Phone:
    def charging(self):
        print("Charging your phone...")

class SmartPhone(Camera, Phone):
    pass
s = SmartPhone()
s.take_photo()  # Output: Photo taken
s.charging()        # Output: Charging your phone...


# Second example 
class Play:
    def play_game(self):
        print("Playing game", end=" and ")

class Compute:
    def calculate(self):
        print("Calculating")

class GamerRobot(Play, Compute):
    pass
robot = GamerRobot()
robot.play_game() 
robot.calculate()


# Third example of multiple inheritance
class Runner:
    def move(self):
        print("Running fast", end = " and ")

class Swimmer:
    def move(self):
        print("Swimming smoothly")

class Triathlete(Runner, Swimmer):
    def move(self):
        Runner.move(self)
        Swimmer.move(self)

t = Triathlete()
t.move()



# Fourth example of multiple inheritance
class Writer:
    def write(self):
        print("Writing a book", end=" and ")

class Artist:
    def draw(self):
        print("Drawing a picture")

class CreativePerson(Writer, Artist):
    pass
c = CreativePerson()
c.write()  # Output: Writing a book
c.draw()   # Output: Drawing a picture
