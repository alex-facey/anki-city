# import the main necessary libraries that anki uses 
from aqt import mw, gui_hooks
from aqt.utils import qconnect
from aqt.qt import QAction
from .session_window import SessionWindow

session_window = None 

# function that opens a new window when the user clicks the add on in the tools menu
def open_session_window():
    global session_window
    if session_window is None:
        session_window = SessionWindow(mw)
        
    session_window.show() # use show so Anki isn't locked and I can still study while the session window is open
    session_window.raise_()
    session_window.activateWindow() 

# registered on Anki's answer hook so I can count reviews later
def on_card_answered(reviewer, card, ease):
    if session_window is not None:
        session_window.record_answer()

# create a qaction action that is a command the user can use, its parent is the main mw window becuase if it wasnt attached then the action would be disregarded
action = QAction("Anki City", mw)

# connect the action to the function so upon click the function executes
# this is a signals and slot connection from qt
qconnect(action.triggered, open_session_window)

# add the action to the tools menu inside the main windows layout("form" holds all the widgets inside the window)
mw.form.menuTools.addAction(action)

# register the hook
gui_hooks.reviewer_did_answer_card.append(on_card_answered)