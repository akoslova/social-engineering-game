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

        def __init__(self, label, unlocked=False):
            self.label = label
            self.unlocked = unlocked

            levels.append(self)

        def set_unlocked(unlocked):
            self.unlocked = unlocked

    Level("tutorial", True)
    Level("level_1", True)
    Level("level_2", True)
    Level("level_3")
    Level("level_4")
    Level("level_5")


screen levels(adj):
    add "gui/levelselection/levelselection_base.png"

    for i in levels:
        if (i.unlocked):
            imagebutton auto "gui/levelselection/" + i.label + "_unlocked_%s.png":
                focus_mask True
                action Jump(i.label)
        else:
            imagebutton auto "gui/levelselection/" + i.label + "_locked_%s.png":
                focus_mask True


# This is used to preserve the state of the scrollbar on the selection
# screen.
default tutorials_adjustment = ui.adjustment()


label start:

    #call screen levels
    call screen levels(adj=tutorials_adjustment)

    #call tutorial

