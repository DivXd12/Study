import tkinter as tk
from tkinter import messagebox

class DiagnosticApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Diagnostic Medical Avansat")
        self.root.geometry("550x420")

        self.frame = tk.Frame(root)
        self.frame.pack(expand=True, fill="both", padx=20, pady=20)

        self.progress_label = tk.Label(self.frame, text="", font=("Arial", 10))
        self.progress_label.pack(anchor="e")

        self.question_label = tk.Label(self.frame, text="", font=("Arial", 16), wraplength=500)
        self.question_label.pack(pady=30)

        self.btn_frame = tk.Frame(self.frame)
        self.btn_frame.pack()

        self.btn_yes = tk.Button(self.btn_frame, text="DA", width=12, height=2,
                                 command=lambda: self.answer(True))
        self.btn_yes.pack(side="left", padx=10)

        self.btn_no = tk.Button(self.btn_frame, text="NU", width=12, height=2,
                                command=lambda: self.answer(False))
        self.btn_no.pack(side="right", padx=10)

        self.control_frame = tk.Frame(self.frame)
        self.control_frame.pack(pady=20)

        self.back_button = tk.Button(self.control_frame, text="Înapoi", command=self.go_back)
        self.back_button.pack(side="left", padx=10)

        self.reset_button = tk.Button(self.control_frame, text="Restart", command=self.start)
        self.reset_button.pack(side="right", padx=10)

        self.start()

    def start(self):
        self.step = 0
        self.history = []

        self.weights = {
            "Raceala": 1,
            "Gripa": 1,
            "COVID-19": 1,
            "Alergie": 1,
            "Bronsita": 1,
            "Pneumonie": 1
        }

        self.questions = [
            ("Ai febră?", "febra"),
            ("Febra este peste 38°C?", "febra_mare"),
            ("Ai tuse?", "tuse"),
            ("Tusea este productivă (cu mucus)?", "tuse_productiva"),
            ("Ai dificultăți de respirație?", "respiratie"),
            ("Ai dureri musculare?", "dureri"),
            ("Ai pierdut gustul sau mirosul?", "miros"),
            ("Ai strănut și ochi iritați?", "alergie")
        ]

        self.update_question()

    def update_question(self):
        if self.step < len(self.questions):
            text, _ = self.questions[self.step]
            self.question_label.config(text=text)
            self.progress_label.config(text=f"Pasul {self.step+1} / {len(self.questions)}")
        else:
            self.show_result()

    def answer(self, value):
        _, key = self.questions[self.step]
        self.history.append((key, value))

        if key == "febra":
            if value:
                self.weights["Gripa"] += 2
                self.weights["COVID-19"] += 2
                self.weights["Pneumonie"] += 2
            else:
                self.weights["Alergie"] += 2

        elif key == "febra_mare":
            if value:
                self.weights["Pneumonie"] += 3
                self.weights["Gripa"] += 2
            else:
                self.weights["Raceala"] += 2

        elif key == "tuse":
            if value:
                self.weights["Bronsita"] += 2
                self.weights["Pneumonie"] += 2

        elif key == "tuse_productiva":
            if value:
                self.weights["Bronsita"] += 3
                self.weights["Pneumonie"] += 2

        elif key == "respiratie":
            if value:
                self.weights["Pneumonie"] += 4
                self.weights["COVID-19"] += 2

        elif key == "dureri":
            if value:
                self.weights["Gripa"] += 3

        elif key == "miros":
            if value:
                self.weights["COVID-19"] += 5

        elif key == "alergie":
            if value:
                self.weights["Alergie"] += 4

        self.step += 1
        self.update_question()

    def go_back(self):
        if self.step > 0:
            self.step -= 1
            self.history.pop()
            self.start()

    def show_result(self):
        total = sum(self.weights.values())

        probabilities = {
            k: round((v / total) * 100, 2)
            for k, v in self.weights.items()
        }

        best = max(probabilities, key=probabilities.get)

        result_text = f"Diagnostic probabil: {best}\n\nProbabilități:\n"
        for k, v in sorted(probabilities.items(), key=lambda x: -x[1]):
            result_text += f"{k}: {v}%\n"

        result_text += "\n(Acesta este doar un model educațional)"

        messagebox.showinfo("Rezultat", result_text)
        self.start()


if __name__ == "__main__":
    root = tk.Tk()
    app = DiagnosticApp(root)
    root.mainloop()