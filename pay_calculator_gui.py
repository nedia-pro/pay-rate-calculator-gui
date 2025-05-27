import tkinter as tk
from tkinter import messagebox

def calculate_pay():
    try:
        hourly_rate = float(entry_hourly_rate.get())
        hours = int(entry_hours.get())
        minutes = int(entry_minutes.get())
        total_hours = hours + minutes / 60
        total_pay = hourly_rate * total_hours
        label_result.config(text=f"Total pay: ${total_pay:.2f}")
    except ValueError:
        messagebox.showerror("Input error", "Please enter valid numbers.")

root = tk.Tk()
root.title("Pay Rate Calculator")

tk.Label(root, text="Hourly Rate ($):").grid(row=0, column=0, padx=10, pady=5, sticky="e")
entry_hourly_rate = tk.Entry(root)
entry_hourly_rate.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Hours Worked:").grid(row=1, column=0, padx=10, pady=5, sticky="e")
entry_hours = tk.Entry(root)
entry_hours.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Minutes Worked:").grid(row=2, column=0, padx=10, pady=5, sticky="e")
entry_minutes = tk.Entry(root)
entry_minutes.grid(row=2, column=1, padx=10, pady=5)

btn_calculate = tk.Button(root, text="Calculate Pay", command=calculate_pay)
btn_calculate.grid(row=3, column=0, columnspan=2, pady=10)

label_result = tk.Label(root, text="Total pay: $0.00", font=("Arial", 14))
label_result.grid(row=4, column=0, columnspan=2, pady=10)

root.mainloop()
