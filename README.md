# University Management System

This repository contains a University Management System implemented in both Command-Line Interface (CLI) and Graphical User Interface (GUI) formats. The project demonstrates core Python programming, data management, and user interface development skills.

---

## 📁 Project Structure


```
CLI App/
    Admins.py
    DataFile.py
    Students.py
    Subjects.py
    UniApp.py

GUI App/
    DataFile.py
    home.py
    student_view.py
    Subjects.py
```


---

## Features

- **Student and Subject Management:** Add, update, and view students and subjects.
- **Admin Controls:** CLI app includes admin functionalities for managing university data.
- **Data Persistence:** Data is stored and managed using custom Python modules.
- **User Interfaces:** 
  - CLI App for terminal-based interaction.
  - GUI App for a user-friendly graphical experience.

---

## Technologies Used

- Python 3
- Tkinter (for GUI)
- Object-Oriented Programming
- File I/O for Data Storage

---

## Folders Overview

### CLI App

A terminal-based application for managing university data. Key modules:
- `Admins.py`: Admin functionalities.
- `Students.py`: Student management.
- `Subjects.py`: Subject management.
- `DataFile.py`: Data storage and retrieval.
- `UniApp.py`: Main entry point for the CLI application.

### GUI App

A graphical application using Tkinter for enhanced user experience. Key modules:
- `home.py`: Main window and navigation.
- `student_view.py`: Student management interface.
- `Subjects.py`: Subject management interface.
- `DataFile.py`: Data storage and retrieval.

---

## How to Run

### CLI App

```sh
cd "CLI App"
python UniApp.py
```
## GUI App

```sh
cd "GUI App"
python home.py
```