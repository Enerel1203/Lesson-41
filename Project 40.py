import tkinter as tk

def calculate():
    p = float(entry_p.get())
    t = float(entry_t.get())
    r = float(entry_r.get())

    si = (p * t * r) / 100
    ci = p * ((1 + r/100) ** t) - p

    label_si.config(text="Simple Interest: " + str(round(si, 2)))
    label_ci.config(text="Compound Interest: " + str(round(ci, 2)))

root = tk.Tk()
root.title("Interest Calculator")
root.geometry("400x300")

tk.Label(root, text="Principal").grid(row=0, column=0)
tk.Label(root, text="Time (years)").grid(row=1, column=0)
tk.Label(root, text="Rate (%)").grid(row=2, column=0)

entry_p = tk.Entry(root)
entry_t = tk.Entry(root)
entry_r = tk.Entry(root)

entry_p.grid(row=0, column=1)
entry_t.grid(row=1, column=1)
entry_r.grid(row=2, column=1)

tk.Button(root, text="Calculate", command=calculate).grid(row=3, column=0, columnspan=2)

label_si = tk.Label(root, text="Simple Interest: 0")
label_ci = tk.Label(root, text="Compound Interest: 0")

label_si.grid(row=4, column=0, columnspan=2)
label_ci.grid(row=5, column=0, columnspan=2)

root.mainloop()