# The M-List - Movie Recommendation System

## Introduction
The M-List is a software application designed to recommend the latest movies and shows. It simplifies the overwhelming task of choosing entertainment options by curating a personalized selection. Built using **Python, MySQL, and tkinter**, the project provides a functional and user-friendly Graphical User Interface (GUI) for seamless interaction.

## Features
- **User Management**: Admins can create and manage user accounts with different access levels.
- **Movies Database**: Stores details like rank, name, genre, director, cast, and ratings.
- **Search & Retrieval**: Users can search for movies based on various criteria (genre, director, cast, etc.).
- **Wish List**: Users can save movies they wish to watch later.
- **Graphical User Interface (GUI)**: A user-friendly and interactive UI using tkinter.

## System Requirements
### Hardware
- Minimum **2 GB RAM** and **10 GB free disk space**
- **Processor**: At least **2 cores, 2 GHz clock speed**
- Compatible with **Windows, macOS, or Linux**

### Software
- **Python 3.8+**
- **MySQL 5.7+**
- **Text Editor (VS Code, Python IDLE, etc.)**

## Database Design
The project consists of two primary databases:

### 1. Admin Database
Stores user credentials and their respective wish lists.
- `adminT` Table: Stores user ID, email, and passwords.
- `<username>WL` Table: Stores wish lists unique to each user.

### 2. Movies Database
Stores and manages all movie-related data, including:
- Movie name
- Genre
- Director
- Cast
- Ratings
- Box Office collection

## Application Workflow
1. **Login System** (`login.py`)
   - Users enter credentials via a tkinter-based GUI.
   - Credentials are validated using `MoviesDat.py`.
   - Admins are redirected to `admin.py`, regular users to `user.py`.

2. **Admin Panel** (`admin.py`)
   - Add or remove users.
   - Manage movies (add/update/delete movies from the database).
   - View the number of users in the system.

3. **User Interface** (`user.py`)
   - Search movies based on category (Genre, Director, Cast, etc.).
   - Add movies to a personal wish list.
   - View and remove movies from the wish list.

4. **Database Operations** (`MoviesDat.py`)
   - Acts as a bridge between MySQL and Python.
   - Handles retrieval, updates, and storage of data.

## Installation & Setup
### 1. Clone the Repository
```bash
   git clone https://github.com/your-username/m-list.git
   cd m-list
```

### 2. Install Dependencies
Ensure you have Python installed, then install the required packages:
```bash
   pip install mysql-connector-python tkinter
```

### 3. Configure MySQL Database
- Create a MySQL database and import the provided schema.
- Update database credentials in `MoviesDat.py`.

### 4. Run the Application
```bash
   python login.py
```


## Conclusion
The M-List successfully integrates Python, MySQL, and a GUI to create a smooth and personalized movie recommendation experience. With an intuitive interface and a secure database, the application provides an efficient way for users to discover and organize their favorite movies.

## References
- [Python Tutorial](https://pythontutorial.net)
- [GeeksforGeeks](https://geeksforgeeks.org)
- [The Movie DB](https://themoviedb.org)
