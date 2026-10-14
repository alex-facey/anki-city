# import the main necessary libraries that anki uses 
from aqt import mw
from aqt.utils import showInfo, qconnect
from aqt.qt import QAction

# define a function that the will be done when the user does  acertain command
def show_message():
    showInfo("Wagwan, Anki!") #showinfo is ankis way of creating a pop up message to the user

# create a qaction action that is a command the user can use, its parent is the main mw window becuase if it wasnt attached then the action would be disregarded
action = QAction("Anki City", mw)

# connect the action to the function so upon click the function executes
# this is a signals and slot connection from qt
qconnect(action.triggered, show_message)

# add the action to the tools menu inside the main windows layout("form" holds all the widgets inside the window)
mw.form.menuTools.addAction(action)