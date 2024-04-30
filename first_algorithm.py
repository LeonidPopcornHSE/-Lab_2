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
    rectangles = []
    for i in range(n):
        rectangles.append([10 * i, 10 * i, 10 * (2 * n - i), 10 * (2 * n - i)])
    return rectangles

def generate_points(n):
    base_x, base_y, modulo = 196, 123, 31
    points = []
    for i in range(2 * n):
        x = calculate_power(base_x * i, modulo, 20 * n)
        y = calculate_power(base_y * i, modulo, 20 * n)
        points.append([x, y])
    return points

def is_inside_rectangle(x1, y1, x2, y2, x, y):
    return 1 if (x1 <= x < x2) and (y1 <= y < y2) else 0

n = 1
for _ in range(1, 11):
    n *= 2
    rectangles = generate_rectangles(n)
    points = generate_points(n)
    start_time = time.perf_counter()
    for point in points:
        ans = 0
        for rect in rectangles:
            ans += is_inside_rectangle(rect[0], rect[1], rect[2], rect[3], point[0], point[1])
    end_time = time.perf_counter()
    print(n, (end_time - start_time) * 1000)
