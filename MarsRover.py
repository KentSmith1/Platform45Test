# Class for Rover.
class Rover:
    def __init__(self, direction, pos_x, pos_y):
        self.direction = direction
        self.pos_x = pos_x
        self.pos_y = pos_y


# Class for Plateau.
class Plateau:
    def __init__(self, size_x, size_y):
        self.size_x = size_x
        self.size_y = size_y


# Main block.
def main():
    try:
        rover_count = int(input("Enter the amount of rovers:"))
    except ValueError:
        print("Error converting to int. Please make sure to enter only a number.")
        return
    dims = input("Enter the Plateau dimensions (1 space between each dimension please):")
    plat = create_plateau(dims)
    if type(plat) is str:
        print(plat)
        return

    rov_arr = []
    i = 0
    while i < rover_count:
        pos = input("Enter the rover position and direction:")
        rov = create_rover(pos, plat)
        if type(rov) is str:
            print(rov)
        else:
            instructions = input("Enter the rover commands:")
            rov_arr.append(run_commands(plat, rov, instructions))
            i = i + 1

    for x in rov_arr:
        print(str(x.pos_x) + " " + str(x.pos_y) + " " + x.direction)


# Function that creates plateau. Returns Plateau object.
def create_plateau(dims):
    separator = dims.find(" ")
    if separator == -1:
        return "Error. No spaces detected."
    size_x = int(dims[0:separator])
    size_y = int(dims[separator+1:])
    return Plateau(size_x, size_y)


# Function that creates Rover. Returns Rover object.
def create_rover(pos, plat):
    separator = pos.find(" ")
    if separator == -1:
        return "Error: No spaces detected."
    pos_x = int(pos[0:separator])
    if pos_x > plat.size_x:
        return "Error: X co-ordinate is out of bounds."
    _pos = pos[separator+1:]
    _separator = _pos.find(" ")
    pos_y = int(_pos[0:_separator])
    if pos_y > plat.size_y:
        return "Error: Y co-ordinate is out of bounds."
    direc = _pos[_separator+1:].upper()
    if direc != "N" and direc != "E" and direc != "S" and direc != "W":
        return "Error: Invalid direction. Please Re-enter the rover position and direction: "
    return Rover(direc, pos_x, pos_y)


# Function that processes the command string.
def run_commands(plat, rov, commands):
    for i in range(0, len(commands)):
        if commands[i].upper() == "L":
            rov.direction = change_direction(rov.direction, "L")
        elif commands[i].upper() == "R":
            rov.direction = change_direction(rov.direction, "R")
        elif commands[i].upper() == "M":
            rov = move(rov, plat)
        else:
            print("Invalid input")
    return rov


# Function to change rover direction
def change_direction(direction, turn):
    if direction == "N":
        if turn == "L":
            return "W"
        elif turn == "R":
            return "E"
    elif direction == "E":
        if turn == "L":
            return "N"
        elif turn == "R":
            return "S"
    elif direction == "S":
        if turn == "L":
            return "E"
        elif turn == "R":
            return "W"
    elif direction == "W":
        if turn == "L":
            return "S"
        elif turn == "R":
            return "N"


# Function to move rover.
def move(rover, plat):
    if rover.direction == "N":
        if rover.pos_y < plat.size_y:
            rover.pos_y = rover.pos_y + 1
    elif rover.direction == "E":
        if rover.pos_x < plat.size_x:
            rover.pos_x = rover.pos_x + 1
    elif rover.direction == "S":
        if rover.pos_y > 0:
            rover.pos_y = rover.pos_y - 1
    elif rover.direction == "W":
        if rover.pos_x > 0:
            rover.pos_x = rover.pos_x - 1
    return rover


main()
