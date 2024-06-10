import sys
import random
import pyautogui as p
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget
from PyQt5.QtCore import QTimer


class MouseMoverApp(QMainWindow):
    def __init__(self):
        super().__init__()

        # Get the screen width and height
        self.screen_width, self.screen_height = p.size()

        # Setup UI components
        self.initUI()

        # Timer to move mouse every 3 minutes (180000 milliseconds)
        self.move_timer = QTimer(self)
        self.move_timer.timeout.connect(self.move_mouse_randomly)
        self.move_timer.start(180000)  # 3 minutes

        # Timer for countdown
        self.countdown_timer = QTimer(self)
        self.countdown_timer.timeout.connect(self.update_countdown)
        self.countdown_timer.start(1000)  # 1 second

        # Initial countdown time in seconds
        self.remaining_time = 180  # 3 minutes

    def initUI(self):
        self.setWindowTitle('Random Mouse Mover')

        # Create a label to display the current mouse position
        self.position_label = QLabel('Current mouse position: ', self)

        # Create a label to display the countdown
        self.countdown_label = QLabel('Time until next move: 3:00', self)

        # Create a button to manually move the mouse to a random position
        self.move_button = QPushButton('Move Mouse Now', self)
        self.move_button.clicked.connect(self.move_mouse_randomly)

        # Create a layout and add widgets
        layout = QVBoxLayout()
        layout.addWidget(self.position_label)
        layout.addWidget(self.countdown_label)
        layout.addWidget(self.move_button)

        # Create a central widget, set the layout, and set it as the central widget
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        # Set the window size
        self.resize(290, 50)

        # Update the mouse position label initially
        self.update_mouse_position()

    def update_mouse_position(self):
        mouseX, mouseY = p.position()
        self.position_label.setText(f'Current mouse position: ({mouseX}, {mouseY})')

    def update_countdown(self):
        self.remaining_time -= 1
        minutes, seconds = divmod(self.remaining_time, 60)
        self.countdown_label.setText(f'Time until next move: {minutes}:{seconds:02}')
        if self.remaining_time <= 0:
            self.move_mouse_randomly()

    def move_mouse_randomly(self):
        random_x = random.randint(0, self.screen_width)
        random_y = random.randint(0, self.screen_height)
        p.moveTo(random_x, random_y, duration=0.5)
        self.update_mouse_position()
        print(f"Moved mouse to: ({random_x}, {random_y})")
        self.remaining_time = 180  # Reset countdown after move


def main():
    app = QApplication(sys.argv)
    ex = MouseMoverApp()
    ex.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
