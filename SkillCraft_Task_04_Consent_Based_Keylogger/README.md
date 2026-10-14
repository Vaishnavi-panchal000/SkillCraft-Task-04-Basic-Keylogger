# SkillCraft Task 04 — Consent-Based Keystroke Logger

## Overview
This project demonstrates basic keystroke-event handling in Python with a Tkinter GUI. It records text only when the user types inside this application's text box after explicitly giving consent, and lets the user save that text to a `.txt` file.

## Safety and privacy
- Does **not** monitor keystrokes in other applications.
- Does **not** run invisibly or in the background.
- Requires an explicit consent checkbox before recording starts.
- Saves only when the user chooses **Save log…**.

## Technologies
- Python 3
- Tkinter (Python GUI library)
- `datetime` and `pathlib` (standard library)

## Requirements
- Python 3.10 or newer recommended
- Tkinter (usually included with standard Windows Python installations)

No third-party packages are required.

## Run on Windows
1. Install Python from https://www.python.org/downloads/ if needed.
2. Open Command Prompt in this project folder.
3. Run:

```bash
py keylogger_demo.py
```

If `py` is unavailable, try:

```bash
python keylogger_demo.py
```

## How to use
1. Open the application.
2. Check the consent box.
3. Click **Start demo**.
4. Type in the application's text box only.
5. Click **Stop** when finished.
6. Click **Save log…** to save the text you entered.
7. Open the saved `.txt` file to verify the output.

## Project structure
```text
SkillCraft_Task_04_Consent_Based_Keylogger/
├── keylogger_demo.py
├── README.md
└── requirements.txt
```

## Learning outcomes
- Handling keyboard events in a GUI
- Building a simple Python desktop interface
- Saving user-provided text to a file
- Applying consent and privacy boundaries in a logging demo

## Disclaimer
For educational demonstration only. Use only with informed consent. This project intentionally does not implement system-wide keylogging.
