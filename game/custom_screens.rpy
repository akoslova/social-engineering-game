$ renpy.include("screens.rpy")

screen inv_screen():
    modal False

    imagebutton auto "gui/inventory/bookicon_%s.png":
        focus_mask True
        #hovered SetVariable("screen_tooltip", "inventory")
        #unhovered SetVariable("screen_tooltip", "")
        action Show("knowledge_inventory"), Hide("inv_screen")


screen knowledge_inventory():
    add "gui/inventory/background.png" 
    add "gui/inventory/book.png" 
    add "gui/inventory/todos.png"
    add "gui/inventory/knowledge_tab.png"
    
    modal True 

    vbox:
        pos 0.25, 0.25
        for item in inventory.data:
            text "[item.name] - [item.description]\n" style "inventory_text"
    
    vbox:
        pos 0.8, 0.2
        text "[todo.aim]"

    imagebutton auto "gui/inventory/back_%s.png":
        focus_mask True
        #hovered SetVariable("screen_tooltip", "Return")
        #unhovered SetVariable("screen_tooltip", "")
        action Hide("knowledge_inventory"), Show("inv_screen")

    imagebutton idle "gui/inventory/people_tab.png":
        focus_mask True
        action Show("people_inventory"), Hide("knowledge_inventory")


screen people_inventory():
    add "gui/inventory/background.png" 
    add "gui/inventory/book.png"
    add "gui/inventory/people_tab.png"

    modal True 

    vbox:
        pos 0.25, 0.25
        for item in people.list:
            hbox:
                add [item.image]
                vbox:
                    text "Name: [item.name]\n" style "inventory_text"
                    text "Profession: [item.profession]\n" style "inventory_text"
    

    imagebutton idle "gui/inventory/knowledge_tab.png":
        focus_mask True
        action Show("knowledge_inventory"), Hide("people_inventory")

    imagebutton auto "gui/inventory/back_%s.png":
        focus_mask True
        #hovered SetVariable("screen_tooltip", "Return")
        #unhovered SetVariable("screen_tooltip", "")
        action Hide("people_inventory"), Show("inv_screen")