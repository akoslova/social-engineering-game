$ renpy.include("inventory.rpy")

$ renpy.include("tutorial_story.rpy")
$ renpy.include("level_1.rpy")

init python:

    # A list of level objects.
    levels = [ ]

    class Level(object):
        """
        Represents a label that we can jump to.
        """

        def __init__(self, label, title, unlocked=False):
            self.label = label
            self.title = title

            levels.append(self)


    Level("tutorial", _("Tutorial"))
    Level("level_1", _("Level 1"))


screen levels(adj):

    frame:
        xsize 640
        xalign .5
        ysize 485
        ypos 30

        #has side "c r b"

        viewport:
            yadjustment adj
            mousewheel True
            draggable True

            vbox:
                for i in levels:

                    textbutton i.title:
                        #action Return(i)
                        action Jump(i.label)
                        left_padding 20
                        xfill True


        bar adjustment adj style "vscrollbar"

        #textbutton _("That's enough for now."):
            #xfill True
            #action Return(False)
            #top_margin 10


# This is used to preserve the state of the scrollbar on the selection
# screen.
default tutorials_adjustment = ui.adjustment()

# True if this is the first time through the tutorials.
default tutorials_first_time = True


label  start:

    call screen levels(adj=tutorials_adjustment)

    #call tutorial

