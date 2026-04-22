import tkinter as tk
from tkinter import messagebox
import ttkbootstrap as ttk 
print("ttkbootstrap installed correctly")

app = ttk.Window()
style = ttk.Style()
#Establecer el tiempo predeterminado para los intervalos de trabajo y descanso
WORK_TIME = 25 * 60
SHORT_BREAK_TIME = 5 * 60
LONG_BREAK_TIME = 15 * 60

class PomodoroTimer:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("300x300")
        self.root.title("Timer")
        self.style = ttk.Style(theme="darkly")
        self.style.theme_use()

        self.timer_label = tk.Label(self.root, text="00:00:00", font=("Helvetica", 40), fg="white", bg="#333333")
        self.timer_label.pack(pady=20)

        self.start_button = ttk.Button(self.root, text="Start", bootstyle="success", command=self.start_timer)
        self.start_button.pack(pady=5)

        self.stop_button = ttk.Button(self.root, text="Stop", bootstyle="danger", command=self.stop_timer,
                                      state=tk.DISABLED)
        self.stop_button.pack(pady=5)

        self.work_time, self.break_time = WORK_TIME, SHORT_BREAK_TIME
        self.is_work_time, self.pomodoros_completed, self.is_running = True, 0, False

        self.root.mainloop()

    def start_timer(self):
        self.start_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)
        self.is_running = True
        self.update_timer()
    
    def stop_timer(self):
        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)
        self.is_running = False

    def update_timer(self):
        if self.is_running:
            if self.is_work_time:
                self.work_time -= 1
                if self.work_time == 0:
                    self.is_work_time = False
                    self.pomodoros_completed += 1
                    self.break_time = LONG_BREAK_TIME if self.pomodoros_completed % 4 == 0 else SHORT_BREAK_TIME
                    messagebox.showinfo("Buen trabajo!" if self.pomodoros_completed % 4 == 0
                                        else "Buen trabajo!", "Toma un descanso y aclara tu mente."
                                        if self.pomodoros_completed % 4 == 0
                                        else "Toma un descanso corto y estira tus piernas!")
            else:
                self.break_time -= 1
                if self.break_time == 0:
                    self.is_work_time, self.work_time = True, WORK_TIME
                    messagebox.showinfo( "¡Vamos a trabajar!")        
            minutes, seconds = divmod(self.work_time if self.is_work_time else self.break_time, 60)
            self.timer_label.config(text="{:02d}:{:02d}".format(minutes, seconds))
            self.root.after(1000, self.update_timer)

PomodoroTimer()