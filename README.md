# SkillCraft Task 04 – Basic Keylogger

## 📌 Project Overview

This project is developed as part of the **SkillCraft Technology Python Development Internship – Task 04**.

The objective is to demonstrate basic keystroke event handling using Python and record user-entered text to a file. This project uses a simple graphical user interface (GUI) built with Tkinter.

For privacy and safety, the application records text only when the user types inside its own text box after providing consent. It does not monitor keystrokes in other applications or run secretly in the background.

## 🎯 Objectives

- Understand keyboard event handling in Python.
- Develop a simple GUI using Tkinter.
- Capture text entered within the application.
- Save user-entered text to a `.txt` file.
- Practice file handling and event-driven programming.

## 🛠️ Technologies Used

- **Programming Language:** Python
- **GUI Library:** Tkinter
- **File Handling:** Python file operations
- **Modules:** `datetime`, `pathlib`

## ✨ Features

- Simple and user-friendly graphical interface.
- Explicit consent before recording starts.
- Start and stop recording controls.
- Captures typing only inside the application.
- Saves the entered text to a text file.
- Clear button to remove entered text.
- Privacy-conscious design.

## 📂 Project Structure

```text
SkillCraft_Task_04_Consent_Based_Keylogger/
│
├── keylogger_demo.py
├── keystroke_log_20261014_200610.txt
├── README.md
└── requirements.txt
```

**File descriptions:**
- `keylogger_demo.py` – Main Python application.
- `keystroke_log_20261014_200610.txt` – Sample output log generated during testing.
- `README.md` – Project documentation.
- `requirements.txt` – Dependency information.

## ⚙️ Requirements

- Python 3.10 or newer recommended.
- Tkinter, generally included with standard Python installations.
- No additional third-party packages are required.

## ▶️ How to Run

1. Install Python from [python.org](https://www.python.org/downloads/).
2. Download or clone this repository.
3. Open Command Prompt or a terminal in the project folder.
4. Run the following command:

```bash
py keylogger_demo.py
```

If the `py` command is unavailable, use:

```bash
python keylogger_demo.py
```

## 📝 How to Use

1. Launch the application.
2. Check the consent checkbox.
3. Click **Start demo**.
4. Type sample text into the application's text box.
5. Click **Stop** when finished.
6. Click **Save log…** to save the text to a `.txt` file.
7. Open the saved file to verify the output.

## 📚 Learning Outcomes

- Understanding keyboard events and GUI programming.
- Working with Python file handling.
- Using standard Python libraries.
- Building a simple desktop application.
- Applying consent and privacy principles in software development.


