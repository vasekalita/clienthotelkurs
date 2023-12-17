import sys
import sqlite3
from PyQt6.QtWidgets import QApplication, QMainWindow, QDialog, QVBoxLayout, QTextEdit, QPushButton
from PyQt6.QtGui import QFont
from kursqtvis import Ui_MainWindow

class FeedbackDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Отзывы")
        self.setFixedSize(400, 200)

        layout = QVBoxLayout(self)

        self.feedback_label = QTextEdit(self)
        self.feedback_label.setReadOnly(True)
        font = QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.feedback_label.setFont(font)
        self.feedback_label.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.feedback_label.setObjectName("feedback_label")
        layout.addWidget(self.feedback_label)

        back_button = QPushButton("Назад", self)
        back_button.clicked.connect(self.close)
        layout.addWidget(back_button)

    def set_feedback(self, feedback):
        self.feedback_label.setPlainText(feedback)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.feedback_first.clicked.connect(self.show_feedback_dialog_first)
        self.ui.feedback_second.clicked.connect(self.show_feedback_dialog_second)
        self.ui.feedback_third.clicked.connect(self.show_feedback_dialog_third)
        self.ui.feedback_fourth.clicked.connect(self.show_feedback_dialog_fourth)

        # Подключение к базе данных
        self.db_connection = sqlite3.connect("hotel.db")
        self.db_cursor = self.db_connection.cursor()

    def show_feedback_dialog_first(self):
        feedback_dialog = FeedbackDialog(self)
        feedback_dialog.setModal(True)

        self.db_cursor.execute("SELECT review_text FROM reviews WHERE room_id = 1")
        feedback = self.db_cursor.fetchall()
        if feedback:
            feedback_text = "\n\n".join([f[0] for f in feedback])
            feedback_dialog.set_feedback(feedback_text)
        else:
            feedback_dialog.set_feedback("Отзывы для 1го номера не найдены.")

        feedback_dialog.exec()

    def show_feedback_dialog_second(self):
        feedback_dialog = FeedbackDialog(self)
        feedback_dialog.setModal(True)

        self.db_cursor.execute("SELECT review_text FROM reviews WHERE room_id = 2")
        feedback = self.db_cursor.fetchall()
        if feedback:
            feedback_text = "\n\n".join([f[0] for f in feedback])
            feedback_dialog.set_feedback(feedback_text)
        else:
            feedback_dialog.set_feedback("Отзывы для 2го номера не найдены.")

        feedback_dialog.exec()

    def show_feedback_dialog_third(self):
        feedback_dialog = FeedbackDialog(self)
        feedback_dialog.setModal(True)

        self.db_cursor.execute("SELECT review_text FROM reviews WHERE room_id = 3")
        feedback = self.db_cursor.fetchall()
        if feedback:
            feedback_text = "\n\n".join([f[0] for f in feedback])
            feedback_dialog.set_feedback(feedback_text)
        else:
            feedback_dialog.set_feedback("Отзывы для 3го номера не найдены.")

        feedback_dialog.exec()

    def show_feedback_dialog_fourth(self):
        feedback_dialog = FeedbackDialog(self)
        feedback_dialog.setModal(True)

        self.db_cursor.execute("SELECT review_text FROM reviews WHERE room_id = 4")
        feedback = self.db_cursor.fetchall()
        if feedback:
            feedback_text = "\n\n".join([f[0] for f in feedback])
            feedback_dialog.set_feedback(feedback_text)
        else:
            feedback_dialog.set_feedback("Отзывы для 4го номера не найдены.")

        feedback_dialog.exec()

    def __del__(self):
        self.db_cursor.close()
        self.db_connection.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())