"""
SkillCraft Task 04 - Consent-Based Keystroke Logger

Safety design:
- Captures keystrokes ONLY while the user types in this app's text box.
- Does not monitor other applications or run in the background.
- Shows a clear notice and lets the user save the text they entered.
"""

import tkinter as tk
from tkinter import filedialog, messagebox
from datetime import datetime
from pathlib import Path


class ConsentKeyLogger:
    def __init__(self, root):
        self.root = root
        self.root.title("Consent-Based Keystroke Logger")
        self.root.geometry("760x540")
        self.root.minsize(620, 440)

        heading = tk.Label(
            root, text="Consent-Based Keystroke Logger",
            font=("Segoe UI", 18, "bold")
        )
        heading.pack(pady=(16, 6))

        notice = (
            "Demo mode: this app records only what you type in the box below. "
            "It does not capture keystrokes from other apps."
        )
        tk.Label(
            root, text=notice, wraplength=700, justify="center",
            fg="#333333"
        ).pack(padx=20, pady=(0, 12))

        self.consent = tk.BooleanVar(value=False)
        tk.Checkbutton(
            root,
            text="I understand and consent to recording my typing in this app.",
            variable=self.consent,
            command=self.update_state
        ).pack(pady=(0, 10))

        self.text_box = tk.Text(root, height=14, wrap="word", state="disabled",
                                font=("Consolas", 11), undo=True)
        self.text_box.pack(fill="both", expand=True, padx=20, pady=6)
        self.text_box.bind("<KeyPress>", self.on_keypress)

        controls = tk.Frame(root)
        controls.pack(pady=12)

        self.start_button = tk.Button(
            controls, text="Start demo", command=self.start, state="disabled",
            width=14
        )
        self.start_button.pack(side="left", padx=5)

        self.stop_button = tk.Button(
            controls, text="Stop", command=self.stop, state="disabled", width=14
        )
        self.stop_button.pack(side="left", padx=5)

        self.save_button = tk.Button(
            controls, text="Save log…", command=self.save_log, width=14
        )
        self.save_button.pack(side="left", padx=5)

        self.clear_button = tk.Button(
            controls, text="Clear", command=self.clear, width=14
        )
        self.clear_button.pack(side="left", padx=5)

        self.status = tk.StringVar(value="Status: consent required")
        tk.Label(root, textvariable=self.status, anchor="w").pack(
            fill="x", padx=20, pady=(0, 12)
        )
        self.active = False

    def update_state(self):
        if not self.active:
            self.start_button.config(state="normal" if self.consent.get() else "disabled")
            self.status.set("Status: ready" if self.consent.get()
                            else "Status: consent required")

    def start(self):
        if not self.consent.get():
            messagebox.showwarning("Consent required", "Please check the consent box first.")
            return
        self.active = True
        self.text_box.config(state="normal")
        self.text_box.focus_set()
        self.start_button.config(state="disabled")
        self.stop_button.config(state="normal")
        self.status.set("Status: recording in this app only")

    def stop(self):
        self.active = False
        self.text_box.config(state="disabled")
        self.start_button.config(state="normal" if self.consent.get() else "disabled")
        self.stop_button.config(state="disabled")
        self.status.set("Status: stopped")

    def on_keypress(self, event):
        # This handler is attached only to the text box in this application.
        if not self.active:
            return "break"
        return None

    def save_log(self):
        content = self.text_box.get("1.0", "end-1c")
        if not content:
            messagebox.showinfo("Nothing to save", "Type something in the demo box first.")
            return
        default_name = f"keystroke_log_{datetime.now():%Y%m%d_%H%M%S}.txt"
        path = filedialog.asksaveasfilename(
            title="Save your demo log",
            defaultextension=".txt",
            initialfile=default_name,
            filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
        )
        if path:
            Path(path).write_text(
                "Consent-Based Keystroke Logger Demo\n"
                f"Saved: {datetime.now():%Y-%m-%d %H:%M:%S}\n"
                "Scope: text entered only in this application.\n\n"
                + content + "\n",
                encoding="utf-8"
            )
            messagebox.showinfo("Saved", f"Log saved to:\n{path}")

    def clear(self):
        if messagebox.askyesno("Clear text", "Clear the text entered in this demo?"):
            was_active = self.active
            self.text_box.config(state="normal")
            self.text_box.delete("1.0", "end")
            if not was_active:
                self.text_box.config(state="disabled")


if __name__ == "__main__":
    root = tk.Tk()
    app = ConsentKeyLogger(root)
    root.mainloop()
