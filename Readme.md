# 👤 Contact Manager App Using Linked List Data Structure (Python Implementation)

## 📑 Table of Contents
- [Description](#description)
- [Features](#features)
- [Objectives](#objectives)
- [Methodology](#methodology)
- [Technologies Used](#technologies-used)
- [Setup/Installation](#setupinstallation)
- [Usage](#usage)
- [Code Structure](#code-structure)
- [Example Output](#example-output)
- [Team Members](#team-members)
- [Contributions](#contributions)
- [License](#license)
- [References](#references)

---

## ✏️ Description
This is a **multi-interface Contact Manager application** implemented in Python, utilizing the **Linked List** data structure for dynamic contact management. The project includes both a **Graphical User Interface (GUI)** using Tkinter and a **Command-Line Interface (CLI)**. It demonstrates linked list operations for adding, deleting, searching, and listing contacts while emphasizing Python's flexibility for cross-interface development.

---

## ✨ Features
### **Core Functionalities**
- **Add Contact**: Insert a new contact (name and phone number).
- **Delete Contact**: Remove a contact by name.
- **Search Contact**: Find a contact by name and display details.
- **List All Contacts**: Display all contacts in the linked list.

### **GUI-Specific Features**
- Intuitive Tkinter-based interface with buttons and input fields.
- Real-time updates of contact list after each operation.

### **CLI-Specific Features**
- Menu-driven interface for all operations.
- Clear text-based output and error handling.

---

## 🚀 Objectives
1. Implement CRUD operations using linked lists in Python.
2. Compare and contrast GUI and CLI development in Python.
3. Demonstrate dynamic data management with linked lists.
4. Ensure seamless integration of front-end and back-end logic.
5. Highlight the advantages of linked lists over static lists in Python.

---

## ⚒️ Methodology
### Why Linked Lists in Python?
- **Dynamic Memory Management**: Python's flexibility allows efficient node-based operations without manual memory management.
- **Modularity**: Separation of linked list logic (backend) from UI (frontend) for maintainability.
- **Traversal Efficiency**: Linked lists provide O(1) insertion/deletion compared to O(n) for lists in some cases.

### Implementation Highlights
- **Node Structure**: Each contact is stored as a `Node` object with `data` (name, phone) and `next` pointer.
- **GUI (Tkinter)**: Event-driven interface with buttons, entry fields, and listboxes.
- **CLI**: Simple text-based menu using input validation and loops.
- **Edge Cases**: Handle empty lists, duplicate entries, and invalid inputs gracefully.

---

## 💻 Technologies Used
- **Programming Language**: Python 3.8+
- **GUI Framework**: Tkinter (built-in Python library)
- **CLI**: Standard Python `input()` and `print()` functions
- **Testing**: Pytest (unit tests for linked list operations)
- **Code Editor**: VS Code (Recoomended), PyCharm, or any Python IDE

---

## 📦 Setup/Installation
1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/contact-manager-python.git
   cd contact-manager-python
   ```

2. **Install dependencies** (if any):
   ```bash
   pip install pytest  # For testing
   ```

3. **Run the application**:
   - **GUI**:
     ```bash
     python app.py
     ```
   - **CLI**:
     ```bash
     python main.py
     ```

---

## 🚗 Usage
### **GUI Workflow**
1. Launch `app.py` to open the Tkinter interface.
2. Use buttons to **Add**, **Delete**, **Search**, or **List** contacts.
3. Real-time updates in the contact list display.

### **CLI Workflow**
1. Run `main.py` to access the menu-driven interface.
2. Choose options via numbered prompts:
   ```
   1. Add Contact
   2. Delete Contact
   3. Search Contact
   4. List All Contacts
   5. Exit
   ```

---

## 👷 Code Structure
```plaintext
.
├── src/
│   └── linkedlist.py  # Core linked list implementation
├── app.py             # Tkinter-based GUI
├── main.py            # Command-line interface
├── LICENSE            # MIT License
└── README.md          # Project documentation
```

### Key Components
- **`linkedlist.py`**: Contains the `Contact` and `LinkedList` classes with core operations.
- **`app.py`**: Implements the Tkinter interface, linking to `main.py` for backend logic.
- **`main.py`**: Implements the text-based menu system, using `main.py` for operations.

---

## Example Output
### **CLI Example**
```bash
Welcome to Contact Manager CLI!
-------------------------------
1. Add Contact
2. Delete Contact
3. Search Contact
4. List All Contacts
5. Exit

Enter choice: 1
Enter name: Alice
Enter phone: 123-456-7890
Contact added!

Enter choice: 4
Contacts:
1. Alice - 123-456-7890

Enter choice: 3
Enter name to search: Alice
Found: Alice - 123-456-7890

Enter choice: 2
Enter name to delete: Alice
Contact deleted!

Enter choice: 4
No contacts found.
```

### **GUI Screenshot**
![GUI Screenshot](docs/gui-screenshot.png) *(Example placeholder image)*

---

## 👥 Team Members
Add your name and your role!!(Use the Roles as a guide)
| Name          | Role                          |
|---------------|-------------------------------|
| Flavio Sobbin | Documentation & Code Review   |
|      | GUI Development (Tkinter)     |
|    | CLI Development & Testing     |
| | Project Lead & Core Logic |


---

## 👥✨ Contributions
Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a new branch: `git checkout -b feature/your-feature`.
3. Develop in either the GUI or CLI (or both!).
5. Submit a pull request.

Report bugs or suggest features via [GitHub Issues](https://github.com/your-username/contact-manager-python/issues).

---

## ©️ License
This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

---

## 📖 References
- [Tkinter Documentation](https://docs.python.org/3/library/tkinter.html)
- [Python Data Structures Tutorial](https://www.w3schools.com/python/python_lists.asp)
