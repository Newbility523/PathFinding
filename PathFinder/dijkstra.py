from queue import Queue, PriorityQueue

from path_finder_base import path_finder


# Dijkstra 寻路

class dijkstra(path_finder):
    name = "Dijkstra"
    total_cost = {}

    def get_cost(self, pos):
        return self.total_cost[pos]

    def start(self):
        start, target = self.collect_start_target()

        print(f"{self.name}")
        print(f"map info: width = {self.map_width}, height = {self.map_height}")
        print(f"target: {start} -> {target}")

        near = PriorityQueue()
        near.put([0, start])
        self.total_cost[start] = 0
        self.add_readched(None, start)

        while not near.empty():
            point_data = near.get()
            current = point_data[1]
            is_end = False
            for next_pos in self.get_near(current):
                new_cost = self.get_cost(current) + self.get_new_cost(current, next_pos)
                if next_pos not in self.reached or new_cost < self.get_cost(next_pos):
                    priority = new_cost
                    near.put([priority, next_pos])
                    self.total_cost[next_pos] = priority
                    self.add_readched(current, next_pos)
                    if next_pos == target:
                        is_end = True
                        break

            # self.print_reached_map()
            if is_end:
                print("Target reached.")
                break
            else:
                # print("Continue?")
                # if input() == "n":
                #     break
                pass

        self.print_path(start, target)

    def add_readched(self, from_pos, to_pos):
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
                        print(f"0{self.ori_map[i][j]}", end="*  ")
                    elif (i, j) == target:
                        print(f"0{self.ori_map[i][j]}", end="*  ")
                    else:
                        print(f"{self.ori_map[i][j]}-", end="   ")
                else:
                    print(f"{self.ori_map[i][j]} ", end="   ")

            print("\n")

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
