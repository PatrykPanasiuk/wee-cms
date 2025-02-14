# Wee-CMS

Wee-CMS is an open-source, lightweight content management system (CMS) designed for simplicity and efficiency. It features a FastAPI backend with SQLite3 for data storage and a PyQt6-based desktop admin panel for managing content. The project is minimalistic, focusing purely on core functionalities.

## Features

- **FastAPI Backend**: A simple REST API for handling content.
- **SQLite3 Database**: Lightweight and easy-to-use database.
- **PyQt6 Admin Panel**: A basic desktop application for managing content.
- **CRUD Functionality**: Create, Read, Update, and Delete operations for posts.
- **Modular Structure**: Clean and organized codebase for easy maintenance.

## Installation

### Prerequisites
- Python 3.10 or newer
- `pip` installed
- SQLite3 installed and accessible from the command line

### Setup

After cloning the repository and installing dependencies, the database must be initialized before running the application. The setup follows these steps:

1. **Clone the repository** and navigate into the project directory:
   ```bash
   git clone https://github.com/yourusername/wee-cms.git
   cd wee-cms
   ```

2. **Install required dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Initialize the SQLite3 database**:
   ```bash
   python -m backend.init_db
   ```

4. **Start the FastAPI backend**:
   ```bash
   uvicorn backend.main:app --reload
   ```

5. **Access API documentation**:
   Open the browser and go to:
   ```
   http://127.0.0.1:8000/docs
   ```

6. **Run the PyQt6 admin panel**:
   ```bash
   cd admin_panel
   python main.py
   ```

## Project Structure

```
wee-cms/
│── backend/                 # FastAPI Backend
│   ├── __init__.py
│   ├── database.py          # SQLite3 setup
│   ├── models.py            # Database models
│   ├── crud.py              # CRUD operations
│   ├── routes.py            # API routes
│   ├── main.py              # FastAPI entry point
│   ├── init_db.py           # Database initialization script
│
│── database/                # SQLite3 database storage
│   ├── data.db              # SQLite3 database file
│
│── admin_panel/             # PyQt6 Admin Panel
│   ├── __init__.py
│   ├── main.py              # GUI for managing content
│
│── frontend/                # Optional frontend directory
│
│── .gitignore               # Ignore unnecessary files
│── requirements.txt         # Project dependencies
│── README.md                # Project documentation
```

## API Endpoints

| Method | Endpoint  | Description |
|--------|----------|-------------|
| GET    | `/posts` | Retrieve all posts |
| POST   | `/posts` | Create a new post |
| GET    | `/posts/{id}` | Retrieve a specific post |
| DELETE | `/posts/{id}` | Delete a post |

## Is This Really a CMS?

A CMS typically includes advanced content management functionalities, such as:
- User authentication and role-based access control
- Rich-text editing and media management
- Frontend rendering for public content display

Wee-CMS currently provides only basic CRUD operations through an API and a minimal admin panel. While it serves as a content management tool, it lacks full-fledged CMS features like WordPress or Drupal. However, it can be expanded with additional functionalities over time.

## Contributing

Contributions are welcome. If you would like to contribute, follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature-branch`)
3. Commit your changes (`git commit -m "Add new feature"`)
4. Push to the branch (`git push origin feature-branch`)
5. Open a pull request

## License

## License

Wee-CMS is licensed under the GNU General Public License v3 (GPLv3). This means:
- The project is open source and can be freely modified and distributed.
- Any modified versions must also be released under the GPL license.
- It cannot be used in proprietary software.

For more details, see the [LICENSE](LICENSE) file.

