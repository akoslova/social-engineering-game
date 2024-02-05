$ renpy.include("screens.rpy")
$ i = 0

screen inv_screen():
    modal False

    imagebutton auto "gui/inventory/bookicon_%s.png":
        focus_mask True
        action Show("knowledge_inventory_page1"), Hide("inv_screen")


screen knowledge_inventory_page1():
    add "gui/inventory/background.png" 
    add "gui/inventory/book.png" 
    add "gui/inventory/todos.png"
    add "gui/inventory/paperclip.png"
    add "gui/inventory/knowledge_tab_active.png"
    
    modal True 

    default res = False
    default data = inventory.data

    $ if (len(inventory.data) > 5): res = True

    $ if (len(inventory.data) > 5): data = inventory.data[0:4]
   

    vbox:
        pos 0.20, 0.15
        xmaximum 0.3
    
        for item in data:
            text "[item.name] - [item.description]\n" style "inventory_text"
    
    vbox:
        pos 0.75, 0.2
        xmaximum 0.15
        text "[todo.aim]"

    imagebutton auto "gui/inventory/back_%s.png":
        focus_mask True
        action Hide("knowledge_inventory_page1"), Show("inv_screen")

    imagebutton idle "gui/inventory/people_tab.png":
        focus_mask True
        action Show("people_inventory"), Hide("knowledge_inventory_page1")
    
    if res:
        imagebutton auto "gui/inventory/arrowright_%s.png":

            focus_mask True 
            action Hide("knowledge_inventory_page1"), Show("knowledge_inventory_page2") 

screen knowledge_inventory_page2():
    add "gui/inventory/background.png" 
    add "gui/inventory/book.png" 
    add "gui/inventory/todos.png"
    add "gui/inventory/paperclip.png"
    add "gui/inventory/knowledge_tab_active.png"
    
    modal True 

    default data = []

    $ if (len(inventory.data) > 5): data = inventory.data[4:] 

    vbox:
        pos 0.25, 0.25
    
        for item in data:
            text "[item.name] - [item.description]\n" style "inventory_text"
    
    vbox:
        pos 0.78, 0.25
        text "[todo.aim]"

    imagebutton auto "gui/inventory/back_%s.png":
        focus_mask True
        action Hide("knowledge_inventory_page2"), Show("inv_screen")

    imagebutton idle "gui/inventory/people_tab.png":
        focus_mask True
        action Show("people_inventory"), Hide("knowledge_inventory_page_2")
    
    imagebutton auto "gui/inventory/arrowleft_%s.png":
        focus_mask True
        action Hide("knowledge_inventory_page2"), Show("knowledge_inventory_page1")


screen people_inventory():
    add "gui/inventory/background.png" 
    add "gui/inventory/book.png"
    add "gui/inventory/people_tab_active.png"

    modal True 

    vbox:
        pos 0.2, 0.15
        for item in people.list:
            hbox:
                add [item.image] zoom 0.25
                vbox:
                    pos -0.8, 0.25
                    text "Name: [item.name]\n" style "inventory_text"
                    text "Profession: [item.profession]\n" style "inventory_text"
    

    imagebutton idle "gui/inventory/knowledge_tab.png":
        focus_mask True
        action Show("knowledge_inventory_page1"), Hide("people_inventory")

    imagebutton auto "gui/inventory/back_%s.png":
        focus_mask True
        action Hide("people_inventory"), Show("inv_screen")

screen nameInput(prompt):
    add "images/bg laptop.png"

    vbox:
        align(0.5,0.358)
        spacing 30

        text prompt:
            xalign 0.5
            size 26
            color "#ffffff"

        input:
            id "input"
            xalign 0.5
            size 26
            color "#ffffff"

screen map(place):
    add "gui/map/background.png"

    modal True 

    imagebutton idle "gui/map/cafe.png":
        focus_mask True

    imagebutton idle "gui/map/core.png":
        focus_mask True

    imagebutton idle "gui/map/event.png":
        focus_mask True

    imagebutton idle "gui/map/tastyfood.png":
        focus_mask True


    if place == "cafe":
        imagebutton auto "gui/map/cafe_active_%s.png":
            focus_mask True
            action Hide("map"), Return()

    if place == "core":
        imagebutton auto "gui/map/core_active_%s.png":
            focus_mask True
            action Hide("map"), Return()

    if  place == "event":
        imagebutton auto "gui/map/event_active_%s.png":
            focus_mask True
            action Hide("map"), Return()

    if place == "tastyfood":
        imagebutton auto "gui/map/tastyfood_active_%s.png":
            focus_mask True
            action Hide("map"), Return()