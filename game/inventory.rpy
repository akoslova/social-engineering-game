init python:

    class Inventory():
        def __init__(self, data):
            self.data = data

        def add_data(self, data):
            self.data.append(data)

        def remove_data(self, data):
            self.data.remove(data)

        def list_items():
            for item in self.data:
                pass

    class InventoryData():
        def __init__(self, name, description):
            self.name = name
            self.description = description

label inventory:

    default inventory = Inventory([])

    define password = InventoryData("Password", "12345678")

    show screen inv_screen

    $ inventory.add_data(password)
