import time

def calculate_power(x, y, n):
    if y == 0:
        return 1
    z = calculate_power(x % n, y // 2, n) % n
    if y % 2 == 0:
        return (z * z) % n
    else:
        return ((x % n) * ((z * z) % n)) % n

def generate_rectangles(n):
    rects = []
    for i in range(n):
        rects.append([10 * i, 10 * i, 10 * (2 * n - i), 10 * (2 * n - i)])
    return rects

def generate_points(n):
    base_x, base_y, modulo = 277, 193, 31
    points = []
    for i in range(2 * n):
        x = calculate_power(base_x * i, modulo, 20 * n)
        y = calculate_power(base_y * i, modulo, 20 * n)
        points.append([x, y])
    return points

def compress_coords(rects):
    coordsX, coordsY = [], []
    for rect in rects:
        coordsX.append(rect[0])
        coordsX.append(rect[2])
        coordsY.append(rect[1])
        coordsY.append(rect[3])
    coordsX = list(set(coordsX))
    coordsX.sort()
    coordsY = list(set(coordsY))
    coordsY.sort()
    return coordsX, coordsY

def binary_search(coords, goal):
    left, right = 0, len(coords) - 1
    if goal < coords[left] or goal > coords[right]:
        return -1
    while right >= left:
        mid = left + (right - left) // 2
        if coords[mid] == goal:
            return mid
        if coords[mid] > goal:
            right = mid - 1
        else:
            left = mid + 1
    return left - 1

class Event:
    def __init__(self, x, left, right, value):
        self.x = x
        self.left = left
        self.right = right
        self.value = value

class Node:
    def __init__(self, number, left_index, right_index, left, right):
        self.number = number
        self.left_index = left_index
        self.right_index = right_index
        self.left = left
        self.right = right

def build_segment_tree(left, right):
    if left + 1 == right:
        return Node(0, left, right, None, None)
    mid = (left + right) // 2
    l = build_segment_tree(left, mid)
    r = build_segment_tree(mid, right)
    return Node(l.number + r.number, l.left_index, r.right_index, l, r)

def insert(node, start, end, status):
    if (start <= node.left_index and node.right_index <= end):
        return Node(node.number + status, node.left_index, node.right_index, node.left, node.right)
    if (node.right_index <= start or end <= node.left_index):
        return node
    new_node = Node(node.number, node.left_index, node.right_index, node.left, node.right)
    new_node.left = insert(new_node.left, start, end, status)
    new_node.right = insert(new_node.right, start, end, status)
    return new_node

def build_persistent_segment_tree(rectangles, coordsY):
    if not rectangles:
        return None
    n = len(coordsY)
    events = []
    for rectangle in rectangles:
        events.append(Event(rectangle[0], rectangle[1], rectangle[3], 1))
        events.append(Event(rectangle[2], rectangle[1], rectangle[3], -1))
    events.sort(key=lambda element: element.x)
    root = build_segment_tree(0, n)
    roots = []
    x = events[0].x
    for event in events:
        if x != event.x:
            roots.append(root)
            x = event.x
        y1, y2 = binary_search(coordsY, event.left), binary_search(coordsY, event.right)
        root = insert(root, y1, y2, event.value)
    roots.append(root)
    return roots

def get_number(node, target):
    if node != None:
        mid = (node.left_index + node.right_index) // 2
        if (target < mid):
            return node.number + get_number(node.left, target)
        else:
            return node.number + get_number(node.right, target)
    return 0

N = 1
for _ in range(1, 11):
    N *= 2
    rects = generate_rectangles(N)
    points = generate_points(N)
    start_time = time.perf_counter()
    coordsX, coordsY = compress_coords(rects)
    roots =  build_persistent_segment_tree(rects, coordsY)
    for point in points:
        x, y = binary_search(coordsX, point[0]), binary_search(coordsY, point[1])
        ans = 0
        if (x != -1 and y != -1):
            ans = get_number(roots[x], y)
    end_time = time.perf_counter()
    print(N, (end_time - start_time) * 1000)
