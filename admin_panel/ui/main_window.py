from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QListWidget
from admin_panel.db import Database
from admin_panel.ui.add_post import AddPostWindow

class AdminPanel(QWidget):
    """Main admin panel window to manage posts."""
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Wee-CMS Admin Panel")
        self.setGeometry(200, 200, 600, 400)

        self.layout = QVBoxLayout()
        self.list_widget = QListWidget()
        self.load_posts()

        self.add_button = QPushButton("Add Post")
        self.delete_button = QPushButton("Delete Post")

        self.layout.addWidget(self.list_widget)
        self.layout.addWidget(self.add_button)
        self.layout.addWidget(self.delete_button)

        self.setLayout(self.layout)

        self.add_button.clicked.connect(self.open_add_post_window)
        self.delete_button.clicked.connect(self.delete_post)

    def load_posts(self):
        """Loads posts from SQLite3."""
        db = Database()
        posts = db.fetch_all("SELECT id, title FROM posts")
        for post in posts:
            self.list_widget.addItem(f"{post[0]} - {post[1]}")

    def open_add_post_window(self):
        """Opens add post window."""
        self.add_post_window = AddPostWindow()
        self.add_post_window.show()

    def delete_post(self):
        """Deletes selected post."""
        selected_item = self.list_widget.currentItem()
        if selected_item:
            post_id = selected_item.text().split(" - ")[0]
            db = Database()
            db.execute("DELETE FROM posts WHERE id = ?", (post_id,))
            self.list_widget.takeItem(self.list_widget.currentRow())

if __name__ == "__main__":
    app = QApplication([])
    window = AdminPanel()
    window.show()
    app.exec()