from bge import logic, events

########################### Logic Bricks
# Get controller
controller = GameLogic.getCurrentController()
# Get sensor named Mouse
mouse = controller.getSensor("Mouse")

# Get the actuators
rotLeftRight = controller.getActuator("LookLeftRight")
rotUpDown = controller.getActuator("LookUpDown") 

############################## Need the size of the game window
import Rasterizer
width = Rasterizer.getWindowWidth()
height = Rasterizer.getWindowHeight()

############################### Get the mouse movement
def mouseMove():

# distance moved from screen center 
x = width/2 - mouse.getXPosition() 
y = height/2 - mouse.getYPosition()

# intialize mouse so it doesn't jerk first time
if hasattr(GameLogic, 'init') == False:
x = 0
y = 0
GameLogic.init = True

return (x, y)
pos = mouseMove()

######## Figure out how much to rotate camera and player ########
# Mouse sensitivity
sensitivity = 0.0020
# Amount, direction and sensitivity
leftRight = pos[0] * sensitivity
upDown = pos[1] * sensitivity
# invert upDown
upDown = upDown

######### Use actuators to rotate camera and player #############
# Set the rotation values
rotLeftRight.setDRot( 0.0, 0.0, leftRight, False) 
rotUpDown.setDRot( upDown, 0.0, 0.0, True)
# Use them
GameLogic.addActiveActuator(rotLeftRight, True)
GameLogic.addActiveActuator(rotUpDown, True)

############# Center mouse pointer in game window ###############
# Center mouse in game window
Rasterizer.setMousePosition(width/2, height/2)