from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QListWidget, QLineEdit, QTextEdit
import sys

class AdminPanel(QWidget):
    """Main admin panel window to manage posts."""
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Wee-CMS Admin Panel")
        self.setGeometry(200, 200, 600, 400)

        self.layout = QVBoxLayout()

        # Lista postów
        self.list_widget = QListWidget()

        # Pole do wpisywania tytułu
        self.title_input = QLineEdit()
        self.title_input.setPlaceholderText("Enter post title")

        # Pole do wpisywania treści
        self.content_input = QTextEdit()
        self.content_input.setPlaceholderText("Enter post content")

        # Przycisk do dodawania postu
        self.add_button = QPushButton("Add Post")
        self.add_button.clicked.connect(self.add_post)

        # Dodanie widgetów do layoutu
        self.layout.addWidget(self.list_widget)
        self.layout.addWidget(self.title_input)
        self.layout.addWidget(self.content_input)
        self.layout.addWidget(self.add_button)

        self.setLayout(self.layout)

    def add_post(self):
        """Dodaje post do listy."""
        title = self.title_input.text()
        content = self.content_input.toPlainText()

        if title and content:
            self.list_widget.addItem(f"{title}: {content}")
            self.title_input.clear()
            self.content_input.clear()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AdminPanel()
    window.show()
    app.exec()