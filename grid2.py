import random
import string

''' globals '''
position_x=0
position_y=0
look_x=0
look_y=0

print("Welcome to the Adventure!!!")

player=raw_input("What is your name? ")
print("Hi %s, thanks for playing!" % player)
print("Type 'help' for help, type 'bye' to quit.")
print("Have fun %s!" % player)

def directions(where):
    print("You can go %s" % string.join(directions, ","))

def describe(what):
        print(what)
    
def cliff(x, y, action='describe'):
    actions = {
        'describe': (lambda: describe("You are on top of a cliff")),
        'look': (lambda: describe("In the distance you see a cliff")),
    }
    
    func=actions.get(action, lambda: describe("unknown action"))
    return func()
    

def wall(x, y, action='describe'):
    actions = {
        'describe': (lambda: describe("You are next to a wall")),
        'look': (lambda: describe("In the distance you see a wall")),
    }
    
    func=actions.get(action, lambda: describe("unknown action"))
    return func()
    
    
def field(x, y, action='describe'):
    actions = {
        'describe': (lambda: describe("You are in a field")),
        'look': (lambda: describe("In the distance you see a field")),
    }
    
    func=actions.get(action, lambda: describe("unknown action"))
    return func()
    
    
def woods(x, y, action='describe'):
    actions = {
        'describe': (lambda: describe("You are in the woods")),
        'look': (lambda: describe("In the distance you see woods")),
    }
    
    func=actions.get(action, lambda: describe("unknown action"))
    return func()
    
    
def house(x, y, action='describe'):
    actions = {
        'describe': (lambda: describe("You are in a house")),
        'look': (lambda: describe("In the distance you see a house")),
    }
    
    func=actions.get(action, lambda: describe("unknown action"))
    return func()
    
def valid_coords(x, y, max_x, max_y):
    if x == -1:
        return False
    if y == -1:
        return False
    if x == max_x:
        return False
    if y == max_y:
        return False
        
    return True

def move_to(delta_x, delta_y, max_x, max_y):
    global position_x
    global position_y

    x = delta_x + position_x
    y = delta_y + position_y
    
    if valid_coords(x, y, max_x, max_y):
        position_x = x
        position_y = y
        return

    print("Move to the void?!")

def look_to(delta_x, delta_y, max_x, max_y):
    global position_x
    global position_y
    
    x = delta_x + position_x
    y = delta_y + position_y
    
    if valid_coords(x, y, max_x, max_y):
        return world[y][x](x, y, 'look')
    
    print("You see the void.")

world = [
  [ cliff, wall,  wall,  wall,  wall,  wall,  wall,  wall],   
  [ cliff, field, field, field, woods, woods, woods, wall],
  [ cliff, field, field, field, woods, woods, woods, wall],
  [ cliff, field, field, field, woods, woods, woods, wall],
  [ cliff, field, field, field, woods, woods, woods, wall],
  [ cliff, field, field, field, woods, woods, house, wall],
  [ cliff, field, field, field, woods, woods, woods, wall],
  [ cliff, field, field, field, woods, woods, woods, wall],
  [ cliff, field, field, field, woods, woods, woods, wall],
  [ cliff, field, field, field, woods, woods, woods, wall],
  [ cliff, wall,  wall,  wall,  wall,  wall,  wall,  wall]]

max_y=len(world)
max_x=len(world[0])

print("World dimensions are: %d/%d" % (max_x, max_y))


while 1:
    print("%d %d" % (position_x, position_y))
    if world[position_y][position_x](position_x, position_y, 'describe') == 0:
	    print("Goodbye")
	    break
    action=raw_input("Move (north, south, east, west)? ")
    if action == "north":
	    move_to(0, -1, max_x, max_y)
    
    if action == "south":
	    move_to(0, 1, max_x, max_y)

    if action == "west":
	    move_to(-1, 0, max_x, max_y)

    if action == "east":
	    move_to(1, 0, max_x, max_y)

    if action == "look north":
	    look_to(0, -1, max_x, max_y)
	    
    if action == "look south":
	    look_to(0, 1, max_x, max_y)

    if action == "look west":
	    look_to(-1, 0, max_x, max_y)

    if action == "look east":
	    look_to(1, 0, max_x, max_y)

    if action == "bye":
		break

