import sys


def ft_inventory_system() -> dict:
    inventory = {}
    for i in range(1, len(sys.argv)):
        data = sys.argv[i].split(":")
        if len(data) == 2:
            if data[0] in inventory:
                print(f"Redundant item '{data[0]}' - discarding")
            else:
                try:
                    value = int(data[1])
                    inventory.update({data[0]: value})
                except ValueError as error:
                    print(f"Quantity error for '{data[0]}': {error}")
        else:
                print(f"Error - invalid parameter '{sys.argv[i]}'")
    return inventory


def main() ->None:
    print("=== Inventory System Analysis ===")
    inventory = ft_inventory_system()
    bigger_i = list(inventory.keys())[0]
    least_i = list(inventory.keys())[0]
    print(f"Got inventory: {inventory}")
    print(f"Item list: {list(inventory.keys())}")
    print(f"Total quantity of the {len(inventory)} items: {sum(inventory.values())}")
    for i in inventory.keys():
        quantity = inventory[i]
        percentage = round(quantity / sum(inventory.values()) * 100, 1)
        print(f"Item {i} represents {percentage}%")
        if inventory[i] > inventory[bigger_i]:
            bigger_i = i
        if inventory[i] < inventory[least_i]:
            least_i = i;
    print(f"Item most abundant: {bigger_i} with quantity {inventory[bigger_i]}")
    print(f"Item least abundant: {least_i} with quantity {inventory[least_i]}")
    inventory.update({"magic_update": 1})
    print(f"Updated inventory: {inventory}")


if __name__ == "__main__":
    main()
