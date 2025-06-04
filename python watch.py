import tkinter as tk

class Stopwatch:
    def _init_(self, root):
        self.root = root
        self.root.title("Stopwatch")

        self.time = 0
        self.running = False

        self.label = tk.Label(root, text="00:00:00", font=("Helvetica", 48))
        self.label.pack()

        btn_frame = tk.Frame(root)
        btn_frame.pack()

        self.start_btn = tk.Button(btn_frame, text="Start", command=self.start)
        self.start_btn.grid(row=0, column=0, padx=5)

        self.stop_btn = tk.Button(btn_frame, text="Stop", command=self.stop)
        self.stop_btn.grid(row=0, column=1, padx=5)

        self.reset_btn = tk.Button(btn_frame, text="Reset", command=self.reset)
        self.reset_btn.grid(row=0, column=2, padx=5)

    def update(self):
        if self.running:
            self.time += 1
            minutes, seconds = divmod(self.time, 60)
            hours, minutes = divmod(minutes, 60)
            self.label.config(text=f"{hours:02}:{minutes:02}:{seconds:02}")
            self.root.after(1000, self.update)

    def start(self):
        if not self.running:
            self.running = True
            self.update()

    def stop(self):
        self.running = False

    def reset(self):
        self.time = 0
        self.running = False
        self.label.config(text="00:00:00")

root = tk.Tk()
sw = Stopwatch(root)
root.mainloop()