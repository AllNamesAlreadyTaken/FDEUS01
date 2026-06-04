class Inventory:
    """Manage in-memory inventory items and quantities."""

    def __init__(self, items=[]):
        """Initialize inventory storage.

        Args:
            items: Optional list of item dictionaries with name and qty.

        Returns:
            None.
        """
        self.items = items

    def add_item(self, name, qty):
        """Add an item record to inventory.

        Args:
            name: Item name.
            qty: Quantity to store.

        Returns:
            None.
        """
        self.items.append({"name": name, "qty": qty})

    def get_stock(self, name):
        """Get the quantity in stock for a given item.

        Args:
            name: Item name to look up.

        Returns:
            Quantity as int when found, otherwise None.
        """
        for item in self.items:
            if item["name"] == name:
                return item["qty"]
        return None

    def updateStock(self, name, qty):
        """Update stock quantity for an item.

        Args:
            name: Item name to update.
            qty: New quantity value.

        Returns:
            True when the item is updated, otherwise False.
        """
        for item in self.items:
            if item["name"] == name:
                item["qty"] = qty
                return True
        return False
