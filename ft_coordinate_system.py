import math


class err_syntax(Exception):
    def __init__(self, msg: str = "Error: You must provide exactly three coordinates separated by commas."):
        super().__init__(msg)


def check_elements(val_list: list[str]) -> None:
    if len(val_list) != 3:
        raise err_syntax()


def get_player_pos() -> tuple[float, float, float]:
    val_str = input("Enter new coordinates as floats in format 'x,y,z': ").split(",")

    try:
        check_elements(val_str)
    except err_syntax as e:
        print(f"{e}")
        return get_player_pos()

    val_float = []
    try:
        for i in val_str:
            parametro_atual = i.strip()
            val_float.append(float(parametro_atual))
    except ValueError:
        print(f"Error on parameter '{parametro_atual}': could not convert string to float: '{parametro_atual}'")
        return get_player_pos()  

    x, y, z = val_float
    return (x, y, z)
