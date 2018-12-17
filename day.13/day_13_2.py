import sys
import functools

# direction: 0 - north, 1 - east, 2 - south, 3 - west
# intersectMemory: 0 - left, 1 - straight, 2 - right
class Cart:
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction
        self.intersectMemory = 0

    def get_pos_string(self):
        return get_string(self.x, self.y)

    def move_forward(self, forward_slash, backward_slash, intersections):
        if self.direction == 0:
            self.y -= 1
        elif self.direction == 1:
            self.x += 1
        elif self.direction == 2:
            self.y += 1
        elif self.direction == 3:
            self.x -= 1
        
        pos_str = self.get_pos_string()

        if pos_str in forward_slash:
            if self.direction == 0 or self.direction == 2:
                self.turn_right()
            else:
                self.turn_left()
        elif pos_str in backward_slash:
            if self.direction == 0 or self.direction == 2:
                self.turn_left()
            else:
                self.turn_right()
        elif pos_str in intersections:
            if self.intersectMemory == 0:
                self.turn_left()
            elif self.intersectMemory == 1:
                # go straight - do nothing
                pass
            else:
                self.turn_right()

            self.intersectMemory = (self.intersectMemory + 1) % 3
    
    def find_another_cart_same_pos(self, carts):
        for c in carts:
            if c == self:
                continue
            if c.x == self.x and c.y == self.y:
                return c
        return None
    
    def turn_right(self):
        self.direction = (self.direction + 1) % 4
    
    def turn_left(self):
        self.direction = (self.direction - 1) % 4


def compare_cart_positions(cart_a, cart_b):
    if cart_a.y == cart_b.y:
        return cart_a.x - cart_b.x
    return cart_a.y - cart_b.y


# def get_x_y(string):
#    return [int(x) for x in string.split(',')]


def get_string(x, y):
    return str(x) + ',' + str(y)


def find_all_characters(string, character):
    result = []

    i = string.find(character)
    while i != -1:
        result.append(i)
        i = string.find(character, i + 1)
    
    return result


def parse_input(forward_slash, backward_slash, intersections, carts):
    y = 0
    for line in sys.stdin:
        
        for x in find_all_characters(line, '/'):
            forward_slash.append(get_string(x, y))

        for x in find_all_characters(line, '\\'):
            backward_slash.append(get_string(x, y))

        for x in find_all_characters(line, '+'):
            intersections.append(get_string(x, y))

        for x in find_all_characters(line, '^'):
            carts.append(Cart(x, y, 0))

        for x in find_all_characters(line, '>'):
            carts.append(Cart(x, y, 1))

        for x in find_all_characters(line, 'v'):
            carts.append(Cart(x, y, 2))

        for x in find_all_characters(line, '<'):
            carts.append(Cart(x, y, 3))

        y += 1


def main():
    forward_slash = []
    backward_slash = []
    intersections = []
    carts = []

    parse_input(forward_slash, backward_slash, intersections, carts)

    while True:
        carts = sorted(carts, key=functools.cmp_to_key(compare_cart_positions))
        crashed_carts = []
        for c in carts:
            if c in crashed_carts:
                continue

            c.move_forward(forward_slash, backward_slash, intersections)
            another_cart = c.find_another_cart_same_pos(carts)
            if another_cart != None:
                crashed_carts.append(c)
                crashed_carts.append(another_cart)
        
        for c in crashed_carts:
            carts.remove(c)

        if len(carts) == 1:
            print(str(carts[0].x) + ',' + str(carts[0].y))
            return

if __name__ == '__main__':
    main()
