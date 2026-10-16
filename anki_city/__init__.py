# import the main necessary libraries that anki uses 
from aqt import mw
from aqt.utils import showInfo, qconnect
from aqt.qt import QAction, QDialog, QSpinBox, QComboBox, QCheckBox, QPushButton, QFormLayout, QLabel, QTimer

session_window = None 

# define a new class that is a window that will be opened when the user clicks the add on in the tools menu
class SessionWindow(QDialog):
    def __init__(self, parent):
        super().__init__(parent)
        self.setWindowTitle("Anki City")
        self.resize(400, 300) # make window larger

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
        self.start_button = QPushButton("Start Session", self)

        layout = QFormLayout(self)
        layout.addRow("Session Length:", self.session_length)
        layout.addRow("Building Type:", self.building_type)
        layout.addRow(self.deep_focus)
        layout.addRow(self.start_button)

        # connect start button clicked signal
        qconnect(self.start_button.clicked, self.start_session)

        # label for the time
        self.time_label = QLabel("Time Remaining: 00:00", self)
        layout.addRow(self.time_label)

        # use QTImr instead of a sleep loop as a loop would prevent ankis main event loop and crash the app
        self.timer = QTimer(self)
        self.timer.setInterval(1000)  # 1 second interval
        self.timer.timeout.connect(self.tick)


    # start timer function, reads inputs at start so any changes dont effect already started session
    def start_session(self):
        minutes = self.session_length.value()
        self.session_building = self.building_type.currentText()
        self.deep_focus_enabled = self.deep_focus.isChecked()

        # disable inputs to prevent changes during the session
        self.set_inputs_enabled(False)

        self.seconds_left = minutes * 60
        mins, secs = divmod(self.seconds_left, 60)
        self.time_label.setText(f"Time Remaining: {mins:02d}:{secs:02d}")
        self.timer.start()

    # runs once every second , updates the time label and check if its at 0 
    def tick(self):
        self.seconds_left -= 1
        mins, secs = divmod(self.seconds_left, 60)
        self.time_label.setText(f"Time Remaining: {mins:02d}:{secs:02d}")

        
        if self.seconds_left <= 0:
            self.finish_session() # call the finish session function to do any cleanup or final actions

    def finish_session(self):
        self.timer.stop()
        self.set_inputs_enabled(True)

        showInfo(f"Session Complete! You built a {self.session_building}")

    def set_inputs_enabled(self, enabled):
        self.session_length.setEnabled(enabled)
        self.building_type.setEnabled(enabled)
        self.deep_focus.setEnabled(enabled)
        self.start_button.setEnabled(enabled)


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