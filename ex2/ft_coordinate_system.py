import math


def get_player_pos() -> tuple:
    while True:
        data = input("Enter new coordinates "
                     "as floats in format 'x,y,z': ")
        coordinates = data.split(",")
        if len(coordinates) == 3:
            xyz = []
            try:
                for cords in coordinates:
                    cords_value = float(cords)
                    xyz.append(cords_value)
                break
            except ValueError as error:
                print(f"Error on parameter '{cords}': '{error}'")
        else:
            print("Invalid syntax")
    return tuple(xyz)


def main() -> None:
    print("=== Game Coordinate System ===")
    print()
    print("Get a first set of coordinates")
    a = get_player_pos()
    print(f"Got a first tuple: {a}")
    print(f"It includes: X={a[0]}, "
        f"Y={a[1]}, Z={a[2]}")
    distance = math.sqrt(
    a[0] ** 2
    + a[1] ** 2
    + a[2] ** 2
    )
    print(f"Distance to center: {round(distance, 4)}")
    print()
    print("Get a second set of coordinates")
    b = get_player_pos()
    print(f"Got a second tuple: {b}")
    final_distance = math.sqrt(
    (a[0]-b[0])**2
    + (a[1]-b[1])**2
    + (a[2]-b[2])**2)
    print(f"Distance between the 2 sets of coordinates: {round(final_distance, 4)}")

if __name__ == "__main__":
    main()
