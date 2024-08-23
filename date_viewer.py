from datetime import datetime
import os
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QMessageBox, QLabel, QLineEdit, QPushButton

def display_date(user_results, user_date):
    date = user_date.text()
    formats = ["%d-%m-%Y", "%d/%m/%Y", "%d-%m-%y", "%d/%m/%y"]

    for fmt in formats:
        try:
            dt_object = datetime.strptime(date, fmt)
            if "%y" in fmt:
                formatted_date = dt_object.strftime("On %d-%m-%y, the day was %A of %B.")
            else:
                formatted_date = dt_object.strftime("On %d-%m-%Y, the day was %A of %B.")
            user_results.setText(formatted_date)
            return
        except ValueError:
            continue

    user_results.setText("Invalid date format. Use DD-MM-YY, or DD/MM/YY.")

def show_info():
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Information)
    msg.setWindowTitle("About Day Finder")
    msg.setText("Day Finder is an application that allows you to input a date (DD-MM-YY or DD/MM/YY)\n"
                "and press SUBMIT. It will display the day of the week corresponding to that date.")
    msg.setStandardButtons(QMessageBox.Ok)
    msg.exec_()

def setup_icon(window):
    """Setup application icon and handle missing file gracefully."""
    icon_relative_path = 'Assets/icon.png'  # Relative path to the icon
    icon_path = os.path.join(os.getcwd(), icon_relative_path)

    if os.path.exists(icon_path):
        window.setWindowIcon(QIcon(icon_path))
    else:
        # Use a default icon or provide a fallback
        default_icon_path = 'Assets/default_icon.png'
        if os.path.exists(default_icon_path):
            window.setWindowIcon(QIcon(default_icon_path))
        else:
            print("Icon file not found. Using default icon.")
            # Optionally set a blank icon or no icon
            window.setWindowIcon(QIcon())

# Configuration
app = QApplication([])
window = QWidget()
window.setGeometry(100, 100, 400, 350)
window.setWindowTitle("Day Finder")

# Set up the icon
setup_icon(window)

# Set up fonts and stylesheet
font_title = QFont('Arial', 18, QFont.Bold)
font_normal = QFont('Arial', 14)
font_bold = QFont('Arial', 14, QFont.Bold)
app.setStyle('Fusion')

window.setStyleSheet("""
    QWidget {
        background-color: yellow;
        border-radius: 10px;
    }
    QLabel {
        color: #333;
    }
    QLineEdit {
        padding: 5px;
        border: 1px solid #ccc;
        border-radius: 5px;
    }
    QPushButton {
        background-color: #007bff;
        color: white;
        padding: 10px;
        border: none;
        border-radius: 5px;
    }
    QPushButton:hover {
        background-color: #0056b3;
    }
    QLabel#user_results {
        font-weight: bold;
        color: #007bff;
    }
""")

# Title
title_label = QLabel("Day Finder by Date")
title_label.setFont(font_title)
title_label.setAlignment(Qt.AlignCenter)

# Today's information
date = datetime.now()
day = date.strftime('%A')
month = date.strftime('%B')
year = date.strftime('%Y')

# Rich text for today's date
today_date = QLabel(
    f"<b>Welcome!</b><br>"
    f"Today is <font color='blue'>{day}</font>, the <font color='green'>{date.day}</font>th day of <font color='red'>{month}</font>, {year}.<br>"
    f"Enjoy your day and let us help you find out what day any given date falls on!"
)
today_date.setFont(font_bold)
today_date.setTextFormat(Qt.RichText)

# Entered Information
user_date = QLineEdit()
user_title = QLabel("Enter your date here: (DD-MM-YY, DD/MM/YY)")
user_title.setFont(font_normal)
user_date.setPlaceholderText("Enter date here...")
user_button = QPushButton("Submit")

# Results
user_results = QLabel()
user_results.setFont(font_normal)
user_results.setObjectName("user_results")

# Layouts
input_layout = QVBoxLayout()
input_layout.addWidget(user_title)
input_layout.addWidget(user_date)
input_layout.addWidget(user_button)
input_layout.addWidget(user_results)
input_layout.setSpacing(10)
input_layout.setContentsMargins(10, 10, 10, 10)

main_layout = QVBoxLayout()
main_layout.addWidget(title_label)
main_layout.addWidget(today_date)
main_layout.addLayout(input_layout)
main_layout.setSpacing(20)
main_layout.setContentsMargins(20, 20, 20, 20)

# Setting Layout
window.setLayout(main_layout)

# Connect Buttons
user_button.clicked.connect(lambda: display_date(user_results, user_date))

# Show information message box
show_info()

# Events
window.show()
app.exec_()
