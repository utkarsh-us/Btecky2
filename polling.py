import tkinter as tk
from tkinter import messagebox
import sqlite3

class PollingSystem:
    def __init__(self, master):
        self.master = master
        self.master.title("Advanced Polling System")

        # Create a database (SQLite in this example)
        self.conn = sqlite3.connect("polling_system.db")
        self.create_table()

        # Create GUI components
        self.question_label = tk.Label(master, text="What is your favorite programming language?")
        self.question_label.pack(pady=10)

        self.languages = ["Python", "Java", "JavaScript", "C++", "Other"]

        self.selected_language = tk.StringVar()
        self.selected_language.set(self.languages[0])

        for language in self.languages:
            language_radio = tk.Radiobutton(master, text=language, variable=self.selected_language, value=language)
            language_radio.pack()

        self.vote_button = tk.Button(master, text="Vote", command=self.vote)
        self.vote_button.pack(pady=10)

        self.show_results_button = tk.Button(master, text="Show Results", command=self.show_results)
        self.show_results_button.pack(pady=10)

    def create_table(self):
        cursor = self.conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS poll (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                language TEXT NOT NULL
            )
        ''')
        self.conn.commit()

    def vote(self):
        language = self.selected_language.get()
        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO poll (language) VALUES (?)", (language,))
        self.conn.commit()
        messagebox.showinfo("Success", "Your vote has been recorded!")

    def show_results(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT language, COUNT(*) FROM poll GROUP BY language")
        results = cursor.fetchall()

        result_str = "\n".join([f"{language}: {count}" for language, count in results])

        messagebox.showinfo("Poll Results", result_str)


def main():
    root = tk.Tk()
    app = PollingSystem(root)
    root.mainloop()


if __name__ == "__main__":
    main()
