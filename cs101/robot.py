from cs1robots import *

create_world(avenues = 5, streets = 5)

# create a robot with one beeper
hubo = Robot(beepers = 1)

# for debugging
hubo.set_pause(0.7)
hubo.set_trace('blue')

# move one step forward
hubo.move()

# turn left 90 degrees
hubo.turn_left()

def turn_right():
    hubo.turn_left()
    hubo.turn_left()
    hubo.turn_left()

hubo.move()
turn_right()
hubo.move()
hubo.turn_left()
hubo.move()
turn_right()