$ renpy.include("inventory.rpy")

$ renpy.include("tutorial_story.rpy")

define m = Character("Me")

label  start:

    #call inventory

    #m "Hi"

    call tutorial

