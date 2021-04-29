import sys

class Ship:

    def __init__(self):
        self.heading = "E"
        self.lat = "N"
        self.latValue = 0
        self.lon = "E"
        self.lonValue = 0
        self.compass = ["E","N","W","S"]


    def changeHeading(self, new_dir):
        self.heading = new_dir


    def changeLat(self):
        self.lat = 'S' if (self.lat == 'N') else 'N'


    def changeLon(self):
        self.lon = 'E' if (self.lon == 'W') else 'W'


    def move(self, direction, distance):
        if (direction in ['N','S']):
            # Ship on N/S moving N/S (respectively)
            if (self.lat == direction):
                self.latValue += distance
            else:
                # Ship does not cross 0
                if (self.latValue - distance >= 0):
                    self.latValue -= distance
                # Ship crosses 0, update hemisphere
                else:
                    self.latValue = distance - self.latValue
                    self.changeLat()
        elif (direction in ['E','W']):
            # Ship on E/W moving E/W (respectively)
            if (self.lon == direction):
                self.lonValue += distance
            # Ship on E/W moving W/E (respectively)
            else:
                # Ship does not cross 0
                if (self.lonValue - distance >= 0):
                    self.lonValue -= distance
                # Ship crosses 0,  update hemisphere
                else:
                    self.lonValue = distance - self.lonValue
                    self.changeLon()
        # Instruction is Forward, Left or Right
        else:
            # Instruction Forward, mode in heading direction
            if (direction == 'F'):
                self.move(self.heading, distance)
            # Instruction is Left or Right (turn = change heading)
            else:
                # Index of current heading
                newI = self.compass.index(self.heading)
                # Calculate the new heading based on compass and degrees
                if (direction == 'L'):
                    newI += (distance/90)
                else:
                    newI -= (distance/90)
                # Truncate result to compass and assign new heading
                self.heading = self.compass[int(newI%4)]

def main():
    instructions = [(x[0], int(x[1:])) for x in open(sys.argv[1], 'r').read().split('\n')[:-1]]
    ship = Ship()
    for direction, distance in instructions:
        ship.move(direction, distance)
    print("1st STAR SOLUTION ->", ship.latValue+ship.lonValue)


if __name__ == "__main__":
    main()
