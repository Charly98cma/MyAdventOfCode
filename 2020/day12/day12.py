import sys

class Ship:

    def __init__(self):
        self.heading = "E"
        # Coordinates of ship
        self.lat = "N"
        self.lat_value = 0
        self.lon = "E"
        self.lon_value = 0
        self.compass = ["E", "N", "W", "S"]

    def change_heading(self, new_dir):
        self.heading = new_dir


    def change_lat(self):
        self.lat = 'S' if (self.lat == 'N') else 'N'


    def change_lon(self):
        self.lon = 'E' if (self.lon == 'W') else 'W'


    def move(self, direction, distance):
        if (direction in ['N', 'S']):
            # Ship on N/S moving N/S (respectively)
            if self.lat == direction:
                self.lat_value += distance
            else:
                # Ship does not cross 0
                if self.lat_value - distance >= 0:
                    self.lat_value -= distance
                # Ship crosses 0, update hemisphere
                else:
                    self.lat_value = distance - self.lat_value
                    self.change_lat()
        elif direction in ['E', 'W']:
            # Ship on E/W moving E/W (respectively)
            if self.lon == direction:
                self.lon_value += distance
            # Ship on E/W moving W/E (respectively)
            else:
                # Ship does not cross 0
                if self.lon_value - distance >= 0:
                    self.lon_value -= distance
                # Ship crosses 0,  update hemisphere
                else:
                    self.lon_value = distance - self.lon_value
                    self.change_lon()
        # Instruction is Forward, Left or Right
        else:
            # Instruction Forward, mode in heading direction
            if direction == 'F':
                self.move(self.heading, distance)
            # Instruction is Left or Right (turn = change heading)
            else:
                # Index of current heading
                new_index = self.compass.index(self.heading)
                # Calculate the new heading based on compass and degrees
                if direction == 'L':
                    new_index += (distance/90)
                else:
                    new_index -= (distance/90)
                # Truncate result to compass and assign new heading
                self.change_heading(self.compass[int(new_index % 4)])


def main():
    instructions = [(x[0], int(x[1:]))
                    for x in open(sys.argv[1], 'r').read().split('\n')[:-1]]
    ship = Ship()
    for direction, distance in instructions:
        ship.move(direction, distance)
    print("1st STAR SOLUTION ->", ship.lat_value+ship.lon_value)


if __name__ == "__main__":
    main()
