import heapq
def building(a):
    buildings = []
    for i in range(len(a)):
        buildings.append(Node(a[i][0], a[i][2], -1, i)) # start == -1
        buildings.append(Node(a[i][1], a[i][2], 1, i))  # end == 1

    buildings.sort(key=lambda a: a.x)
    node_heap = []
    heapq.heappush(node_heap, buildings[0])
    cur_x = buildings[0].x
    area = 0
    for i in range(1, len(buildings)):
        if len(node_heap) > 0:
            top = node_heap[0]
            if top.y < buildings[i].y and buildings[i].state == -1:
                # cal area
                print((buildings[i].x - cur_x) * top.y)
                area += (buildings[i].x - cur_x) * top.y
                cur_x = buildings[i].x
                heapq.heappush(node_heap, buildings[i])
            elif top.y >= buildings[i].y and buildings[i].state == -1:
                heapq.heappush(node_heap, buildings[i])
            elif top.y == buildings[i].y and buildings[i].state == 1:
                print((buildings[i].x - cur_x) * top.y)
                area += (buildings[i].x - cur_x) * top.y
                cur_x = buildings[i].x
                heapq.heappop(node_heap)
            elif top.y > buildings[i].y and buildings[i].state == 1:
                remove_node(node_heap, buildings[i].number)
        else:
            heapq.heappush(node_heap, buildings[i])
            cur_x = buildings[i].x

    return area

def remove_node(array, number):
    for ele in array:
        if ele.number == number:
            array.remove(ele)
            heapq.heapify(array)
            return

class Node:
    def __init__(self, x, y, state, number):
        self.x = x
        self.y = y
        self.state = state
        self.number = number

    def __lt__(a, b):
        if a.y == b.y:
            return a.state < b.state
        return a.y > b.y



x = [ [2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8] ]
print(building(x))
