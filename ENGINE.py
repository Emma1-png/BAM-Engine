import turtle as tu

# Put new algorithm here for penscale calculation
# Min 10
# Max 75
resolution = 10
#Get Penscale
def getPenScale(res):
  """
  Get penscale*resolution=1500 - p*r=1500
  If r = 50, p must be equal to 30
  """

  p = 1500/res

  return p
penscale = getPenScale(resolution)

screenWidth = 850
screenHeight = 550
wn = tu.Screen()
wn.screensize(screenWidth, screenHeight)
wn.setup(screenWidth, screenHeight)

backgroundTurtle = tu.Turtle()
backgroundTurtle.shape("turtle")

class Hex:
  def __init__(self, colour1: str, colour2: str):
    self.colour1 = colour1.lstrip("#")
    self.colour2 = colour2.lstrip("#")

  def HEXtoRGB(self, h):
    return tuple(int(h[i:i+2], 16) for i in (0, 2, 4))
  def RGBtoHEX(self, rgb):
    return "#{:02x}{:02x}{:02x}".format(*rgb)

  def list(self, resolution: int):
    """resolution = amount of colours in the list
    returns list"""
    rgb1 = self.HEXtoRGB(self.colour1)
    rgb2 = self.HEXtoRGB(self.colour2)

    gradient = []

    for i in range(resolution):
      t = i / (resolution - 1)
      rgb = tuple(
        int(rgb1[j] + (rgb2[j] - rgb1[j]) * t)
        for j in range(3)
      )
    gradient.append(self.RGBtoHEX(rgb))
    return gradient

h = Hex("#00FF00", "#FF00FF")
lists = h.list(resolution)

def renderThumbnail():
  backgroundTurtle.clear()

  backgroundTurtle.pensize(penscale)
  backgroundTurtle.pu()
  backgroundTurtle.speed(0)
  backgroundTurtle.goto(-screenWidth/2, -screenHeight/2)
  backgroundTurtle.pd()

  for i in range(resolution):
    backgroundTurtle.pencolor(lists[i])
    backgroundTurtle.fd(screenWidth)
    backgroundTurtle.goto(-screenWidth/2, -screenHeight/2 + (penscale*i)/2.5)

renderThumbnail()

##################
# NEW STUFF HERE #
##################

shapesTurtle = tu.Turtle()
shapesTurtle.shape("turtle")

# Placeholder
shapesTurtle.fillcolor("grey")

class Shapes:
  def __init__(self):
    pass
  def Cube(self, position1List: list, position2List: list, rotationList: list):
    """Returns a list of co ordinates for shapesTurtle to follow"""
    print("TEST CO ORDINATES")
    print(f"1: X:{position1List[0]} Y:{position1List[1]} Z:{position1List[2]}")
    print(f"2: X:{position2List[0]} Y:{position2List[1]} Z:{position2List[2]}")
    print(f"R: X:{rotationList[0]} Y:{rotationList[1]} Z:{rotationList[2]}")

    coordinates = [] # Refer to function definition ("""|""")

    # DO further maths later for rotationList & Z for p1L & p2L
    coordinates.append([position1List[0], position1List[1]])
    coordinates.append([position2List[0], position2List[1]])

    return coordinates

def renderShapesThumbnail(shape):
  shapesTurtle.goto(shape[0][0], shape[0][1])
  shapesTurtle.begin_fill() # FIX THIS
  shapesTurtle.goto(shape[1][0], shape[1][1])
  shapesTurtle.goto(0, 0) # Placeholder
  shapesTurtle.end_fill()

s = Shapes()
renderShapesThumbnail(s.Cube([80, 10, 50], [-30, -40, 5], [10, 0, 0]))

################
wn.exitonclick()
