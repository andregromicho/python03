import math


class err_syntax(Exception):
    def __init__(self, msg: str = "Invalid syntax") -> None:
        super().__init__(msg)


def check_elements(coords_list: list[str]) -> None:
    if len(coords_list) != 3:
        raise err_syntax()


def get_player_pos() -> tuple[float, float, float]:
    user_input = input("Enter new coordinates as floats in format 'x,y,z': ")
    coord_str = user_input.split(",")
    try:
        check_elements(coord_str)
    except err_syntax as e:
        print(f"{e}")
        return get_player_pos()

    try:
        current_coord = coord_str[0].strip()
        x = float(current_coord)

        current_coord = coord_str[1].strip()
        y = float(current_coord)

        current_coord = coord_str[2].strip()
        z = float(current_coord)

        return (x, y, z)
    except ValueError:
        print(
            f"Error on parameter '{current_coord}': "
            f"could not convert string to float: '{current_coord}'"
        )
        return get_player_pos()


def main() -> None:
    print("=== Game Coordinate System ===")

    print("Get a first set of coordinates")
    pos1 = get_player_pos()
    print(f"Got a first tuple: {pos1}")
    print(f"It includes: X={pos1[0]}, Y={pos1[1]}, Z={pos1[2]}")

    dist_to_center = math.sqrt(pos1[0] ** 2 + pos1[1] ** 2 + pos1[2] ** 2)
    print(f"Distance to center: {round(dist_to_center, 4)}")

    print("Get a second set of coordinates")
    pos2 = get_player_pos()

    dist_between = math.sqrt(
        (pos2[0] - pos1[0]) ** 2
        + (pos2[1] - pos1[1]) ** 2
        + (pos2[2] - pos1[2]) ** 2
    )
    print(
        f"Distance between the 2 sets of coordinates: "
        f"{round(dist_between, 4)}"
    )


if __name__ == "__main__":
    main()
