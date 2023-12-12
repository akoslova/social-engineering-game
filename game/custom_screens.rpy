screen inv_screen():
    modal False

    imagebutton idle "gui/inventory_button.png":
        focus_mask True
        #hovered SetVariable("screen_tooltip", "inventory")
        #unhovered SetVariable("screen_tooltip", "")
        action Show("inventory"), Hide("inv_screen")


screen inventory():
    add "gui/inventory.png" 
    modal True 

    vbox:
        pos 0.1, 0.25
        for item in inventory.data:
            text "[item.name] - [item.description]\n" 

    imagebutton idle "gui/return.png":
        focus_mask True
        #hovered SetVariable("screen_tooltip", "Return")
        #unhovered SetVariable("screen_tooltip", "")
        action Hide("inventory"), Show("inv_screen")