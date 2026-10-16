# import the main necessary libraries that anki uses 
from aqt import mw
from aqt.utils import showInfo, qconnect
from aqt.qt import QAction, QDialog

# define a new class that is a window that will be opened when the user clicks the add on in the tools menu
class SessionWindow(QDialog):
    def __init__(self, parent):
        super().__init__(parent)
        self.setWindowTitle("Anki City")
        self.resize(400, 300)
        # add any additional widgets or layout to the window here

# define a function that opens a new window when the user clicks the add on in the tools menu
def open_session_window():
    dialog = SessionWindow(mw)
    dialog.show() # use show so Anki isn't locked and I can still study while the session window is open

# create a qaction action that is a command the user can use, its parent is the main mw window becuase if it wasnt attached then the action would be disregarded
action = QAction("Anki City", mw)

# connect the action to the function so upon click the function executes
# this is a signals and slot connection from qt
qconnect(action.triggered, open_session_window)

# add the action to the tools menu inside the main windows layout("form" holds all the widgets inside the window)
mw.form.menuTools.addAction(action)