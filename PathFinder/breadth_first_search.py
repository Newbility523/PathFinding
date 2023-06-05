from queue import Queue

from path_finder_base import path_finder


# 广度优先算法
class breadth_first_search(path_finder):
    def start(self, star: tuple, target: tuple):
        if star is None or not self.is_vaild(star):
            star = (0, 0)

        if target is None or not self.is_vaild(target):
            target = (0, 0)

        print(f"map info, width = {self.map_width}, height = {self.map_height}")
        print(f"start from {star}, to {target}")
        near = Queue()
        near.put(star)
        self.add_readched(star, None)

        while not near.empty():
            current = near.get()
            is_end = False
            for item in self.get_near(current):
                if item not in self.reached:
                    near.put(item)
                    self.add_readched(item, current)
                    if item == target:
                        is_end = True
                        break

            self.print_reached_map()
            if is_end:
                print("Target reached.")
                break
            else:
                print("Continue?")
                # if input() == "n":
                #     break
                pass

        self.print_path(star, target)

    def add_readched(self, to_pos, from_pos):
        self.reached[to_pos] = from_pos
        self.display_record[to_pos] = True
        self.reached_map[to_pos[0]][to_pos[1]] = 1

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
