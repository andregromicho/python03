import sys


def parse_arguments() -> dict[str, int]:
    """Processa os argumentos da linha de comandos e devolve o inventário."""
    inventory = {}

    # sys.argv[0] é o nome do próprio script, por isso saltamos e começamos no 1
    for arg in sys.argv[1:]:
        # Verificar sintaxe básica (tem de ter exatamente dois lados separados por ':')
        if ":" not in arg or arg.count(":") != 1:
            print(f"Error - invalid parameter '{arg}'")
            continue

        item, qty_str = arg.split(":")

        # Verificar se o item já foi adicionado antes (redundante)
        if item in inventory:
            print(f"Redundant item '{item}' - discarding")
            continue

        # Tentar converter a quantidade para número inteiro
        try:
            qty = int(qty_str)
            inventory[item] = qty
        except ValueError as e:
            print(f"Quantity error for '{item}': {e}")

    return inventory


def main():
    print("=== Inventory System Analysis ===")

    # 1. Obter o inventário a partir dos argumentos
    inventory = parse_arguments()

    # Se o inventário estiver vazio após o parse (nenhum argumento válido)
    if not inventory:
        print("Got inventory: {}")
        return

    # 2. Exibir o inventário
    print(f"Got inventory: {inventory}")

    # 3. Criar e exibir a lista com os nomes de todos os itens
    item_list = list(inventory.keys())
    print(f"Item list: {item_list}")

    # 4. Calcular o total de itens
    total_quantity = sum(inventory.values())
    print(f"Total quantity of the {len(item_list)} items: {total_quantity}")

    # 5. Exibir a percentagem que cada item representa (com 1 casa decimal e % no fim)
    for item, qty in inventory.items():
        percentage = (qty / total_quantity) * 100
        print(f"Item {item} represents {percentage:.1f}%")

    # 6. Encontrar os itens mais e menos abundantes
    # Em caso de empate, o enunciado pede para manter o PRIMEIRO que apareceu.
    # Como o dicionário em Python preserva a ordem de inserção, uma procura simples resolve.
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

    # 7. Atualizar o inventário com um novo item utilizando o dict.update()
    inventory.update({"magic_item": 1})
    print(f"Updated inventory: {inventory}")


if __name__ == "__main__":
    main()