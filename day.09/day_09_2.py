import sys

class Marble:
    def __init__(self, id):
        self.id = id
        self.left = None
        self.right = None

    def connect_left(self, other):
        if self.left != None:
            self.disconnect_left()

        self.left = other
        self.left.right = self

    def connect_right(self, other):
        if self.right != None:
            self.disconnect_right()

        self.right = other
        self.right.left = self

    def disconnect_left(self):
        if self.left == None:
            return

        self.left.right = None
        self.left = None

    def disconnect_right(self):
        if self.right == None:
            return
        
        self.right.left = None
        self.right = None


def print_circle(start_point, current):
    print(start_point.id, end=' ')
    
    next_point = start_point.right
    while next_point != start_point:
        if next_point != current:
            print(next_point.id, end=' ')
        else:
            print('(' + str(next_point.id) + ')', end=' ')

        next_point = next_point.right

    print()


def add_new_marble(new_id, current_marble, all_scores, current_player):
    if new_id % 23 != 0:
        new_marble = Marble(new_id)
        neighbour_left = current_marble.right
        neighbour_right = current_marble.right.right

        neighbour_left.connect_right(new_marble)
        neighbour_right.connect_left(new_marble)

        return new_marble
    else:
        score = new_id

        seventh_marble = current_marble
        for i in range(0, 7):
            seventh_marble = seventh_marble.left
        
        score += seventh_marble.id
        new_current = seventh_marble.right

        seventh_marble.left.connect_right(seventh_marble.right)

        all_scores[current_player] += score
        return new_current


def run_test_case(line):
    input_split = [x for x in line.split(' ')]
    total_players = int(input_split[0])
    total_marbles = int(input_split[6]) * 100

    scores = [0] * total_players
    current_player = 0

    zero = Marble(0)
    zero.connect_left(zero)
    zero.connect_right(zero)

    current_marble = zero

    for new_id in range(1, total_marbles + 1):
        current_marble = add_new_marble(new_id, current_marble, scores, current_player)
        current_player = (current_player + 1) % total_players
        # print_circle(zero, current_marble)

    print(max(scores))


def main():
    for line in sys.stdin:
        run_test_case(line)


main()
