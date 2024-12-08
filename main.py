import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

def draw_window(minutes, color="red", speed=1, font_f="Arial"):
    total_sec = minutes * 60
    total_hour = minutes // 60 if minutes % 60 == 0 else 0
    if speed == 1:
        speed = speed
    elif speed == 2:
        speed = 0.5
    elif speed == 3:
        speed = 0.1
    elif speed == 4:
        speed = 0.02

    def display(hours, minutes, seconds):
        seconds = f"0{seconds}" if seconds < 10 else seconds
        minutes = f"0{minutes}" if minutes < 10 else minutes
        hours = f"0{hours}" if hours < 10 else hours
        label.configure(text=f"{hours}:{minutes}:{seconds}")

    def tksleep(t):
        milliseconds = int(t*1000)
        window = tk._get_default_root('sleep')
        var = tk.IntVar(window)
        window.after(milliseconds, var.set, 1)
        window.wait_variable(var)

    def get_time(hours=0, minutes=0, total_seconds=0):
        seconds = 0
        for value in range(0, total_seconds):
            tksleep(speed)
            if hours > 0 or minutes > 0 and seconds == 0:
                minutes -= 1
                seconds += 59
                display(hours, minutes, seconds)
            else:
                seconds -= 1
                display(hours, minutes, seconds)

        window.destroy()


    window = tk.Toplevel()#Tk()
    window.title("stream timer")
    window.attributes("-fullscreen", True)
    window.attributes("-alpha", 0.8)
    window.configure(bg="black")
    #window.bind("<Escape>", lambda event: window.destroy())
    label = ttk.Label(window, text="", font=(f"{font_f}", 280), foreground=f"{color}", background="black")
    label.pack(expand=True)
    #label.grid(row=0, column=0, pady=280, sticky="we")
    #label.place(height=700, width=1500, relx=.5, rely=.5, anchor="c")
    window.bind("<Escape>", lambda event: get_time(0, 0, 0))#window.destroy())
    get_time(total_hour, minutes, total_sec)
    window.mainloop()

def main():
    color_point = None
    speed_point = 0
    time_point = 0
    font_point = None
    def start_timer():
        time_point = int(set_time.get()) if len(set_time.get()) > 0 else 1
        speed_point = int(set_speed.get()) if len(set_speed.get()) > 0 else 1
        color_point = set_color.get() if len(set_color.get()) > 0 else "red"
        font_point = set_font.get() if len(set_font.get()) > 0 else "Arial"
        if time_point > 0 and speed_point > 0 and len(color_point) > 0:
            draw_window(time_point, color_point, speed_point, font_point)
        else:
            draw_window(time_point)
    def about_message():
        title_message = "stream timer alpha build 0.1a"
        m_info_a = "stream timer by Artemy Gilvanov\nused in project:\nTkinter Library Tcl/Tk 8.6.13"
        m_info_b = "\nNuitka Compiler"
        m_info_c = "\nIcon by Laura Reen"
        showinfo(title=f"{title_message}", message=f"{m_info_a}{m_info_b}{m_info_c}")
    # const region
    COLOR_LST = ["red", "blue", "white", "grey", "cyan", "gold", "yellow", "magenta"]
    SPEED_LST = [1, 2, 3, 4]
    FONT_LST = ["Arial", "Verdana", "Calibri", "Times", "Impact", "Modern", "Romantic", "Txt", "Ink Free"]
    # const end region

    start_window = tk.Tk()
    # const region
    ICON = tk.PhotoImage(file="icon.png")
    # const region end
    start_window.title("stream timer")
    start_window.geometry("765x70")
    start_window.resizable(False, False)
    start_window.iconphoto(True, ICON)
    main_menu = tk.Menu()
    main_menu.add_cascade(label="About", command=about_message)
    start_window.config(menu=main_menu)

    time_label = ttk.Label(start_window, text="set time minutes", width=0)
    color_label = ttk.Label(start_window, text="set color", width=0)
    font_label = ttk.Label(start_window, text="set font", width=0)
    speed_label = ttk.Label(start_window, text="speed modify", width=0)
    start_button = ttk.Button(start_window, text="start", width=25, command=start_timer)
    launch_label = ttk.Label(start_window, text="launch", width=0)

    set_time = ttk.Entry(start_window)
    set_time.insert(-1, "1")
    set_color = ttk.Combobox(start_window, values=COLOR_LST)
    # default value control
    set_color.current(0)
    set_speed = ttk.Combobox(start_window, values=SPEED_LST)
    # default value control
    set_speed.current(0)
    set_font = ttk.Combobox(start_window, values=FONT_LST)
    # default value control
    set_font.current(0)

    time_label.grid(row=0, column=0, padx=5)
    color_label.grid(row=0, column=1, padx=5)
    speed_label.grid(row=0, column=2, padx=5)
    font_label.grid(row=0, column=3, padx=5)
    launch_label.grid(row=0, column=4, padx=5)

    set_time.grid(row=1, column=0, padx=5)
    set_color.grid(row=1, column=1, padx=5)
    set_speed.grid(row=1, column=2, padx=5)
    start_button.grid(row=1, column=4, padx=5)
    set_font.grid(row=1, column=3, padx=5)

    start_window.mainloop()

if __name__ == "__main__":
    main()