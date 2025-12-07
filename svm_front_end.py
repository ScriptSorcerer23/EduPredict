import tkinter as tk
from tkinter import messagebox

# GUI Function to make predictions
def predict():
    try:
        # Retrieve user input
        student_absence_days = float(absence_entry.get())
        
        # Prediction logic based on the given condition
        if 0 < student_absence_days <= 7:
            prediction = "High-performing (1)"
        else:
            prediction = "Low-performing (0)"
        
        # Display result
        result_label.config(text=f"Prediction: {prediction}")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid numerical value for Student Absence Days.")

# GUI Setup
root = tk.Tk()
root.title("SVM Attendance Classifier")

# Instruction Label
instruction = tk.Label(root, text="Enter Student Absence Days (Mapped to Numeric):")
instruction.grid(row=0, column=0, columnspan=2, pady=10)

# Input Field for Student Absence Days
tk.Label(root, text="Student Absence Days:").grid(row=1, column=0, padx=10, pady=5)
absence_entry = tk.Entry(root)
absence_entry.grid(row=1, column=1, padx=10, pady=5)

# Predict Button
predict_button = tk.Button(root, text="Predict", command=predict)
predict_button.grid(row=2, column=0, columnspan=2, pady=10)

# Result Label
result_label = tk.Label(root, text="Prediction: ")
result_label.grid(row=3, column=0, columnspan=2, pady=10)

# Run the GUI
root.mainloop()
