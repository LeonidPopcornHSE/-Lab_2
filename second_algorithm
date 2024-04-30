import time

def power(x, y, n):
    if y == 0:
        return 1
    z = power(x % n, y // 2, n) % n
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
    base_x, base_y, modulo = 196, 123, 31
    points = []
    for i in range(2 * n):
        x = power(base_x * i, modulo, 20 * n)
        y = power(base_y * i, modulo, 20 * n)
        points.append([x, y])
    return points

def checked(x1, y1, x2, y2, x, y):
    return 1 if (x1 <= x < x2) and (y1 <= y < y2) else 0

def compressed_coords(rects):
    coordsX, coordsY = [], []
    for rect in rects:
        coordsX.append(rect[0])
        coordsX.append(rect[2])
        coordsY.append(rect[0])
        coordsY.append(rect[2])
    coordsX = list(set(coordsX))
    coordsX.sort()
    coordsY = list(set(coordsY))
    coordsY.sort()
    return coordsX, coordsY

def create_matrix(rects, coordsX, coordsY):
    n, m = len(coordsY), len(coordsX)
    matrix = []
    for _ in range(n):
        matrix.append([0] * m)
    for i in range(n):
        for j in range(m):
            x, y = coordsX[j], coordsY[i]
            for rect in rects:
                matrix[i][j] += checked(rect[0], rect[1], rect[2], rect[3], x, y)
    return matrix

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

N = 1
for _ in range(1, 11):
    N *= 2
    rects = generate_rectangles(N)
    points = generate_points(N)
    start_time = time.perf_counter()
    coordsX, coordsY = compressed_coords(rects)
    matrix = create_matrix(rects, coordsX, coordsY)
    n, m = len(coordsY), len(coordsX)
    for point in points:
        x, y = binary_search(coordsX, point[0]), binary_search(coordsY, point[1])
    end_time =  time.perf_counter()
    print(N, (end_time - start_time) * 1000)
