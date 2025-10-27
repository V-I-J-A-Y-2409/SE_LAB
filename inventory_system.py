"""
inventory_system.py

A simple inventory management module for adding, removing, saving,
loading, and reporting item quantities.
"""

import json
from datetime import datetime

# Global stock data
stock_data = {}


def add_item(item="default", qty=0, logs=None):
    """Add quantity for an item. Initializes logs list if not provided."""
    if not item:
        return None

    if logs is None:
        logs = []

    try:
        qty = int(qty)
    except (TypeError, ValueError) as exc:
        raise TypeError("qty must be an integer") from exc

    stock_data[item] = stock_data.get(item, 0) + qty
    logs.append(f"{datetime.now()}: Added {qty} of {item}")
    return logs


def remove_item(item, qty):
    """Remove quantity for an item; delete item if quantity <= 0."""
    try:
        qty = int(qty)
    except (TypeError, ValueError) as exc:
        raise TypeError("qty must be an integer") from exc

    if item not in stock_data:
        raise KeyError(f"Item '{item}' not found")

    stock_data[item] -= qty
    if stock_data[item] <= 0:
        del stock_data[item]


def get_qty(item):
    """Return quantity for an item (0 if not present)."""
    return stock_data.get(item, 0)


def load_data(file="inventory.json"):
    """Load inventory from a JSON file and return the data as a dict."""
    try:
        with open(file, "r", encoding="utf-8") as file_obj:
            return json.load(file_obj)
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError as exc:
        raise ValueError("Invalid JSON in inventory file") from exc


def save_data(file="inventory.json"):
    """Save the current inventory to a JSON file."""
    with open(file, "w", encoding="utf-8") as file_obj:
        json.dump(stock_data, file_obj)


def print_data():
    """Print a report of items and their quantities."""
    print("Items Report")
    for name, qty in stock_data.items():
        print(f"{name} -> {qty}")


def check_low_items(threshold=5):
    """Return a list of items with quantity below the threshold."""
    return [name for name, qty in stock_data.items() if qty < threshold]


def main():
    """Example usage of the inventory system."""
    local_data = load_data()
    stock_data.update(local_data)

    add_item("apple", 10)
    add_item("banana", -2)

    try:
        add_item(123, "ten")
    except TypeError:
        pass

    remove_item("apple", 3)
    try:
        remove_item("orange", 1)
    except KeyError:
        pass

    print("Apple stock:", get_qty("apple"))
    print("Low items:", check_low_items())

    save_data()
    print_data()


if __name__ == "__main__":
    main()
