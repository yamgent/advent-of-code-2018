# for this day, both part 1 and part 2 are the same program


import sys

class Star:
    def __init__(self, pos, vel):
        self.x = pos[0]
        self.y = pos[1]
        self.x_vel = vel[0]
        self.y_vel = vel[1]


class StarMap:
    def __init__(self):
        self.stars = []
        self.boundLeft = self.boundRight = self.boundTop = self.boundBottom = 0

    def add(self, star):
        self.stars.append(star)
        self.boundLeft = min(self.boundLeft, star.x)
        self.boundRight = max(self.boundRight, star.x)
        self.boundTop = min(self.boundTop, star.y)
        self.boundBottom = max(self.boundBottom, star.y)

    def print_map(self):
        self.print_map_viewport(self.boundLeft, self.boundRight, self.boundTop, self.boundBottom)
        # self.print_map_viewport(-6, 15, -4, 11)

    def print_map_viewport(self, left, right, top, bottom):        
        if right - left > 200 or bottom - top > 50:
            print("Map is too big to print")
            return

        starPos = {}
        for s in self.stars:
            starPos[get_key(s.x, s.y)] = True

        for y in range(top, bottom + 1):
            for x in range(left, right + 1):
                print('#' if get_key(x, y) in starPos else '.', end='')
            print()

    def move_stars(self):
        for s in self.stars:
            s.x += s.x_vel
            s.y += s.y_vel

        self.boundLeft = self.boundRight = self.stars[0].x
        self.boundTop = self.boundBottom = self.stars[0].y

        for s in self.stars:
            self.boundLeft = min(self.boundLeft, s.x)
            self.boundRight = max(self.boundRight, s.x)
            self.boundTop = min(self.boundTop, s.y)
            self.boundBottom = max(self.boundBottom, s.y)



def get_key(x, y):
    return str(x) + ',' + str(y)


def get_x_y(key):
    components = key.split(',')
    return int(components[0]), int(components[1])


def main():
    starmap = StarMap()

    for line in sys.stdin:
        pos_str, vel_str = line.replace('position=<', '').replace('> velocity=<', '|').replace('>', '').split('|')
        starmap.add(Star(get_x_y(pos_str), get_x_y(vel_str)))

    picture_detected = False
    for i in range(0, 2000000):
        if starmap.boundRight - starmap.boundLeft < 200 and starmap.boundBottom - starmap.boundTop < 50:
            picture_detected = True

            print('Time: ' + str(i) + ' seconds')
            starmap.print_map()
            print()
        elif picture_detected:
            return

        starmap.move_stars()

main()
