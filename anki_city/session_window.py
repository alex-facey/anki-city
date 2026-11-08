# import the main necessary libraries that anki uses 
from aqt import mw
from aqt.utils import showInfo, qconnect
from aqt.qt import QDialog, QSpinBox, QComboBox, QCheckBox, QPushButton, QFormLayout, QLabel, QTimer
from .storage import save_session

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

        self.cards_label = QLabel("Cards Reviewed: 0", self)
        layout.addRow(self.cards_label)
        self.cards_reviewed = 0


    # start timer function, reads inputs at start so any changes dont effect already started session
    def start_session(self):
        config = mw.addonManager.getConfig(__name__)
        self.batch_size = config["batch_size"]
        self.cards_reviewed = 0
        self.cards_label.setText("Cards Reviewed: 0")
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
        total_buildings = 1 + self.cards_reviewed // self.batch_size
        save_session(self.session_building, total_buildings,  self.cards_reviewed, broken=False)

        showInfo(f"Session complete! You reviewed {self.cards_reviewed} cards and built {total_buildings} {self.session_building}{'s' if total_buildings != 1 else ''}")
    
    # counts every answer including Again, so there's never a reason to grade a card dishonestly to earn more
    def record_answer(self):
        if self.timer.isActive():
            self.cards_reviewed += 1
            self.cards_label.setText(f"Cards Reviewed: {self.cards_reviewed}")


    #helper functions
    def set_inputs_enabled(self, enabled):
        self.session_length.setEnabled(enabled)
        self.building_type.setEnabled(enabled)
        self.deep_focus.setEnabled(enabled)
        self.start_button.setEnabled(enabled)