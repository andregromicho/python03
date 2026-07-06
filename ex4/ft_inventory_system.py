import sys


def parse_arguments() -> dict[str, int]:
    inventory = {}

    for arg in sys.argv[1:]:
        if arg.count(":") != 1:
            print(f"Error - invalid parameter '{arg}'")
            continue

        item, qty_str = arg.split(":")

        if item in inventory:
            print(f"Redundant item '{item}' - discarding")
            continue

        try:
            qty = int(qty_str)
            inventory[item] = qty
        except ValueError as e:
            print(f"Quantity error for '{item}': {e}")

    return inventory


def main() -> None:
    print("=== Inventory System Analysis ===")

    inventory = parse_arguments()

    if not inventory:
        print("Got inventory: {}")
        return

    print(f"Got inventory: {inventory}")

    item_list = list(inventory.keys())
    print(f"Item list: {item_list}")

    total_quantity = sum(inventory.values())
    print(f"Total quantity of the {len(item_list)} items: {total_quantity}")

    for item, qty in inventory.items():
        percentage = (qty / total_quantity) * 100
        print(f"Item {item} represents {percentage:.1f}%")

    most_abundant_item = None
    max_qty = -1

    least_abundant_item = None
    min_qty = float("inf")

    for item, qty in inventory.items():
        if qty > max_qty:
            max_qty = qty
            most_abundant_item = item
        if qty < min_qty:
            min_qty = qty
            least_abundant_item = item

    print(f"Item most abundant: {most_abundant_item} with quantity {max_qty}")
    print(
        f"Item least abundant: {least_abundant_item} with quantity {min_qty}"
    )

    inventory.update({"magic_item": 1})
    print(f"Updated inventory: {inventory}")


if __name__ == "__main__":
    main()
