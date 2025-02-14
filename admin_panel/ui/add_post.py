from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QTextEdit, QPushButton
from admin_panel.db import Database

class AddPostWindow(QWidget):
    """Window for adding new posts."""
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Add New Post")
        self.setGeometry(300, 300, 400, 300)

        self.layout = QVBoxLayout()

        self.title_label = QLabel("Title:")
        self.title_input = QLineEdit()

        self.content_label = QLabel("Content:")
        self.content_input = QTextEdit()

        self.submit_button = QPushButton("Submit")
        self.submit_button.clicked.connect(self.add_post)

        self.layout.addWidget(self.title_label)
        self.layout.addWidget(self.title_input)
        self.layout.addWidget(self.content_label)
        self.layout.addWidget(self.content_input)
        self.layout.addWidget(self.submit_button)

        self.setLayout(self.layout)

    def add_post(self):
        """Inserts new post into database."""
        title = self.title_input.text()
        content = self.content_input.toPlainText()

        db = Database()
        conn = db.get_connection()
        if conn:
            with conn.cursor() as cursor:
                cursor.execute("INSERT INTO posts (title, content) VALUES (%s, %s)", (title, content))
                conn.commit()
        self.close()