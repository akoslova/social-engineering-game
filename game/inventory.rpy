init python:

    class Inventory():
        def __init__(self, data):
            self.data = data

        def add_data(self, data):
            self.data.append(data)

        def remove_data(self, data):
            self.data.remove(data)

    class InventoryData():
        def __init__(self, name, description):
            self.name = name
            self.description = description

label start:

    default inventory = Inventory([])

    define password = InventoryData("Password", "12345678")

    $ inventory.add_data(password)
