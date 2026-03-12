import math


def calculate_distance(
        p1: tuple[int, ...],
        p2: tuple[int, ...]
        ) -> float:
    x1, y1, z1 = p1
    x2, y2, z2 = p2
    radicand = (x2 - x1)*(x2 - x1) + (y2 - y1)*(y2 - y1) + (z2 - z1)*(z2 - z1)
    distance = math.sqrt(float(radicand))
    return distance


if __name__ == "__main__":
    print("=== Game Coordinate System ===\n")

    origin = tuple((0, 0, 0))
    created_position = tuple((10, 20, 5))
    print(f"Position created: {created_position}")
    print(
        f"Distance between {origin} and {created_position}: "
        f"{calculate_distance(origin, created_position):.2f}\n"
        )

    print("Parsing coordinates: \"3,4,0\"")
    str_coord = "3,4,0"
    list_coord = str_coord.split(",")
    parsed_position = tuple(
        [int(list_coord[0]), int(list_coord[1]), int(list_coord[2])]
        )
    print(f"Parsed position: {parsed_position}")
    print(
        f"Distance between {origin} and {parsed_position}: "
        f"{calculate_distance(origin, parsed_position):.1f}\n"
        )

    print("Parsing invalid coordinates: \"abc,def,ghi\"")
    str_coord2 = "abc,def,ghi"
    list_coord2 = str_coord2.split(",")
    try:
        parsed_position2 = tuple(
            [int(list_coord2[0]), int(list_coord2[1]), int(list_coord2[2])]
            )
    except ValueError as error:
        print(f"Error parsing coordinates: {error}")
        print(
            f"Error details - Type: {error.__class__.__name__}, "
            f"Args: {error.args}\n"
            )

    print("Unpacking demonstration:")
    x, y, z = parsed_position
    print(f"Player at x={x}, y={y}, z={z}")
    print(f"Coordinates: X={x}, Y={y}, Z={z}")
