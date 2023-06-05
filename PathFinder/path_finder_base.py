import copy
from queue import Queue


# 广度优先算法
class path_finder:
    name = ""
    reached_map = []
    ori_map = []
    map_width = 0
    map_height = 0

    reached = {}

    display_record = {}
    _start_chars = ['s', 'S']
    _target_chars = ['t', 'T']
    _block_chars = ['x', 'X']

    def __init__(self, input_map: list):
        self.ori_map = copy.deepcopy(input_map)
        self.reached_map = copy.deepcopy(input_map)
        self.map_width = len(input_map)
        self.map_height = len(input_map[0])

    def clean(self):
        pass

    def add_readched(self, to_pos, from_pos):
        self.reached[to_pos] = from_pos
        self.display_record[to_pos] = True
        self.reached_map[to_pos[0]][to_pos[1]] = 1

    def collect_start_target(self):
        start = None
        target = None
        for i in range(self.map_width):
            for j in range(self.map_height):
                if start is None and self.ori_map[i][j] in self._start_chars:
                    start = (i, j)

                if target is None and self.ori_map[i][j] in self._target_chars:
                    target = (i, j)

        return start, target

    def start(self):
        pass

    def get_new_cost(self, from_pos: tuple, to_pos: tuple):
        c = self.ori_map[to_pos[0]][to_pos[1]]
        if c in self._start_chars:
            return 1
        if c in self._target_chars:
            return 1
        if c in self._block_chars:
            return 99999

        c_num = int(c)
        if c_num <= 0:
            c_num = 1

        return c_num

    def print_path(self, star: tuple, target: tuple):
        print("result: ")
        path = []
        current = target
        if not self.reached[current]:
            print("not path!")
            return

        while current is not None and current != star:
            path.append(current)
            current = self.reached[current]

        path.append(star)
        path.reverse()

        for item in path:
            print(f"({item[0]}, {item[1]})", end=" -> ")

        print("")

        for i in range(self.map_width):
            for j in range(self.map_height):
                if (i, j) in path:
                    if (i, j) == star:
                        print("S", end="* ")
                    elif (i, j) == target:
                        print("T", end="* ")
                    else:
                        print("=", end="  ")
                else:
                    print(self.ori_map[i][j], end="  ")

            print("")

    def print_reached_map(self):
        for i in range(self.map_width):
            for j in range(self.map_height):
                index = (i, j)
                if index in self.display_record:
                    print(self.reached_map[i][j], end="* ")
                else:
                    print(self.reached_map[i][j], end="  ")

            print("")

        self.display_record.clear()

    def is_vaild(self, pos):
        if pos is None:
            return False
        if pos[0] < 0 or pos[0] >= self.map_width:
            return False
        if pos[1] < 0 or pos[1] >= self.map_height:
            return False
        if self.ori_map[pos[0]][pos[1]] in self._block_chars:
            return False

        return True

    def get_near(self, pos):
        near_list = []
        if self.is_vaild((pos[0] - 1, pos[1])):
            near_list.append((pos[0] - 1, pos[1]))
        if self.is_vaild((pos[0] + 1, pos[1])):
            near_list.append((pos[0] + 1, pos[1]))
        if self.is_vaild((pos[0], pos[1] - 1)):
            near_list.append((pos[0], pos[1] - 1))
        if self.is_vaild((pos[0], pos[1] + 1)):
            near_list.append((pos[0], pos[1] + 1))

        return near_list
