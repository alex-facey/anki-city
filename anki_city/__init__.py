# import the main necessary libraries that anki uses 
from aqt import mw
from aqt.utils import showInfo, qconnect
from aqt.qt import QAction, QDialog

# define a function that open a new window when the user clicks the add on in the tools menu
def open_session_window():
    dialog = QDialog(mw)
    dialog.setWindowTitle("Anki City")
    # dialog.resize(400, 300)
    dialog.show() # use show so Anki isn't locked and I can still study while the session window is open

# create a qaction action that is a command the user can use, its parent is the main mw window becuase if it wasnt attached then the action would be disregarded
action = QAction("Anki City", mw)

# connect the action to the function so upon click the function executes
# this is a signals and slot connection from qt
qconnect(action.triggered, open_session_window)

# add the action to the tools menu inside the main windows layout("form" holds all the widgets inside the window)
mw.form.menuTools.addAction(action)