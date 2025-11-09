import math

def taxi_zum_zum(moves:str):
    """
    🎶 The sole spot of light in the night, blinks on the roof of the taxi… 🎶 that is casually cruising in the
street grid of the dusky Manhattan, the city we know and love from classic hard boiled 9ilm noir
works such as “Blast of Silence”. The taxicab starts its journey at the origin (0,0) of the in5inite
two-dimensional integer grid, denoted by ℤ2. Fitting in the gaunt and angular spirit of the time that
tolerates few deviations or gray areas, the taxicab is at all times headed straight in one of the four
main axis directions, initially north.
This taxicab then executes the given sequence of moves, given as a string of characters 'L' for
turning 90 degrees left while standing in place (just in case we are making a turn backwards, in case
you spotted some glad rags or some out-of-town palooka looking to be taken for a ride), 'R' for
turning 90 degrees right (ditto), and 'F' for moving one block forward to current heading. This
function should return the 5inal position of the taxicab on this in5initely spanning Manhattan that
has no borders. (As someone hypothesized, the rest of the world simulates it with mirrors.)
    """
    head = [0, 1] #initially north
    position = [0, 0] # initially at the origin

    def L_Rotate(head: list):
        new_x = round(math.cos(math.pi / 2) * head[0] - math.sin(math.pi /2)*head[1])
        new_y = round(math.sin(math.pi / 2) * head[0] + math.cos(math.pi /2)*head[1])

        return [new_x, new_y]

    def R_Rotate(head: list):
        new_x = round(math.cos(-math.pi / 2) * head[0] - math.sin(-math.pi /2)*head[1])
        new_y = round(math.sin(-math.pi / 2) * head[0] + math.cos(-math.pi /2)*head[1])

        return [new_x, new_y]

    for i in moves:
        if i=='L':
            head = L_Rotate(head)
        if i=='R':
            head = R_Rotate(head)
        if i=='F':
            position[0] += head[0]
            position[1] += head[1]

    return (position[0], position[1])

print(taxi_zum_zum('RFRL'))

print(taxi_zum_zum('LFFLF'))

print(taxi_zum_zum('FR'*1729))

print(taxi_zum_zum('FFLLLFRLFLRFRLRRL'))




    

