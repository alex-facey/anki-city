# import the main necessary libraries that anki uses 
from aqt import mw
from aqt.utils import showInfo, qconnect
from aqt.qt import QAction, QDialog, QSpinBox, QComboBox, QCheckBox, QPushButton, QFormLayout

session_window = None 

# define a new class that is a window that will be opened when the user clicks the add on in the tools menu
class SessionWindow(QDialog):
    def __init__(self, parent):
        super().__init__(parent)
        self.setWindowTitle("Anki City")
        self.resize(400, 300) # make window larger

        # add any additional widgets or layout to the window 
        
        # session length widget
        self.session_length = QSpinBox(self)
        self.session_length.setRange(1, 120) # set the range of the spinbox
        self.session_length.setValue(30) # set the default value of the spinbox
        self.session_length.setSuffix(" minutes") 

        # building type widget
        self.building_type = QComboBox(self)
        self.building_type.addItems(["Nexus Tower", "Arasaka Spire", "Chrome Citadel"]) # add items to the list of strings
        
        # deep focus checkbox widget
        self.deep_focus = QCheckBox("Deep Focus", self)
        
        # start button widget
        start_button = QPushButton("Start Session", self)

        layout = QFormLayout(self)
        layout.addRow("Session Length:", self.session_length)
        layout.addRow("Building Type:", self.building_type)
        layout.addRow(self.deep_focus)
        layout.addRow(start_button)

        # connect start button clicked signal
        qconnect(start_button.clicked, self.start_session)


    # start timer function
    def start_session(self):
        minutes = self.session_length.value()
        building = self.building_type.currentText()
        deep_focus = self.deep_focus.isChecked()

        # show info message with the selected options
        showInfo(f"Starting a {minutes} minute session to build {building} with Deep Focus {'enabled' if deep_focus else 'disabled'}.")


# define a function that opens a new window when the user clicks the add on in the tools menu
def open_session_window():
    global session_window
    if session_window is None:
        session_window = SessionWindow(mw)
        
    session_window.show() # use show so Anki isn't locked and I can still study while the session window is open
    session_window.raise_()
    session_window.activateWindow() 

# create a qaction action that is a command the user can use, its parent is the main mw window becuase if it wasnt attached then the action would be disregarded
action = QAction("Anki City", mw)

# connect the action to the function so upon click the function executes
# this is a signals and slot connection from qt
qconnect(action.triggered, open_session_window)

# add the action to the tools menu inside the main windows layout("form" holds all the widgets inside the window)
mw.form.menuTools.addAction(action)