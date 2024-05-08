import tkinter as tk

border_effects = {
    "flat": tk.FLAT,
    "afundado": tk.SUNKEN,
    "elevado": tk.RAISED,
    "borda": tk.GROOVE,
    "ondulado": tk.RIDGE,
}

janela = tk.Tk()

frame_a = tk.Frame()

frame_b = tk.Frame()

label_a = tk.Label(master = frame_a, text="Frame A")
label_a.pack()

label_b = tk.Label(master = frame_b, text="Frame B")
label_b.pack()

frame_a.pack()
frame_b.pack()

janela.mainloop()