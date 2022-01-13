from Stepper1 import *

x_tot = 1000 # total length of movement defined in camera steps
y_tot = 1000 # total length of movement defined in camera steps

# coordinates = [(x,y) for x in range( x_tot) for y in range( y_tot )] 
p_def = [x_tot/2, y_tot/2] # default position (middle)
p1 = [x_tot/4, y_tot/4]                     # plant1 : bottom-left
p2 = [(x_tot - x_tot/4), y_tot/4]           # plant2 : bottom-right 
p3 = [x_tot/4, (y_tot - y_tot/4) ]          # plant3 : top-left
p4 = [(x_tot - x_tot/4), (y_tot - y_tot/4)] # plant4 : top-right

p_prev = p_def     # GLOBAL variable to save previous position

setupX() #setup motor for x coordinate movement
setupY() #setup motor for y coordinate movement

# moves camera from current position to target position
def move_to(p_target) :

    x_d = p_target[1] - p_prev[1]
    y_d = p_target[2] - p_prev[2]

    # move in x direction
    if x_d < 0:
        for i in reversed(range(x_d)):
            backwardStepX()
    if x_d > 0 :
        for i in (range(x_d)):
            forwardStepX()
        
    # move in y direction
    if y_d < 0 :
        for i in reversed(range(y_d)):
            backwardStepY()
    if y_d > 0 :
        for i in (range(y_d)):
            forwardStepY()
    
    #set endpoint as current point for later movement
    global p_prev
    p_prev = p_target




# move to default position from initial
def initialize() :
    global p_prev
    p_prev = [0, 0] # fill x_init and y_init according to cam position at setup
    move_to(p_def)            # move to default position



# returns to default position
def return_to_def() :

    move_to(p_def)



# moves to selected plant based on input
def plant_move(plant_select) :
    if plant_select == 1 :
        move_to(p1)
    if plant_select == 2 :
        move_to(p2)
    if plant_select == 3 :
        move_to(p3)  
    if plant_select == 4 :
        move_to(p4)     


    
