import math

def calculate_bounding_box(points):
    
    min_x, min_y, min_z = min(point["x"] for point in points), min(point["y"] for point in points), min(point["z"] for point in points)
    max_x, max_y, max_z = max(point["x"] for point in points), max(point["y"] for point in points), max(point["z"] for point in points)

    return {
        "minPoint": {"x": min_x, "y": min_y, "z": min_z},
        "maxPoint": {"x": max_x, "y": max_y, "z": max_z},
    }

def rotate_mesh(mesh, angle, axis):
    angle_rad = math.radians(angle)
    rotated_mesh = []
    for point in mesh:
        x, y, z = point["x"], point["y"], point["z"]
        if axis == "X":
            y, z = y * math.cos(angle_rad) - z * math.sin(angle_rad), y * math.sin(angle_rad) + z * math.cos(angle_rad)
        elif axis == "Y":
            x, z = x * math.cos(angle_rad) + z * math.sin(angle_rad), -x * math.sin(angle_rad) + z * math.cos(angle_rad)
        elif axis == "Z":
            x, y = x * math.cos(angle_rad) - y * math.sin(angle_rad), x * math.sin(angle_rad) + y * math.cos(angle_rad)
        rotated_mesh.append({"x": x, "y": y, "z": z})
    return rotated_mesh

def move_mesh(mesh, x, y, z):
    return [{"x": point["x"] + x, "y": point["y"] + y, "z": point["z"] + z} for point in mesh]

def is_polygon_convex(points):
    def cross_product(a, b, c):
        ab = [b["x"] - a["x"], b["y"] - a["y"], b["z"] - a["z"]]
        ac = [c["x"] - a["x"], c["y"] - a["y"], c["z"] - a["z"]]
        return ab[1] * ac[2] - ab[2] * ac[1]

    signs = []
    n = len(points)
    for i in range(n):
        a, b, c = points[i], points[(i + 1) % n], points[(i + 2) % n]
        signs.append(cross_product(a, b, c) >= 0)

    return all(signs) or not any(signs)

