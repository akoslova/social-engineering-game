$ renpy.include("inventory.rpy")

define m = Character("Me")

label start:
    #story...

    call inventory

    m "Hello"

    