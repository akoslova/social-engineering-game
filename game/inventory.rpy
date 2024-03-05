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

    class ToDo():
        def __init__(self, aim):
            self.aim = aim
        
        def update_aim(self, aim):
            self.aim = aim

    class Person():
        def __init__(self, name, image, profession):
            self.name = name
            self.image = image
            self.profession = profession

    class People_List():
        def __init__(self, list):
            self.list = list

        def add_person(self, list):
            self.list.append(list)


label inventory:

    default inventory = Inventory([])

    #define password = InventoryData("Password", "12345678")

    #$ inventory.add_data(password)

    default todo = ToDo(" ")

    #$ todo.update_aim("Open Door")

    default people = People_List([])


    show screen inv_screen


    
